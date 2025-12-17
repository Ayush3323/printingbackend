import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api/v1';

// Create axios instance with default config
const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Add auth interceptor
api.interceptors.request.use((config) => {
    const auth = localStorage.getItem('adminAuth');
    if (auth) {
        config.headers.Authorization = `Basic ${auth}`;
    }
    return config;
});

// Admin User Management APIs
export const adminUserAPI = {
    getUsers: (params) => api.get('/admin/users/', { params }),
    getUser: (id) => api.get(`/admin/users/${id}/`),
    updateUser: (id, data) => api.patch(`/admin/users/${id}/`, data),
    deleteUser: (id) => api.delete(`/admin/users/${id}/`),
    deactivateUser: (id) => api.post(`/admin/users/${id}/deactivate/`),
    activateUser: (id) => api.post(`/admin/users/${id}/activate/`),
    getUserStats: () => api.get('/admin/users/stats/'),
};

// Admin Catalog Management APIs
export const adminCatalogAPI = {
    // Categories
    getCategories: (params) => api.get('/admin/categories/', { params }),
    getCategory: (id) => api.get(`/admin/categories/${id}/`),
    createCategory: (data) => api.post('/admin/categories/', data),
    updateCategory: (id, data) => api.patch(`/admin/categories/${id}/`, data),
    deleteCategory: (id) => api.delete(`/admin/categories/${id}/`),
    getCategoryStats: () => api.get('/admin/categories/stats/'),

    // Subcategories
    getSubcategories: (params) => api.get('/admin/subcategories/', { params }),
    getSubcategory: (id) => api.get(`/admin/subcategories/${id}/`),
    createSubcategory: (data) => api.post('/admin/subcategories/', data),
    updateSubcategory: (id, data) => api.patch(`/admin/subcategories/${id}/`, data),
    deleteSubcategory: (id) => api.delete(`/admin/subcategories/${id}/`),

    // Products
    getProducts: (params) => api.get('/admin/products/', { params }),
    getProduct: (id) => api.get(`/admin/products/${id}/`),
    createProduct: (data) => api.post('/admin/products/', data),
    updateProduct: (id, data) => api.patch(`/admin/products/${id}/`, data),
    deleteProduct: (id) => api.delete(`/admin/products/${id}/`),
    bulkUpdateStock: (updates) => api.post('/admin/products/bulk_update_stock/', { updates }),
    getProductStats: () => api.get('/admin/products/stats/'),
};

// Auth API
export const authAPI = {
    login: (username, password) => {
        const credentials = btoa(`${username}:${password}`);
        localStorage.setItem('adminAuth', credentials);
        localStorage.setItem('adminUser', username);
        return Promise.resolve({ username });
    },
    logout: () => {
        localStorage.removeItem('adminAuth');
        localStorage.removeItem('adminUser');
    },
    isAuthenticated: () => {
        return !!localStorage.getItem('adminAuth');
    },
    getUser: () => {
        return localStorage.getItem('adminUser');
    },
};

export default api;
