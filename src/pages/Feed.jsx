import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import postsService from '../services/posts';
import PostCard from '../components/PostCard';
import '../styles/Feed.css';

export const Feed = () => {
    const [posts, setPosts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');
    const [page, setPage] = useState(1);
    const [hasMore, setHasMore] = useState(true);
    const { isAuthenticated } = useAuth();
    const navigate = useNavigate();

    useEffect(() => {
        loadPosts();
    }, [page]);

    const loadPosts = async () => {
        try {
            setLoading(true);
            const response = await postsService.getAllPosts(page);
            setPosts(response.results || []);
            setHasMore(!!response.next);
        } catch (err) {
            setError('Failed to load posts');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const handlePostDeleted = (deletedPostId) => {
        setPosts(posts.filter(post => post.id !== deletedPostId));
    };

    return (
        <div className='feed-container'>
            <div className='feed-header'>
                <h1>MakPost Feed</h1>
                {isAuthenticated && (
                    <button onClick={() => navigate('/create-post')} className='btn-primary'>Create Post</button>
                )}
            </div>
            {error && <div className='error-message'>{error}</div>}
            <div className='posts-list'>
                {loading ? (
                    <div className='loading'>Loading posts...</div>
                ) : posts.length === 0 ? (
                    <div className='no-posts'>No posts yet. Be the first to create one!</div>
                ) : (
                    posts.map(post => (
                        <PostCard key={post.id} post={post} onPostDeleted={handlePostDeleted} />
                    ))
                )}
            </div>
            <div className='pagination'>
                {page > 1 && (
                    <button onClick={() => setPage(page - 1)} className='btn-secondary'>Previous</button>
                )}
                {hasMore && (
                    <button onClick={() => setPage(page + 1)} className='btn-secondary'>Next</button>
                )}
            </div>
        </div>
    );
};

export default Feed;