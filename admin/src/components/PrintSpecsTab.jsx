import React, { useState, useEffect } from 'react';
import { adminCatalogAPI } from '../services/api';

const PrintSpecsTab = ({ productId }) => {
    const [printSpecs, setPrintSpecs] = useState(null);
    const [loading, setLoading] = useState(true);
    const [editing, setEditing] = useState(false);

    const [formData, setFormData] = useState({
        width_mm: '',
        height_mm: '',
        bleed_margin_mm: 3.0,
        safe_zone_mm: 3.0,
        format_template_url: '',
        allowed_file_types: 'pdf,jpg,png,svg',
        min_resolution_dpi: 300
    });

    useEffect(() => {
        if (productId) {
            fetchPrintSpecs();
        }
    }, [productId]);

    const fetchPrintSpecs = async () => {
        try {
            setLoading(true);
            const response = await adminCatalogAPI.getPrintSpecs({ product: productId });
            if (response.data && response.data.length > 0) {
                setPrintSpecs(response.data[0]);
                setFormData(response.data[0]);
            } else {
                setPrintSpecs(null);
            }
        } catch (error) {
            console.error('Error fetching print specs:', error);
        } finally {
            setLoading(false);
        }
    };

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSave = async () => {
        try {
            const data = {
                ...formData,
                product: productId
            };

            if (printSpecs) {
                await adminCatalogAPI.updatePrintSpec(printSpecs.id, data);
            } else {
                await adminCatalogAPI.createPrintSpec(data);
            }

            alert('Print specifications saved successfully');
            setEditing(false);
            fetchPrintSpecs();
        } catch (error) {
            console.error('Error saving print specs:', error);
            alert('Failed to save print specs: ' + (error.response?.data?.detail || error.message));
        }
    };

    const handleDelete = async () => {
        if (window.confirm('Delete print specifications?')) {
            try {
                await adminCatalogAPI.deletePrintSpec(printSpecs.id);
                setPrintSpecs(null);
                setFormData({
                    width_mm: '',
                    height_mm: '',
                    bleed_margin_mm: 3.0,
                    safe_zone_mm: 3.0,
                    format_template_url: '',
                    allowed_file_types: 'pdf,jpg,png,svg',
                    min_resolution_dpi: 300
                });
            } catch (error) {
                console.error('Error deleting print specs:', error);
                alert('Failed to delete print specs');
            }
        }
    };

    if (loading) return <div>Loading print specifications...</div>;

    return (
        <div className="print-specs-tab">
            <div className="tab-header">
                <h3>Print Specifications</h3>
                {printSpecs && !editing && (
                    <div className="header-actions">
                        <button onClick={() => setEditing(true)} className="btn-primary">Edit</button>
                        <button onClick={handleDelete} className="btn-delete">Delete</button>
                    </div>
                )}
                {!printSpecs && (
                    <button onClick={() => setEditing(true)} className="btn-primary">+ Add Print Specs</button>
                )}
            </div>

            {!editing && printSpecs ? (
                <div className="specs-display">
                    <div className="spec-row">
                        <label>Dimensions:</label>
                        <span>{printSpecs.width_mm} × {printSpecs.height_mm} mm</span>
                    </div>
                    <div className="spec-row">
                        <label>Bleed Margin:</label>
                        <span>{printSpecs.bleed_margin_mm} mm</span>
                    </div>
                    <div className="spec-row">
                        <label>Safe Zone:</label>
                        <span>{printSpecs.safe_zone_mm} mm</span>
                    </div>
                    <div className="spec-row">
                        <label>Min Resolution:</label>
                        <span>{printSpecs.min_resolution_dpi} DPI</span>
                    </div>
                    <div className="spec-row">
                        <label>Allowed File Types:</label>
                        <span>{printSpecs.allowed_file_types}</span>
                    </div>
                    {printSpecs.format_template_url && (
                        <div className="spec-row">
                            <label>Template URL:</label>
                            <a href={printSpecs.format_template_url} target="_blank" rel="noopener noreferrer">
                                {printSpecs.format_template_url}
                            </a>
                        </div>
                    )}
                </div>
            ) : editing || !printSpecs ? (
                <div className="specs-form">
                    <div className="form-row">
                        <div className="form-group">
                            <label>Width (mm) *</label>
                            <input
                                type="number"
                                step="0.1"
                                name="width_mm"
                                value={formData.width_mm}
                                onChange={handleInputChange}
                                required
                            />
                        </div>
                        <div className="form-group">
                            <label>Height (mm) *</label>
                            <input
                                type="number"
                                step="0.1"
                                name="height_mm"
                                value={formData.height_mm}
                                onChange={handleInputChange}
                                required
                            />
                        </div>
                    </div>

                    <div className="form-row">
                        <div className="form-group">
                            <label>Bleed Margin (mm)</label>
                            <input
                                type="number"
                                step="0.1"
                                name="bleed_margin_mm"
                                value={formData.bleed_margin_mm}
                                onChange={handleInputChange}
                            />
                        </div>
                        <div className="form-group">
                            <label>Safe Zone (mm)</label>
                            <input
                                type="number"
                                step="0.1"
                                name="safe_zone_mm"
                                value={formData.safe_zone_mm}
                                onChange={handleInputChange}
                            />
                        </div>
                    </div>

                    <div className="form-row">
                        <div className="form-group">
                            <label>Min Resolution (DPI)</label>
                            <input
                                type="number"
                                name="min_resolution_dpi"
                                value={formData.min_resolution_dpi}
                                onChange={handleInputChange}
                            />
                        </div>
                        <div className="form-group">
                            <label>Allowed File Types</label>
                            <input
                                type="text"
                                name="allowed_file_types"
                                value={formData.allowed_file_types}
                                onChange={handleInputChange}
                                placeholder="pdf,jpg,png,svg"
                            />
                        </div>
                    </div>

                    <div className="form-group">
                        <label>Format Template URL</label>
                        <input
                            type="url"
                            name="format_template_url"
                            value={formData.format_template_url}
                            onChange={handleInputChange}
                            placeholder="https://example.com/template.ai"
                        />
                    </div>

                    <div className="form-footer">
                        {editing && (
                            <button onClick={() => setEditing(false)} className="btn-secondary">Cancel</button>
                        )}
                        <button onClick={handleSave} className="btn-primary">
                            {printSpecs ? 'Update' : 'Create'} Specifications
                        </button>
                    </div>
                </div>
            ) : (
                <div className="empty-state">
                    <p>No print specifications defined for this product.</p>
                </div>
            )}
        </div>
    );
};

export default PrintSpecsTab;
