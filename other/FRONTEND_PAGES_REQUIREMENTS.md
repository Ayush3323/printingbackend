# Vistaprint Clone - Complete Frontend Pages Requirements

## 📋 Overview
This document lists **every single page** required to complete the Vistaprint replica website. Pages are categorized by functionality and include status (✅ Created / ❌ Missing).

---

## 🏠 **1. PUBLIC/CUSTOMER PAGES**

### Home & Navigation
| Page | Route | Status | Description |
|------|-------|--------|-------------|
| **Homepage** | `/` | ✅ Created | Main landing page with hero banners, categories, featured products |
| **Search Results** | `/search?q={query}` | ❌ Missing | Search results page with filters |
| **View All Products** | `/view-all` | ✅ Created | Browse all products (same as Categories) |
| **404 Not Found** | Any invalid route | ❌ Missing | Custom 404 error page |

### Product Browsing
| Page | Route | Status | Description |
|------|-------|--------|-------------|
| **Categories Listing** | `/categories` | ✅ Created | Main categories page |
| **Category Detail** | `/categories/:categorySlug` | ✅ Created | Products within a category |
| **Subcategory Detail** | `/categories/:categorySlug/:subcategorySlug` | ❌ Missing | Products within a subcategory |
| **Product Detail** | `/product/:slug` | ✅ Created | Individual product page with specs, reviews |
| **Product Templates** | `/product/:slug/templates` | ✅ Created | Template selection for product |
| **Product Reviews** | `/product/:slug/reviews` | ❌ Missing | Full reviews page with filters |

### Design & Customization
| Page | Route | Status | Description |
|------|-------|--------|-------------|
| **Zakeke Editor** | `/zakeke-editor/:productId` | ✅ Created | Main product customization tool (Zakeke integration) |
| **Template Editor** | `/editor/:templateId` | ✅ Created | Edit a template-based design |
| **My Designs** | `/my-designs` | ❌ Missing | User's saved designs gallery |
| **Design Detail** | `/my-designs/:designId` | ❌ Missing | View/edit individual saved design |
| **Asset Library** | `/my-assets` | ❌ Missing | User's uploaded images/logos |
| **Template Gallery** | `/templates` | ❌ Missing | Browse all available templates |
| **Template Gallery (by Category)** | `/templates/:categorySlug` | ❌ Missing | Templates filtered by category |

### Shopping Cart & Checkout
| Page | Route | Status | Description |
|------|-------|--------|-------------|
| **Shopping Cart** | `/cart` | ✅ Created | Cart review page |
| **Checkout - Step 1: Address** | `/checkout/address` | ❌ Missing | Select/enter shipping address |
| **Checkout - Step 2: Payment** | `/checkout/payment` | ❌ Missing | Payment method selection |
| **Checkout - Step 3: Review** | `/checkout/review` | ❌ Missing | Order review before submission |
| **Checkout - Success** | `/checkout/success/:orderId` | ❌ Missing | Order confirmation page |
| **Checkout - Failed** | `/checkout/failed` | ❌ Missing | Payment failure page |

### User Account (Authenticated)
| Page | Route | Status | Description |
|------|-------|--------|-------------|
| **Login** | `/login` | ❌ Missing | User login page |
| **Register** | `/register` | ❌ Missing | User registration page |
| **Forgot Password** | `/forgot-password` | ❌ Missing | Password reset request |
| **Reset Password** | `/reset-password/:token` | ❌ Missing | Password reset form |
| **My Account Dashboard** | `/account` | ❌ Missing | Account overview dashboard |
| **My Profile** | `/account/profile` | ❌ Missing | Edit profile information |
| **My Addresses** | `/account/addresses` | ❌ Missing | Manage billing/shipping addresses |
| **My Orders** | `/account/orders` | ❌ Missing | Order history list |
| **Order Detail** | `/account/orders/:orderId` | ❌ Missing | Individual order details with tracking |
| **Order Tracking** | `/track-order/:orderId` | ❌ Missing | Public order tracking (with tracking number) |
| **My Designs** | `/account/designs` | ❌ Missing | Saved designs management |
| **My Assets** | `/account/assets` | ❌ Missing | Uploaded assets management |
| **Account Settings** | `/account/settings` | ❌ Missing | Account preferences, notifications |
| **Wishlist/Favorites** | `/account/wishlist` | ❌ Missing | Saved favorite products |
| **Recently Viewed** | `/account/recent` | ❌ Missing | Recently viewed products |

