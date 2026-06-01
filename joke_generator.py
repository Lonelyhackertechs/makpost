"""
Random Joke Generator using external API
Uses the JokeAPI (https://jokeapi.dev/) to fetch random jokes
"""

import requests
import json
from typing import Dict, Optional


class JokeGenerator:
    """A class to generate random jokes using external APIs"""
    
    BASE_URL = "https://v2.jokeapi.dev/joke/"
    
    CATEGORIES = {
        "general": "Any",
        "programming": "Programming",
        "knock_knock": "Knock-Knock",
        "all": "Any"
    }
    
    def __init__(self, timeout: int = 5):
        """
        Initialize the JokeGenerator
        
        Args:
            timeout (int): Request timeout in seconds (default: 5)
        """
        self.timeout = timeout
    
    def get_random_joke(self, category: str = "Any", 
                       safe_mode: bool = True) -> Optional[Dict]:
        """
        Fetch a random joke from the API
        
        Args:
            category (str): Joke category - "Any", "Programming", "Knock-Knock", etc.
            safe_mode (bool): If True, filters out offensive jokes (default: True)
            
        Returns:
            Optional[Dict]: Joke data or None if request fails
        """
        try:
            # Build the URL with parameters
            flags = "?safe-mode" if safe_mode else ""
            url = f"{self.BASE_URL}{category}{flags}"
            
            # Make the request
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            
            data = response.json()
            
            # Check if the API returned an error
            if data.get("error"):
                print(f"API Error: {data.get('message', 'Unknown error')}")
                return None
            
            return data
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching joke: {e}")
            return None
    
    def format_joke(self, joke_data: Dict) -> str:
        """
        Format joke data for display
        
        Args:
            joke_data (Dict): Joke data from API
            
        Returns:
            str: Formatted joke text
        """
        if not joke_data:
            return "Could not fetch a joke. Please try again."
        
        if joke_data.get("type") == "single":
            # Single-part joke
            return joke_data.get("joke", "No joke content")
        
        elif joke_data.get("type") == "twopart":
            # Two-part joke (setup and delivery)
            setup = joke_data.get("setup", "")
            delivery = joke_data.get("delivery", "")
            return f"{setup}\n\n{delivery}"
        
        return "Unknown joke format"
    
    def get_and_display_joke(self, category: str = "Any", 
                            safe_mode: bool = True) -> None:
        """
        Get a random joke and display it nicely
        
        Args:
            category (str): Joke category
            safe_mode (bool): If True, filters out offensive jokes
        """
        joke_data = self.get_random_joke(category, safe_mode)
        formatted_joke = self.format_joke(joke_data)
        
        print("\n" + "="*60)
        print("🎭 HERE'S A RANDOM JOKE FOR YOU 🎭")
        print("="*60)
        print(formatted_joke)
        print("="*60 + "\n")


def main():
    """Main function to demonstrate the joke generator"""
    
    generator = JokeGenerator()
    
    # Example 1: Get a random joke from any category
    print("Getting a random joke...")
    generator.get_and_display_joke(category="Any", safe_mode=True)
    
    # Example 2: Get a programming joke
    print("Getting a programming joke...")
    generator.get_and_display_joke(category="Programming", safe_mode=True)
    
    # Example 3: Get a knock-knock joke
    print("Getting a knock-knock joke...")
    generator.get_and_display_joke(category="Knock-Knock", safe_mode=True)


if __name__ == "__main__":
    main()
