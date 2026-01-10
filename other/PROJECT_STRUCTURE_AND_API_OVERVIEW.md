# Vistaprint Clone - Complete Project Structure & API Overview

## 📁 Project Structure

```
vistaprint/
├── backend/              # Django REST Framework API
│   ├── apps/
│   │   ├── users/       # User management & authentication
│   │   ├── catalog/     # Products, categories, subcategories
│   │   ├── designs/     # Design engine, templates, assets
│   │   ├── orders/      # Order management & fulfillment
│   │   └── zakeke/      # Zakeke integration (product customization)
│   ├── shop_project/    # Django project settings
│   ├── manage.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env            # Environment variables
│
├── frontend_/           # Customer-facing frontend (React + Vite)
│   └── src/
│       ├── pages/      # Homepage, Product, Cart, Editor, etc.
│       ├── components/ # Navbar, Footer, ProductCarousel, etc.
│       ├── services/   # API service layers
│       └── context/    # React context providers
│
├── admin/               # Admin dashboard frontend (React + Vite)
│   └── src/
│       ├── pages/      # Admin management pages
│       ├── components/ # Admin UI components
│       └── services/   # Admin API services
│
└── other/              # Documentation & guides
    ├── documentation.md
    ├── DOCKER_GUIDE.md
    └── postman/        # API testing collection
```

---

## 🛠 Technology Stack

### Backend
- **Framework:** Django 5.0+ with Django REST Framework
- **Database:** PostgreSQL 15
- **Authentication:** Basic Auth (Username/Password), Session-based
- **Storage:** 
  - Static files: WhiteNoise
  - Media files: Local storage (S3 URLs stored in database)
- **CORS:** django-cors-headers
- **Other:** 
  - Pillow (image processing)
  - python-dotenv (environment variables)
  - drf-nested-routers (nested API routes)
  - gunicorn (production server)
  - requests (Zakeke API integration)

### Frontend
- **Customer Frontend:** React + Vite
- **Admin Frontend:** React + Vite
- **Styling:** CSS, Tailwind CSS (in frontend_)
- **HTTP Client:** Axios

### Infrastructure
- **Containerization:** Docker + Docker Compose
- **Deployment:** Hostinger VPS (Gunicorn + Nginx)
- **Database:** PostgreSQL

---

## 🗄 Database Models Overview

### 1. Users App (`apps/users/models.py`)

#### User
- Extends Django's AbstractUser
- Fields: role, phone, avatar, company_name, tax_id, is_verified
- B2B fields: company_name, tax_id

#### Role
- Defines user access levels (Customer, Print Shop Manager, Admin, etc.)

#### Address
- User addresses (billing/shipping)
- Fields: recipient_name, street, city, state, zip_code, country
- Support for default addresses per type

### 2. Catalog App (`apps/catalog/models.py`)

#### Category
- Top-level product categories
- Fields: name, slug, description, image, is_active, display_order

#### Subcategory
- Child categories within categories
- Fields: name, slug, category (FK), image, is_active

#### Product
- Core product model
- Fields: name, slug, sku, description, base_price
- Discounts: discount_type, discount_value, discount_start_date, discount_end_date
- Media: primary_image (S3 URL)
- Inventory: stock_quantity, is_infinite_stock
- Computed: final_price (property method)
- SEO: meta_title, meta_description

#### ProductImage
- Product gallery images
- Fields: product (FK), image (S3 URL), alt_text, display_order, is_primary

#### ProductReview
- Customer reviews
- Fields: product (FK), user (FK), rating (1-5), title, comment, helpful_count
- Constraints: One review per user per product

#### Banner
- Hero banners and promotions
- Fields: title, subtitle, image (S3 URL), placement, buttons_json, is_active
- Date ranges: start_date, end_date

### 3. Designs App (`apps/designs/models.py`)

#### SavedDesign
- User-created designs
- Fields: user (FK), product (FK), name, design_json (Fabric.js canvas state)
- Preview: preview_image, thumbnail_high_res
- Versioning: version number
- Organization: tags (JSON array), is_template

#### Asset
- User-uploaded assets (images, logos)
- Fields: user (FK), file, type, original_filename, size_bytes, mime_type, resolution_dpi

#### Template
- Pre-designed templates
- Fields: product (FK), name, description, surface, design_json, subcategory (FK)
- Organization: tags (JSON array), locked, is_active

#### TemplateElement
- Elements within templates (text/image)
- Fields: template (FK), type, default_text, default_image
- Positioning: x_percent, y_percent, max_width_percent, rotation
- Styling: font_family, font_size, color

#### Font
- Available fonts for design tool
- Fields: name, family, file, weight, style

### 4. Orders App (`apps/orders/models.py`)