### Help & Support
| Page | Route | Status | Description |
|------|-------|--------|-------------|
| **Contact Us** | `/contact` | ❌ Missing | Contact form and information |
| **Help Center** | `/help` | ❌ Missing | FAQ and help articles |
| **Help - Shipping** | `/help/shipping` | ❌ Missing | Shipping information and policies |
| **Help - Returns** | `/help/returns` | ❌ Missing | Return policy and process |
| **Help - Design Tips** | `/help/design-tips` | ❌ Missing | Design guidelines and tips |
| **Live Chat** | `/support/chat` | ❌ Missing | Live chat support (if integrated) |
| **Bulk Order Inquiry** | `/bulk-orders` | ❌ Missing | Bulk order request form |

### About & Company
| Page | Route | Status | Description |
|------|-------|--------|-------------|
| **About Us** | `/about` | ❌ Missing | Company information and mission |
| **Careers** | `/careers` | ❌ Missing | Job listings and career information |
| **For Investors** | `/investors` | ❌ Missing | Investor relations |
| **For Media** | `/media` | ❌ Missing | Press releases and media kit |
| **Sustainability** | `/sustainability` | ❌ Missing | Environmental and social responsibility |
| **Corporate Social Responsibility** | `/csr` | ❌ Missing | CSR initiatives |

### Legal & Policies
| Page | Route | Status | Description |
|------|-------|--------|-------------|
| **Terms and Conditions** | `/terms` | ❌ Missing | Terms of service |
| **Privacy Policy** | `/privacy` | ❌ Missing | Privacy and cookie policy |
| **Cookie Policy** | `/cookies` | ❌ Missing | Cookie usage details |
| **Copyright** | `/copyright` | ❌ Missing | Copyright information |
| **Patents & Trademarks** | `/patents` | ❌ Missing | Intellectual property information |
| **Accessibility** | `/accessibility` | ❌ Missing | Accessibility statement |

### Promotions & Special Pages
| Page | Route | Status | Description |
|------|-------|--------|-------------|
| **Current Promotions** | `/promotions` | ❌ Missing | Active deals and discounts |
| **Promotion Detail** | `/promotions/:slug` | ❌ Missing | Specific promotion page |
| **New Products** | `/new-products` | ❌ Missing | Recently added products |
| **Best Sellers** | `/best-sellers` | ❌ Missing | Top-selling products |
| **Sale/Clearance** | `/sale` | ❌ Missing | Products on sale |

### Additional Features
| Page | Route | Status | Description |
|------|-------|--------|-------------|
| **Blog/Resources** | `/blog` | ❌ Missing | Blog listing page |
| **Blog Post** | `/blog/:slug` | ❌ Missing | Individual blog article |
| **Compare Products** | `/compare` | ❌ Missing | Side-by-side product comparison |
| **Print Specifications Guide** | `/print-specs` | ❌ Missing | Print specs guide and information |
| **Design Ideas/Inspiration** | `/inspiration` | ❌ Missing | Design inspiration gallery |
| **Size Guide** | `/size-guide` | ❌ Missing | Product sizing information |
| **Color Guide** | `/color-guide` | ❌ Missing | Color options and print colors |

---

## 🔐 **2. ADMIN DASHBOARD PAGES** (Admin Frontend - `/admin` folder)

### Dashboard & Overview
| Page | Route | Status | Description |
|------|-------|--------|-------------|
| **Admin Dashboard** | `/` (index) | ✅ Created | Admin overview with stats, charts, recent orders |
| **Admin Login** | `/login` | ✅ Created | Admin authentication |

