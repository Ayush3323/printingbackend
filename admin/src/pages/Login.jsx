import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import './Login.css';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const { login } = useAuth();
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setLoading(true);

        try {
            // First, try to authenticate with the backend
            const response = await fetch('http://127.0.0.1:8000/api/v1/admin/users/', {
                method: 'GET',
                headers: {
                    'Authorization': `Basic ${btoa(`${username}:${password}`)}`,
                },
            });

            if (response.ok) {
                // Valid credentials
                const result = login(username, password);
                if (result.success) {
                    navigate('/');
                } else {
                    setError('Login failed');
                }
            } else if (response.status === 401) {
                setError('Invalid username or password');
            } else {
                setError('Server error. Please try again.');
            }
        } catch (err) {
            console.error('Login error:', err);
            setError('Network error. Please check if the server is running.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="login-container">
            <div className="login-card">
                <div className="login-header">
                    <h1>Admin Dashboard</h1>
                    <p>Sign in to continue</p>
                </div>

                <form onSubmit={handleSubmit} className="login-form">
                    {error && (
                        <div className="error-message">
                            {error}
                        </div>
                    )}

                    <div className="form-group">
                        <label htmlFor="username">Username</label>
                        <input
                            id="username"
                            type="text"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            placeholder="Enter your username"
                            required
                            autoFocus
                        />
                    </div>

                    <div className="form-group">
                        <label htmlFor="password">Password</label>
                        <input
                            id="password"
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            placeholder="Enter your password"
                            required
                        />
                    </div>

                    <button type="submit" className="login-btn" disabled={loading}>
                        {loading ? 'Signing in...' : 'Sign In'}
                    </button>
                </form>

                <div className="login-footer">
                    <p className="default-credentials">
                        Default credentials: <br />
                        <strong>Username:</strong> admin <br />
                        <strong>Password:</strong> (set during setup)
                    </p>
                </div>
            </div>
        </div>
    );
};

export default Login;
