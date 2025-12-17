# Admin Dashboard Setup Guide

## Current Status: ✅ Backend Ready | ⚠️ Authentication Needed

---

## Quick Start (5 Steps)

### Step 1: Set Superuser Password (REQUIRED)

```bash
cd backend
python manage.py shell
```

In the Django shell:
```python
from django.contrib.auth import get_user_model
User = get_user_model()
admin = User.objects.get(username='admin')
admin.set_password('admin123')  # ⚠️ Change to secure password!
admin.save()
exit()
```

### Step 2: Add Authentication to Frontend (Temporary)

Open your browser at `http://localhost:5173`

Press `F12` to open console, then run:
```javascript
// Replace 'admin123' with your password from Step 1
const auth = btoa('admin:admin123');
localStorage.setItem('adminAuth', auth);
localStorage.setItem('adminUser', 'admin');
location.reload();
```

### Step 3: Navigate to Admin Pages

Click on the sidebar:
- **Customers** - Manage users
- **Products** - Manage products  
- **Categories** - Manage category tree

### Step 4: Create Your First Category & Subcategory

1. Go to **Categories** page
2. Click **"+ Add Category"**
3. Fill in:
   - Name: `Marketing Materials`
   - Slug: `marketing-materials`
4. Click **Create**
5. Click **"+ Add Subcategory"** under the new category
6. Fill in:
   - Name: `Business Cards`
   - Slug: `business-cards`
7. Click **Create**

### Step 5: Create Your First Product

1. Go to **Products** page
2. Click **"+ Add Product"**
3. Fill in:
   - Name: `Premium Business Card`
   - Slug: `premium-business-card`
   - SKU: `BC-001`
   - Subcategory: Select "Business Cards"
   - Price: `15.00`
   - Stock: `100`
4. Click **Create**

---

## What You Can Do Now

### ✅ Ready to Use Features:

1. **User Management** (`/customers`)
   - ✅ Create new users (via "+ Create User" button)
   - ✅ View all users
   - ✅ Activate/Deactivate users
   - ✅ Delete users
   - ✅ Search users

2. **Category Management** (`/categories`)
   - ✅ Create categories (top-level)
   - ✅ Create subcategories (under categories)
   - ✅ Edit categories/subcategories
   - ✅ Delete categories/subcategories
   - ✅ Tree view hierarchy

3. **Product Management** (`/products`)
   - ✅ Create products (with subcategory)
   - ✅ Edit products
   - ✅ Delete products
   - ✅ Search products
   - ✅ Set price, stock, active status

---

## Data Upload Workflow

**Recommended Order:**

```
1. Categories (Root)
   ↓
2. Subcategories (Under Categories)
   ↓
3. Products (Under Subcategories)
   ↓
4. Users/Customers (Can be done anytime)
```

---

## Important Notes

### ⚠️ CORS is now configured
- `localhost:5173` is allowed
- Credentials are enabled

### ⚠️ No Login Page Yet
- Currently using localStorage (temporary)
- You can build a proper login page later

### ⚠️ Data Hierarchy
- **Must create Categories first**
- **Then Subcategories**
- **Then Products** (products require subcategories)

---

## Troubleshooting

### "Authentication required" error:
- Run Step 2 again (set localStorage)
- Make sure password is correct

### "No subcategories available":
- Go to Categories page
- Create a category first
- Then create subcategories under it

### CORS errors:
- Backend is already configured
- Make sure Django server is running: `python manage.py runserver`

---

## Next Steps (Optional)

- Build a proper Login page
- Add image upload for products
- Add bulk import functionality
- Add user role management

---

## Summary

**You are READY to add data!**

1. ✅ Set admin password (Step 1)
2. ✅ Add auth to browser (Step 2)  
3. ✅ Create Categories → Subcategories → Products
4. ✅ Create users via "+ Create User" button

**No database deletion needed - everything is ready!**