### Catalog Management
| Page | Route | Status | Description |
|------|-------|--------|-------------|
| **Categories List** | `/categories` | ✅ Created | Manage categories (CRUD operations) |
| **Category Create/Edit** | Modal in Categories page | ✅ Created | Category form with image upload |
| **Subcategories List** | Included in Categories page | ✅ Created | Manage subcategories (CRUD) |
| **Subcategory Create/Edit** | Modal in Categories page | ✅ Created | Subcategory form |
| **Products List** | `/products` | ✅ Created | Manage products with filters/search |
| **Product Create/Edit** | Modal in Products page | ✅ Created | Product form with Zakeke integration, tabs (basic/attributes/zakeke) |
| **Product Images** | Integrated in Product form | ⚠️ Partial | Product image management (primary image) |
| **Product Reviews** | `/reviews` | ✅ Created | Manage product reviews with filters |
| **Banners** | `/marketing` | ❌ Missing | Manage homepage/hero banners (planned in sidebar) |

### Order Management
| Page | Route | Status | Description |
|------|-------|--------|-------------|
| **Orders List** | `/orders` | ❌ Missing | All orders with filters/status (sidebar link exists) |
| **Order Detail** | `/orders/:id` | ❌ Missing | Order details and management |
| **Print Jobs** | `/orders?tab=print-jobs` | ❌ Missing | Manage print job queue (can be tab in Orders) |
| **Print Job Detail** | `/orders/print-jobs/:id` | ❌ Missing | Print job status and details |
| **Shipments** | `/courier` | ❌ Missing | **ShipMozo Integration** - Shipment tracking management (sidebar link exists) |
| **Courier Management** | `/courier` | ❌ Missing | **ShipMozo API Integration** - Create labels, track shipments, manage carriers |

### User Management
| Page | Route | Status | Description |
|------|-------|--------|-------------|
| **Users List** | `/customers` | ✅ Created | Manage all users with search, filters, activate/deactivate |
| **User Detail** | Modal in Customers page | ✅ Created | User details view (can be enhanced) |
| **User Create/Edit** | Modal in Customers page | ✅ Created | Create/Edit user form (CreateUserModal component) |

### Design & Templates
| Page | Route | Status | Description |
|------|-------|--------|-------------|
| **Templates List** | `/templates` | ❌ Missing | Manage design templates (not in sidebar yet) |
| **Template Create/Edit** | `/templates/new` <br> `/templates/:id/edit` | ❌ Missing | Template editor |
| **Fonts Management** | `/fonts` | ❌ Missing | Upload and manage fonts (not in sidebar yet) |
| **Saved Designs** | `/designs` | ❌ Missing | View user-created designs (not in sidebar yet) |

### Payment & Finance
| Page | Route | Status | Description |
|------|-------|--------|-------------|
| **Payments List** | `/payments` | ❌ Missing | **Razorpay Integration** - Payment transactions, refunds, settlements (sidebar link exists) |
| **Payment Details** | `/payments/:id` | ❌ Missing | **Razorpay Integration** - Individual payment details |
| **Refund Management** | `/payments/refunds` | ❌ Missing | **Razorpay Integration** - Process and manage refunds |
| **Finance Dashboard** | `/finance` | ❌ Missing | Financial reports, revenue analytics (sidebar link exists) |

### Settings & Configuration
| Page | Route | Status | Description |
|------|-------|--------|-------------|
| **Settings** | `/settings` | ❌ Missing | General site settings |
| **Zakeke Configuration** | `/settings/zakeke` | ❌ Missing | Zakeke API configuration (already used in Products page) |
| **Payment Settings** | `/settings/payments` | ❌ Missing | **Razorpay Gateway** configuration (API keys, webhooks) |
| **Shipping Settings** | `/settings/shipping` | ❌ Missing | **ShipMozo API** configuration (carriers, rates, labels) |

### Marketing & Content
| Page | Route | Status | Description |
|------|-------|--------|-------------|
| **Marketing Dashboard** | `/marketing` | ❌ Missing | Promotions, campaigns (sidebar link exists) |
| **Banners Management** | `/marketing/banners` | ❌ Missing | Manage homepage/hero banners |
| **Navbar Images** | `/navbar-images` | ❌ Missing | Manage navigation menu images (sidebar link exists) |

### Inventory Management
| Page | Route | Status | Description |
|------|-------|--------|-------------|
| **Stock Management** | `/stocks` | ❌ Missing | Inventory levels, low stock alerts (sidebar link exists) |
| **Bulk Stock Update** | `/stocks/bulk-update` | ❌ Missing | Bulk stock operations |

