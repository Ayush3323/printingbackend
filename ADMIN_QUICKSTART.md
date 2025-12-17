# Admin Dashboard Integration - Quick Start Guide

## Backend Setup

### 1. Set Superuser Password

The superuser `admin` was created without a password. Set it now:

```bash
cd backend
python manage.py shell
```

Then in the Django shell:
```python
from django.contrib.auth import get_user_model
User = get_user_model()
admin = User.objects.get(username='admin')
admin.set_password('admin123')  # Change this to a secure password
admin.save()
exit()
```

### 2. Verify Server is Running

```bash
python manage.py runserver
```

Server should be at: `http://127.0.0.1:8000`

### 3. Test Admin API (Optional)

```bash
curl --location 'http://127.0.0.1:8000/api/v1/admin/users/' \
--header 'Authorization: Basic YWRtaW46YWRtaW4xMjM='
```

---

## Frontend Setup

### 1. Install Dependencies

Already done: `npm install axios`

### 2. Start Dev Server

```bash
cd admin
npm run dev
```

Frontend should be at: `http://localhost:5173`

### 3. Login

1. Open browser to `http://localhost:5173`
2. Navigate to **Customers** page (click on sidebar)
3. You'll need to login. For now, use browser localStorage:

**Manual Auth (Temporary):**

Open browser console and run:
```javascript
// Base64 encode "admin:admin123"
const auth = btoa('admin:admin123');
localStorage.setItem('adminAuth', auth);
localStorage.setItem('adminUser', 'admin');
location.reload();
```

### 4. Test Customers Page

- Search for users
- View user details (modal)
- Toggle activate/deactivate
- Delete users

---

## Available Admin Features

### Backend APIs

**User Management:**
- `GET /api/v1/admin/users/` - List all users
- `GET /api/v1/admin/users/{id}/` - Get user detail
- `PATCH /api/v1/admin/users/{id}/` - Update user
- `DELETE /api/v1/admin/users/{id}/` - Delete user
- `POST /api/v1/admin/users/{id}/activate/` - Activate user
- `POST /api/v1/admin/users/{id}/deactivate/` - Deactivate user
- `GET /api/v1/admin/users/stats/` - User statistics

**Catalog Management:**
- `GET /api/v1/admin/categories/` - List categories
- `POST /api/v1/admin/categories/` - Create category
- `PATCH /api/v1/admin/categories/{id}/` - Update category
- `DELETE /api/v1/admin/categories/{id}/` - Delete category
- Same pattern for `/admin/subcategories/` and `/admin/products/`

### Frontend Pages

**Completed:**
- ✅ Customers (User Management)

**TODO:**
- ⬜ Products (Product Management)
- ⬜ Categories (Category Tree Management)
- ⬜ Login Page (proper auth flow)

---

## Nested URL Examples

### Old (Flat):
```
/api/v1/categories/
/api/v1/subcategories/
/api/v1/products/
```

### New (Nested):
```
/api/v1/categories/1/subcategories/
/api/v1/categories/1/subcategories/1/products/
```

---

## Next Steps

1. **Set superuser password** (see step 1 above)
2. **Test Customers page** with real data
3. **Create Products page** (similar to Customers)
4. **Create Login page** (proper authentication flow)