#### Order
- Customer orders
- Status: Pending, Processing, Hold, Printing, Shipped, Delivered, Cancelled, Refunded
- Financials: subtotal, tax_total, shipping_total, discount_total, total_amount
- Payment: payment_method, transaction_id, is_paid, paid_at
- Logistics: shipping_address, billing_address, estimated_delivery_date
- Notes: customer_notes, internal_notes

#### OrderItem
- Items within an order
- Fields: order (FK), product (FK), design (FK), quantity, unit_price, total_price
- **Critical for POD:** 
  - product_name_snapshot, sku_snapshot (frozen at purchase time)
  - frozen_canvas_state (JSON) - source of truth for printing
- Production: print_file_url, render_status

#### PrintJob
- Aggregates OrderItems for batch printing
- Status: Queued, Ripping, Printing, Cutting, Completed, Failed
- Fields: batch_id, items (M2M), printer_name, started_at, completed_at

#### Shipment
- Shipping information
- Fields: order (OneToOne), carrier, tracking_number, label_url, weight_kg

### 5. Zakeke App (`apps/zakeke/models.py`)

#### ZakekeProduct
- Maps local products to Zakeke products
- Fields: product (OneToOne), zakeke_product_id, is_active

---

## 🔌 API Endpoints Structure

### Base URL: `/api/v1/`

### 1. Users API (`/api/v1/`)

#### Public Endpoints
- `POST /users/register/` - User registration

#### Authenticated Endpoints (Basic Auth)
- `GET /users/me/` - Get current user profile
- `PUT/PATCH /users/me/` - Update profile

#### Address Management
- `GET /addresses/` - List user addresses
- `POST /addresses/` - Create address
- `GET /addresses/{id}/` - Get address
- `PUT/PATCH /addresses/{id}/` - Update address
- `DELETE /addresses/{id}/` - Delete address

### 2. Catalog API (`/api/v1/`)

#### Categories
- `GET /categories/` - List all categories
- `GET /categories/{id}/` - Get category details

#### Nested Routes (using drf-nested-routers)
- `GET /categories/{category_id}/subcategories/` - Get subcategories in category
- `GET /categories/{category_id}/subcategories/{subcategory_id}/products/` - Get products in subcategory

#### Subcategories
- `GET /subcategories/` - List all subcategories
- `GET /subcategories/{id}/` - Get subcategory details

#### Products
- `GET /products/` - List products
  - Query params: `?category={slug}`, `?subcategory={slug}`, `?search={term}`
- `GET /products/{id}/` - Get product details
- `GET /products/{id}/reviews/` - Get product reviews (via serializer)

#### Banners
- `GET /banners/` - List active banners
  - Query params: `?placement={hero_primary|hero_secondary|homepage|category}`

### 3. Designs API (`/api/v1/`)

#### My Designs
- `GET /my-designs/` - List user's saved designs
- `POST /my-designs/` - Create design
- `GET /my-designs/{id}/` - Get design
- `PUT/PATCH /my-designs/{id}/` - Update design
- `DELETE /my-designs/{id}/` - Delete design

#### Assets
- `GET /assets/` - List user's assets
- `POST /assets/` - Upload asset (multipart/form-data)
- `GET /assets/{id}/` - Get asset
- `PUT/PATCH /assets/{id}/` - Update asset
- `DELETE /assets/{id}/` - Delete asset

#### Templates
- `GET /templates/` - List templates (public)
  - Query params: `?search={term}`
- `GET /templates/{id}/` - Get template details

#### Fonts
- `GET /fonts/` - List available fonts (public)

### 4. Orders API (`/api/v1/`)

#### Orders
- `GET /orders/` - List user's orders
  - Query params: `?ordering={created_at|-created_at|total_amount}`
- `POST /orders/` - Create order (checkout)
  - Request body includes nested `items[]` array
- `GET /orders/{id}/` - Get order details
- `PUT/PATCH /orders/{id}/` - Update order (limited fields)

### 5. Zakeke Integration API (`/api/v1/zakeke/`)

#### Public Endpoints
- `GET /zakeke/token/` - Get Zakeke access token (Server Side)
- `GET /zakeke/test_auth/` - Test Zakeke authentication

#### Authenticated (Zakeke Basic Auth: CLIENT_ID:SECRET_KEY)
- `GET /zakeke/catalog/` - Zakeke calls this to get product catalog
  - Query params: `?search={term}&page={number}`
- `GET /zakeke/{product_id}/options/` - Get product options for Zakeke
- `POST /zakeke/{product_id}/customizer/` - Enable customization for product
- `DELETE /zakeke/{product_id}/customizer/` - Disable customization
- `GET /zakeke/designs/{design_id}/` - Get design details from Zakeke
- `POST /zakeke/order/` - Register order in Zakeke to generate print files

### 6. Admin API (`/api/v1/admin/`)