### Reports & Analytics
| Page | Route | Status | Description |
|------|-------|--------|-------------|
| **Sales Reports** | `/reports/sales` | ❌ Missing | Sales analytics and reports (charts exist in Dashboard) |
| **Product Reports** | `/reports/products` | ❌ Missing | Product performance analytics |
| **User Reports** | `/reports/users` | ❌ Missing | User analytics and statistics |

---

## 📊 **3. SUMMARY STATISTICS**

### Current Status
- **✅ Created:** 13 pages (7 Customer + 6 Admin)
- **❌ Missing:** 75+ pages
- **Total Required:** ~88 pages

### Pages by Category
| Category | Created | Missing | Total |
|----------|---------|---------|-------|
| Public/Customer Pages | 7 | 50+ | 57+ |
| Admin Dashboard Pages | 6 | 25+ | 31+ |
| **Total** | **13** | **75+** | **88+** |

### Admin Dashboard Status
- **✅ Created:** 6 pages (Login, Dashboard, Reviews, Customers, Products, Categories)
- **❌ Missing:** 25+ pages (Orders, Payments, Marketing, Stocks, Courier, Finance, etc.)

---

## 🎯 **4. PRIORITY RANKING**

### **P0 - Critical (Must Have)**
1. ✅ Homepage
2. ✅ Categories/Product Browsing
3. ✅ Product Detail
4. ✅ Cart
5. ❌ **Login/Register** - URGENT
6. ❌ **Checkout Flow** - URGENT
7. ❌ **Order Confirmation** - URGENT
8. ❌ **My Account Dashboard** - URGENT
9. ❌ **My Orders** - URGENT
10. ✅ Zakeke Editor
11. ❌ **Search Results** - HIGH PRIORITY

### **P1 - High Priority**
1. ❌ Checkout Address/Payment/Review
2. ❌ Order Detail/Tracking
3. ❌ My Designs
4. ❌ My Profile
5. ❌ My Addresses
6. ❌ Contact Us
7. ❌ Help Center/FAQ
8. ❌ Admin Dashboard (all admin pages)

### **P2 - Medium Priority**
1. ❌ Blog/Resources
2. ❌ About Us
3. ❌ Terms/Privacy
4. ❌ Promotions pages
5. ❌ Template Gallery
6. ❌ Wishlist

### **P3 - Low Priority (Nice to Have)**
1. ❌ Careers
2. ❌ Investor relations
3. ❌ Inspiration gallery
4. ❌ Compare products
5. ❌ Size/Color guides

---

## 📝 **5. ROUTE STRUCTURE SUMMARY**

### Customer Routes (Frontend_)
```
/                                    → Homepage
/view-all                            → All Products
/categories                          → Categories Listing
/categories/:categorySlug            → Category Products
/categories/:categorySlug/:subcategorySlug → Subcategory Products
/product/:slug                       → Product Detail
/product/:slug/templates             → Template Selection
/zakeke-editor/:productId            → Zakeke Editor
/editor/:templateId                  → Template Editor
/cart                                → Shopping Cart
/checkout/*                          → Checkout Flow (multi-step)
/login                               → Login
/register                            → Register
/account/*                           → Account Pages
/search                              → Search Results
/contact                             → Contact Us
/help/*                              → Help Center
```

### Admin Routes (Admin - separate frontend app)
```
/login                                 → Admin Login
/                                      → Admin Dashboard (index)
/categories                            → Category Management ✅
/products                              → Product Management ✅
/customers                             → User/Customer Management ✅
/reviews                               → Product Reviews Management ✅
/orders                                → Order Management (Missing - planned)
/payments                              → Payment Management (Missing - Razorpay integration)
/courier                               → Courier/ShipMozo Management (Missing - ShipMozo integration)
/marketing                             → Marketing & Banners (Missing)
/navbar-images                         → Navbar Images (Missing)
/stocks                                → Stock Management (Missing)
/finance                               → Finance Reports (Missing)
/settings/*                            → Settings (Missing)
```

---

## 🔧 **6. TECHNICAL REQUIREMENTS**

### Authentication Required Pages
- All `/account/*` pages
- All `/checkout/*` pages
- `/my-designs`, `/my-assets`
- `/account/*` dashboard pages

