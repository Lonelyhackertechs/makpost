import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import postsService from '../services/posts';
import '../styles/CreatePost.css';

export const CreatePost = () => {
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');
    const [image, setImage] = useState(null);
    const [video, setVideo] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const { user } = useAuth();
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        try {
            setLoading(true);
            await postsService.createPost({
                title,
                content,
                image,
                video,
                college: user?.college,
            });
            navigate('/');
        } catch (err) {
            setError(err.error || err.message || 'Failed to create post');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className='create-post-container'>
            <div className='create-post-box'>
                <h1>Create a New Post</h1>
                {error && <div className='error-message'>{error}</div>}
                <form onSubmit={handleSubmit}>
                    <div className='form-group'>
                        <label>Title *</label>
                        <input type='text' value={title} onChange={(e) => setTitle(e.target.value)} placeholder='Post title' required />
                    </div>
                    <div className='form-group'>
                        <label>Content *</label>
                        <textarea value={content} onChange={(e) => setContent(e.target.value)} placeholder='What\'s on your mind?' rows='6' required />
                    </div>
                    <div className='form-group'>
                        <label>Image (Optional)</label>
                        <input type='file' accept='image/*' onChange={(e) => setImage(e.target.files[0])} />
                    </div>
                    <div className='form-group'>
                        <label>Video (Optional)</label>
                        <input type='file' accept='video/*' onChange={(e) => setVideo(e.target.files[0])} />
                    </div>
                    <div className='button-group'>
                        <button type='submit' disabled={loading} className='btn-primary'>{loading ? 'Creating...' : 'Create Post'}</button>
                        <button type='button' onClick={() => navigate('/')} className='btn-secondary'>Cancel</button>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default CreatePost;