**Authentication:** Basic Auth (must be staff/superuser)

#### Users Management
- `GET /admin/users/` - List all users
  - Query params: `?search={term}&ordering={field}`
- `GET /admin/users/{id}/` - Get user
- `PUT/PATCH /admin/users/{id}/` - Update user
- `DELETE /admin/users/{id}/` - Delete user
- `POST /admin/users/{id}/activate/` - Activate user
- `POST /admin/users/{id}/deactivate/` - Deactivate user
- `GET /admin/users/stats/` - Get user statistics

#### Catalog Management
- **Categories:**
  - `GET /admin/categories/` - List categories
  - `POST /admin/categories/` - Create category
  - `GET /admin/categories/{id}/` - Get category
  - `PUT/PATCH /admin/categories/{id}/` - Update category
  - `DELETE /admin/categories/{id}/` - Delete category
  - `GET /admin/categories/stats/` - Get category statistics

- **Subcategories:**
  - `GET /admin/subcategories/` - List subcategories
  - `POST /admin/subcategories/` - Create subcategory
  - `GET /admin/subcategories/{id}/` - Get subcategory
  - `PUT/PATCH /admin/subcategories/{id}/` - Update subcategory
  - `DELETE /admin/subcategories/{id}/` - Delete subcategory

- **Products:**
  - `GET /admin/products/` - List products
  - `POST /admin/products/` - Create product
  - `GET /admin/products/{id}/` - Get product
  - `PUT /admin/products/{id}/` - Update product
  - `DELETE /admin/products/{id}/` - Delete product
  - `POST /admin/products/bulk_update_stock/` - Bulk update stock
  - `GET /admin/products/stats/` - Get product statistics

- **Product Images:**
  - `GET /admin/product-images/` - List images
    - Query params: `?product={id}`
  - `POST /admin/product-images/` - Create image
  - `PUT/PATCH /admin/product-images/{id}/` - Update image
  - `DELETE /admin/product-images/{id}/` - Delete image

- **Product Reviews:**
  - `GET /admin/product-reviews/` - List reviews
    - Query params: `?product={id}&search={term}&ordering={field}`
  - `POST /admin/product-reviews/` - Create review
  - `GET /admin/product-reviews/{id}/` - Get review
  - `PUT/PATCH /admin/product-reviews/{id}/` - Update review
  - `DELETE /admin/product-reviews/{id}/` - Delete review
  - `POST /admin/product-reviews/{id}/mark_helpful/` - Mark review as helpful

---

## 🔐 Authentication & Permissions

### Authentication Methods

1. **Basic Authentication** (Primary)
   - Username/Password via HTTP Basic Auth
   - Header: `Authorization: Basic <base64(username:password)>`
   - Used for: User API, Orders, Designs

2. **Session Authentication** (Django default)
   - Used for: Django Admin interface

3. **Zakeke Basic Auth** (Custom)
   - CLIENT_ID:SECRET_KEY via HTTP Basic Auth
   - Used for: Zakeke integration endpoints

### Permission Classes

- `IsAuthenticated` - User must be logged in
- `IsAuthenticatedOrReadOnly` - Auth required for write, read allowed for all
- `IsOwner` - User can only access their own resources
- `IsAdminOrStaff` - Admin/staff only (for admin endpoints)
- `AllowAny` - No authentication required

### CORS Configuration

**Allowed Origins:**
- `http://localhost:5173` (Customer frontend)
- `http://localhost:5174` (Admin frontend)
- `http://127.0.0.1:5173`
- `http://127.0.0.1:5174`
- Configurable via `CORS_ALLOWED_ORIGINS` in `.env`

**Credentials:** Enabled (`CORS_ALLOW_CREDENTIALS = True`)

---

## 🌐 Environment Variables

### Backend `.env` file structure:

```env
# Security
SECRET_KEY="your-secret-key-here"
DEBUG=True
ALLOWED_HOSTS=*

# Database
DB_NAME=vistaprint_db
DB_USER=postgres
DB_PASSWORD=root
DB_HOST=localhost
DB_PORT=5432

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://localhost:5174,http://127.0.0.1:5173,http://127.0.0.1:5174

# Zakeke Integration
ZAKEKE_CLIENT_ID=294600
ZAKEKE_SECRET_KEY=your-secret-key-here
```

---

## 🎨 Frontend Structure

### Customer Frontend (`frontend_/`)

**Pages:**
- `Homepage.jsx` - Landing page with banners, categories
- `Product.jsx` - Product detail page
- `Categories.jsx` - Category/subcategory browsing
- `Cart.jsx` - Shopping cart
- `Editor.jsx` / `ZakekeEditor.jsx` - Product design tool integration