### Public Pages
- Homepage, Categories, Products
- Login, Register, Forgot Password
- Help, Contact, Legal pages
- Search Results

### API Integration Points
- User Service: Login, Register, Profile, Addresses
- Catalog Service: Categories, Products, Reviews, Banners
- Order Service: Cart, Checkout, Orders, Tracking
- Design Service: Saved Designs, Assets, Templates
- Zakeke Service: Editor, Design Details, Order Registration

---

## ✅ **7. NEXT STEPS**

1. **Phase 1 - Critical Path:**
   - Create Login/Register pages
   - Build complete Checkout flow (3-4 steps)
   - Create Order Confirmation page
   - Build My Account dashboard
   - Add My Orders page

2. **Phase 2 - User Experience:**
   - Search Results page
   - Order Detail/Tracking page
   - My Designs page
   - Profile/Address management pages
   - Contact/Help pages

3. **Phase 3 - Admin Dashboard:**
   - Admin Login
   - Dashboard with stats
   - Catalog management pages
   - Order management pages
   - User management pages

4. **Phase 4 - Content & Legal:**
   - About, Terms, Privacy pages
   - Blog/Resources
   - Additional support pages

---

## 📌 **Notes**

- Some pages may be combined (e.g., Profile and Settings in one page)
- Consider using modals/drawers for simpler actions (address edit, quick view)
- Multi-step forms (checkout) can be single-page with step indicators
- Admin pages can share common layouts/components
- Implement responsive design for all pages
- Consider lazy loading for better performance
- Add loading states and error handling for all pages

---

## 🔌 **8. INTEGRATION REQUIREMENTS**

### Razorpay Payment Gateway
**Status:** ❌ Not Integrated Yet
**Pages Affected:**
- `/payments` - Payment transactions list
- `/payments/:id` - Payment details
- `/payments/refunds` - Refund management
- `/settings/payments` - Razorpay configuration
- Customer `/checkout/payment` - Payment method selection

**Integration Points:**
- Backend API endpoints for Razorpay webhooks
- Payment intent creation
- Refund processing
- Settlement reports
- Payment status updates

### ShipMozo Order Management API
**Status:** ❌ Not Integrated Yet
**Pages Affected:**
- `/courier` - Courier/shipment management
- `/orders/:id` - Shipment tracking in order detail
- `/settings/shipping` - ShipMozo API configuration
- Customer `/track-order/:orderId` - Order tracking

**Integration Points:**
- Create shipping labels
- Track shipments
- Carrier management
- Shipping rates calculation
- Delivery status updates
- Return label generation

### Zakeke Integration
**Status:** ✅ Already Integrated
**Pages Using:**
- `/products` - Zakeke product ID linking
- Customer `/zakeke-editor/:productId` - Product customization

---

## 📝 **9. ADMIN DASHBOARD FEATURES SUMMARY**

### ✅ Currently Implemented Features
1. **Authentication:** Login with Basic Auth
2. **Dashboard:** Stats cards, charts (Sales, Products, Comparison), Recent Orders
3. **Categories Management:** Full CRUD for categories and subcategories
4. **Products Management:** 
   - Full CRUD operations
   - Zakeke product integration tab
   - Product attributes management
   - Image upload support
5. **Customers Management:** 
   - User list with search/filters
   - Create/Edit users
   - Activate/Deactivate accounts
6. **Reviews Management:** Product reviews listing and management
7. **Data Caching:** Context-based caching system for performance
8. **Protected Routes:** Route protection for admin pages

### ❌ Planned Features (Sidebar Links Exist)
1. **Orders Management** - Full order lifecycle
2. **Payments (Razorpay)** - Payment transactions and refunds
3. **Courier (ShipMozo)** - Shipment management and tracking
4. **Marketing** - Promotions and banners
5. **Stocks** - Inventory management
6. **Finance** - Financial reports and analytics
7. **Navbar Images** - Navigation menu image management

---

**Last Updated:** Based on admin dashboard review and integration requirements
**Status Tracking:** This document should be updated as pages are created and integrations are added
**Next Integration Priority:** 
1. Razorpay Payment Gateway
2. ShipMozo Order Management API
