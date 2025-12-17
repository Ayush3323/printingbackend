import React, { useState, useEffect } from 'react';
import { adminCatalogAPI } from '../services/api';
import './Products.css';

const Products = () => {
    const [products, setProducts] = useState([]);
    const [categories, setCategories] = useState([]);
    const [subcategories, setSubcategories] = useState([]);
    const [loading, setLoading] = useState(true);
    const [showModal, setShowModal] = useState(false);
    const [editingProduct, setEditingProduct] = useState(null);
    const [searchTerm, setSearchTerm] = useState('');

    const [formData, setFormData] = useState({
        name: '',
        slug: '',
        sku: '',
        subcategory: '',
        description: '',
        base_price: '',
        stock_quantity: 0,
        is_active: true,
    });

    useEffect(() => {
        fetchProducts();
        fetchCategories();
        fetchSubcategories();
    }, []);

    const fetchProducts = async () => {
        try {
            setLoading(true);
            const response = await adminCatalogAPI.getProducts({ search: searchTerm });
            setProducts(response.data || []);
        } catch (error) {
            console.error('Error fetching products:', error);
            setProducts([]);
            if (error.response?.status === 401) {
                alert('Authentication required. Please set your credentials.');
            } else {
                alert('Failed to fetch products');
            }
        } finally {
            setLoading(false);
        }
    };

    const fetchCategories = async () => {
        try {
            const response = await adminCatalogAPI.getCategories();
            setCategories(response.data || []);
        } catch (error) {
            console.error('Error fetching categories:', error);
            setCategories([]);
        }
    };

    const fetchSubcategories = async () => {
        try {
            const response = await adminCatalogAPI.getSubcategories();
            setSubcategories(response.data || []);
        } catch (error) {
            console.error('Error fetching subcategories:', error);
            setSubcategories([]);
        }
    };

    const handleSearch = (e) => {
        e.preventDefault();
        fetchProducts();
    };

    const openCreateModal = () => {
        setEditingProduct(null);
        setFormData({
            name: '',
            slug: '',
            sku: '',
            subcategory: '',
            description: '',
            base_price: '',
            stock_quantity: 0,
            is_active: true,
        });
        setShowModal(true);
    };

    const openEditModal = (product) => {
        setEditingProduct(product);
        setFormData({
            name: product.name || '',
            slug: product.slug || '',
            sku: product.sku || '',
            subcategory: product.subcategory || '',
            description: product.description || '',
            base_price: product.base_price || '',
            stock_quantity: product.stock_quantity || 0,
            is_active: product.is_active ?? true,
        });
        setShowModal(true);
    };

    const handleInputChange = (e) => {
        const { name, value, type, checked } = e.target;
        setFormData({
            ...formData,
            [name]: type === 'checkbox' ? checked : value,
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            if (editingProduct) {
                await adminCatalogAPI.updateProduct(editingProduct.id, formData);
                alert('Product updated successfully');
            } else {
                await adminCatalogAPI.createProduct(formData);
                alert('Product created successfully');
            }
            setShowModal(false);
            fetchProducts();
        } catch (error) {
            console.error('Error saving product:', error);
            alert('Failed to save product: ' + (error.response?.data?.detail || error.message));
        }
    };

    const handleDelete = async (productId) => {
        if (window.confirm('Are you sure you want to delete this product?')) {
            try {
                await adminCatalogAPI.deleteProduct(productId);
                alert('Product deleted successfully');
                fetchProducts();
            } catch (error) {
                console.error('Error deleting product:', error);
                alert('Failed to delete product');
            }
        }
    };

    if (loading) {
        return <div className="loading">Loading products...</div>;
    }

    return (
        <div className="products-page">
            <div className="page-header">
                <h1>Product Management</h1>
                <div className="header-actions">
                    <form onSubmit={handleSearch} className="search-bar">
                        <input
                            type="text"
                            placeholder="Search products..."
                            value={searchTerm}
                            onChange={(e) => setSearchTerm(e.target.value)}
                        />
                        <button type="submit">Search</button>
                    </form>
                    <button onClick={openCreateModal} className="btn-primary">
                        + Add Product
                    </button>
                </div>
            </div>

            <div className="products-table-container">
                <table className="products-table">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>SKU</th>
                            <th>Subcategory</th>
                            <th>Price</th>
                            <th>Stock</th>
                            <th>Status</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {products.length === 0 ? (
                            <tr>
                                <td colSpan="8" style={{ textAlign: 'center', padding: '40px', color: '#6b7280' }}>
                                    No products available. Click "Add Product" to create one.
                                </td>
                            </tr>
                        ) : (
                            products.map((product) => (
                                <tr key={product.id}>
                                    <td>{product.id}</td>
                                    <td>{product.name || 'Not Available'}</td>
                                    <td><code>{product.sku || 'N/A'}</code></td>
                                    <td>{product.subcategory_name || 'Not Available'}</td>
                                    <td>₹{product.base_price || '0.00'}</td>
                                    <td>{product.stock_quantity ?? 'N/A'}</td>
                                    <td>
                                        <span className={`status-badge ${product.is_active ? 'active' : 'inactive'}`}>
                                            {product.is_active ? 'Active' : 'Inactive'}
                                        </span>
                                    </td>
                                    <td>
                                        <div className="action-buttons">
                                            <button onClick={() => openEditModal(product)} className="btn-edit">
                                                Edit
                                            </button>
                                            <button onClick={() => handleDelete(product.id)} className="btn-delete">
                                                Delete
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                            ))
                        )}
                    </tbody>
                </table>
            </div>

            {showModal && (
                <div className="modal-overlay" onClick={() => setShowModal(false)}>
                    <div className="modal-content modal-large" onClick={(e) => e.stopPropagation()}>
                        <div className="modal-header">
                            <h2>{editingProduct ? 'Edit Product' : 'Create Product'}</h2>
                            <button onClick={() => setShowModal(false)} className="modal-close">
                                ×
                            </button>
                        </div>
                        <form onSubmit={handleSubmit} className="modal-body">
                            <div className="form-grid">
                                <div className="form-group">
                                    <label>Product Name *</label>
                                    <input
                                        type="text"
                                        name="name"
                                        value={formData.name}
                                        onChange={handleInputChange}
                                        required
                                    />
                                </div>

                                <div className="form-group">
                                    <label>Slug *</label>
                                    <input
                                        type="text"
                                        name="slug"
                                        value={formData.slug}
                                        onChange={handleInputChange}
                                        required
                                    />
                                </div>

                                <div className="form-group">
                                    <label>SKU *</label>
                                    <input
                                        type="text"
                                        name="sku"
                                        value={formData.sku}
                                        onChange={handleInputChange}
                                        required
                                    />
                                </div>

                                <div className="form-group">
                                    <label>Subcategory *</label>
                                    <select
                                        name="subcategory"
                                        value={formData.subcategory}
                                        onChange={handleInputChange}
                                        required
                                    >
                                        <option value="">Select Subcategory</option>
                                        {subcategories.length === 0 ? (
                                            <option value="" disabled>No subcategories available - Create categories first</option>
                                        ) : (
                                            subcategories.map((sub) => (
                                                <option key={sub.id} value={sub.id}>
                                                    {sub.name}
                                                </option>
                                            ))
                                        )}
                                    </select>
                                </div>

                                <div className="form-group">
                                    <label>Base Price *</label>
                                    <input
                                        type="number"
                                        step="0.01"
                                        name="base_price"
                                        value={formData.base_price}
                                        onChange={handleInputChange}
                                        required
                                    />
                                </div>

                                <div className="form-group">
                                    <label>Stock Quantity</label>
                                    <input
                                        type="number"
                                        name="stock_quantity"
                                        value={formData.stock_quantity}
                                        onChange={handleInputChange}
                                    />
                                </div>

                                <div className="form-group full-width">
                                    <label>Description</label>
                                    <textarea
                                        name="description"
                                        value={formData.description}
                                        onChange={handleInputChange}
                                        rows="3"
                                    />
                                </div>

                                <div className="form-group">
                                    <label className="checkbox-label">
                                        <input
                                            type="checkbox"
                                            name="is_active"
                                            checked={formData.is_active}
                                            onChange={handleInputChange}
                                        />
                                        <span>Active</span>
                                    </label>
                                </div>
                            </div>

                            <div className="modal-footer">
                                <button type="button" onClick={() => setShowModal(false)} className="btn-secondary">
                                    Cancel
                                </button>
                                <button type="submit" className="btn-primary">
                                    {editingProduct ? 'Update' : 'Create'}
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            )}
        </div>
    );
};

export default Products;