**Services:**
- `apiConfig.js` - Axios instance with interceptors
- `catalogService.js` - Catalog API calls
- `userService.js` - User/auth API calls
- `zakekeService.js` - Zakeke integration

**Context:**
- `ShopContext.jsx` - Global shop state (cart, user, etc.)

### Admin Frontend (`admin/`)

**Pages:**
- User management
- Product/category management
- Order management
- Dashboard with statistics

**Services:**
- `api.js` - Admin API service layer
  - `adminUserAPI` - User management
  - `adminCatalogAPI` - Catalog management
  - `authAPI` - Admin authentication

---

## 🔗 Zakeke Integration

### Purpose
Zakeke is a third-party product customization tool integrated for print-on-demand products.

### Integration Flow

1. **Product Setup:**
   - Admin links local product to Zakeke product via `zakeke_product_id`
   - Endpoint: `POST /api/v1/zakeke/{product_id}/customizer/`

2. **Catalog Sync:**
   - Zakeke calls `GET /api/v1/zakeke/catalog/` to get product catalog
   - Returns: `code` (product ID), `name`, `thumbnail`

3. **Design Creation:**
   - User designs product in Zakeke editor (frontend)
   - Design stored in Zakeke cloud

4. **Order Registration:**
   - On checkout, order registered in Zakeke via `POST /api/v1/zakeke/order/`
   - Zakeke generates print files
   - Print files stored in `OrderItem.print_file_url`

5. **Design Retrieval:**
   - Get design details: `GET /api/v1/zakeke/designs/{design_id}/`
   - Returns full design JSON from Zakeke

### Zakeke Client (`apps/zakeke/client.py`)
- Singleton pattern
- Handles OAuth2 token management
- Supports C2S (Client-to-Server) and S2S (Server-to-Server) tokens
- Auto-refreshes tokens

---

## 🚀 Deployment Configuration

### Docker Compose (`docker-compose.yml`)

**Services:**
1. **db** - PostgreSQL 15 (port 5433)
2. **backend** - Django API (port 8000)
3. **frontend** - Customer frontend (port 5173)
4. **admin** - Admin frontend (port 5174)

### Production (Hostinger VPS)

**Backend:**
- Gunicorn WSGI server
- Process file: `Procfile` → `web: gunicorn shop_project.wsgi`
- Static files served via WhiteNoise
- Environment variables from `.env`

**Database:**
- PostgreSQL on server
- Connection via `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`

**CORS:**
- Must include production frontend URLs in `CORS_ALLOWED_ORIGINS`

---

## 📝 Key Features

1. **User Management**
   - Registration, login, profile management
   - B2B support (company name, tax ID)
   - Address management (billing/shipping)

2. **Catalog System**
   - Hierarchical categories/subcategories
   - Product management with pricing, discounts
   - Product images (S3 URLs)
   - Reviews and ratings
   - Banners for promotions

3. **Design Engine**
   - User-created designs (Fabric.js canvas state)
   - Template system
   - Asset uploads
   - Font library

4. **Order Management**
   - Full order lifecycle
   - Payment tracking
   - Shipping integration
   - Print job batching
   - Order item snapshots (critical for POD)

5. **Zakeke Integration**
   - Product customization
   - Print file generation
   - Design storage and retrieval

6. **Admin Dashboard**
   - User management
   - Catalog management
   - Order management
   - Statistics and analytics

---

## 🔄 API Request/Response Examples

### Register User
```http
POST /api/v1/users/register/
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "SecurePass123",
  "first_name": "John",
  "last_name": "Doe",
  "company_name": "Acme Corp",
  "phone": "+1234567890"
}
```

### Get User Profile
```http
GET /api/v1/users/me/
Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw==
```

### Create Order
```http
POST /api/v1/orders/
Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw==
Content-Type: application/json

{
  "shipping_address": 1,
  "items": [
    {
      "product": 1,
      "design": 1,
      "quantity": 2
    }
  ]
}
```

### Get Product Catalog (Zakeke)
```http
GET /api/v1/zakeke/catalog/?search=tshirt&page=1
Authorization: Basic {CLIENT_ID}:{SECRET_KEY}
```

---

## 📚 Additional Resources

- **API Documentation:** `other/documentation.md`
- **Postman Collection:** `other/postman/vistaprint_api.postman_collection.json`
- **Docker Guide:** `other/DOCKER_GUIDE.md`
- **Deployment Guide:** `other/HOSTINGER_SERVER_CMD.MD`

---

## 🎯 Summary

This is a **full-stack print-on-demand e-commerce platform** with:
- **Django REST Framework** backend
- **React** frontend (customer + admin)
- **PostgreSQL** database
- **Zakeke** integration for product customization
- **Docker** containerization
- **Production-ready** deployment on Hostinger VPS

The system supports the complete customer journey: browsing products, customizing designs, placing orders, and order fulfillment with print file generation.
