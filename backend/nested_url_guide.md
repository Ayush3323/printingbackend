# Nested URL Testing Guide

## New URL Structure

The backend now supports **nested URL routing**:

### Category → Subcategory → Product Hierarchy

**Old Structure (Flat):**
```
/api/v1/categories/
/api/v1/subcategories/
/api/v1/products/
```

**New Structure (Nested):**
```
/api/v1/categories/                              # List all categories
/api/v1/categories/{id}/                         # Get category detail
/api/v1/categories/{id}/subcategories/           # List subcategories under category
/api/v1/categories/{id}/subcategories/{sub_id}/  # Get subcategory detail
/api/v1/categories/{id}/subcategories/{sub_id}/products/  # List products under subcategory
```

**Backward Compatibility:**
- Old flat routes still work: `/api/v1/products/`
- Query params still supported: `/api/v1/products/?category=marketing-materials`

---

## Testing Examples

### 1. Create Category
```bash
POST /api/v1/categories/
{
    "name": "Marketing Materials",
    "slug": "marketing-materials"
}
# Response: { "id": 1, "name": "Marketing Materials", ... }
```

### 2. Create Subcategory Under Category
```bash
POST /api/v1/categories/1/subcategories/
{
    "category": 1,
    "name": "Business Cards",
    "slug": "business-cards"
}
# Response: { "id": 1, "name": "Business Cards", "category": 1, ... }
```

### 3. List Subcategories of a Category
```bash
GET /api/v1/categories/1/subcategories/
# Response: [{ "id": 1, "name": "Business Cards", ... }]
```

### 4. Create Product Under Subcategory
```bash
POST /api/v1/categories/1/subcategories/1/products/
{
    "subcategory": 1,
    "name": "Premium Card",
    "slug": "premium-card",
    "sku": "BC-001",
    "base_price": "15.00"
}
```

### 5. List Products of a Subcategory
```bash
GET /api/v1/categories/1/subcategories/1/products/
# Response: [{ "id": 1, "name": "Premium Card", ... }]
```

---

## Benefits

1. **RESTful Design**: URLs reflect resource hierarchy
2. **Clear Relationships**: Easy to understand parent-child structure
3. **Filtered by Default**: Nested routes auto-filter by parent
4. **Frontend Friendly**: Easier to build category/subcategory navigation

---

## URL Patterns Summary

| URL Pattern | Description |
|-------------|-------------|
| `GET /categories/` | List all categories |
| `POST /categories/` | Create category |
| `GET /categories/{id}/` | Get category detail |
| `GET /categories/{id}/subcategories/` | List subcategories of category {id} |
| `POST /categories/{id}/subcategories/` | Create subcategory under category {id} |
| `GET /categories/{id}/subcategories/{sub_id}/` | Get subcategory detail |
| `GET /categories/{id}/subcategories/{sub_id}/products/` | List products of subcategory {sub_id} |
| `POST /categories/{id}/subcategories/{sub_id}/products/` | Create product under subcategory {sub_id} |
