# Vistaprint Clone - API Documentation

**Version:** 1.0  
**Base URL:** `http://127.0.0.1:8000/api/v1`  
**Authentication:** Basic Authentication (Username & Password)

---

## Table of Contents

1. [Module A: Users & Authentication](#module-a-users--authentication)
2. [Module B: Catalog Management](#module-b-catalog-management)
3. [Module C: Design Engine](#module-c-design-engine)
4. [Module D: Orders & Fulfillment](#module-d-orders--fulfillment)

---

## Module A: Users & Authentication

### 1.1 Register User

**Description:** Creates a new user account.

**HTTP Method:** `POST`

**Endpoint:** `/users/register/`

**Authentication:** Not Required

#### CURL Request:

```bash
curl --location 'http://127.0.0.1:8000/api/v1/users/register/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "SecurePass123",
    "first_name": "John",
    "last_name": "Doe",
    "company_name": "Acme Corp",
    "phone": "+1234567890"
}'
```

#### Request:

```json
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

#### Parameter Details:

| Parameter Name | Type           | Mandatory | Size (up to) | Description                          |
|----------------|----------------|-----------|--------------|--------------------------------------|
| username       | Alphanumeric   | M         | 150          | Unique username                      |
| email          | Email          | M         | 254          | Valid email address                  |
| password       | String         | M         | 128          | Strong password (min 8 characters)   |
| first_name     | Alphanumeric   | O         | 150          | User's first name                    |
| last_name      | Alphanumeric   | O         | 150          | User's last name                     |
| company_name   | Alphanumeric   | O         | 255          | Company/Business name                |
| phone          | Alphanumeric   | O         | 20           | Contact phone number                 |

#### Response:

**Success (201 Created):**

```json
{
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "phone": "+1234567890",
    "avatar": null,
    "company_name": "Acme Corp",
    "tax_id": null,
    "role": null,
    "addresses": [],
    "is_verified": false,
    "date_joined": "2025-12-16T06:30:00Z",
    "last_login": null
}
```

**Error (400 Bad Request):**

```json
{
    "username": ["A user with that username already exists."],
    "email": ["Enter a valid email address."]
}
```

---

### 1.2 Get My Profile

**Description:** Retrieves the authenticated user's profile information.

**HTTP Method:** `GET`

**Endpoint:** `/users/me/`

**Authentication:** Required (Basic Auth)

#### CURL Request:

```bash
curl --location 'http://127.0.0.1:8000/api/v1/users/me/' \
--header 'Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw=='
```

#### Request:

No request body.

#### Parameter Details:

No parameters required.

#### Response:

**Success (200 OK):**

```json
{
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "phone": "+1234567890",
    "avatar": null,
    "company_name": "Acme Corp",
    "tax_id": null,
    "role": {
        "id": 1,
        "name": "customer",
        "description": "Regular customer"
    },
    "addresses": [
        {
            "id": 1,
            "type": "shipping",
            "is_default": true,
            "recipient_name": "John Doe",
            "street": "123 Main St",
            "city": "New York",
            "zip_code": "10001",
            "country": "USA"
        }
    ],
    "is_verified": false,
    "date_joined": "2025-12-16T06:30:00Z",
    "last_login": "2025-12-16T07:00:00Z"
}
```

**Error (401 Unauthorized):**

```json
{
    "detail": "Authentication credentials were not provided."
}
```

---

### 1.3 Update My Profile

**Description:** Updates the authenticated user's profile.

**HTTP Method:** `PATCH`

**Endpoint:** `/users/me/`

**Authentication:** Required (Basic Auth)

#### CURL Request:

```bash
curl --location --request PATCH 'http://127.0.0.1:8000/api/v1/users/me/' \
--header 'Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw==' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name": "Jonathan",
    "phone": "+1987654321"
}'
```

#### Request:

```json
{
    "first_name": "Jonathan",
    "phone": "+1987654321"
}
```

#### Parameter Details:

| Parameter Name | Type         | Mandatory | Size (up to) | Description           |
|----------------|--------------|-----------|--------------|-----------------------|
| first_name     | Alphanumeric | O         | 150          | Updated first name    |
| last_name      | Alphanumeric | O         | 150          | Updated last name     |
| phone          | Alphanumeric | O         | 20           | Updated phone number  |
| company_name   | Alphanumeric | O         | 255          | Updated company name  |
| tax_id         | Alphanumeric | O         | 50           | Tax/Business ID       |

#### Response:

**Success (200 OK):**

```json
{
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "first_name": "Jonathan",
    "last_name": "Doe",
    "phone": "+1987654321",
    "avatar": null,
    "company_name": "Acme Corp",
    "tax_id": null,
    "role": {
        "id": 1,
        "name": "customer",
        "description": "Regular customer"
    },
    "addresses": [],
    "is_verified": false,
    "date_joined": "2025-12-16T06:30:00Z",
    "last_login": "2025-12-16T07:00:00Z"
}
```

---

### 1.4 List My Addresses

**Description:** Retrieves all addresses for the authenticated user.

**HTTP Method:** `GET`

**Endpoint:** `/addresses/`

**Authentication:** Required (Basic Auth)

#### CURL Request:

```bash
curl --location 'http://127.0.0.1:8000/api/v1/addresses/' \
--header 'Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw=='
```

#### Request:

No request body.

#### Response:

**Success (200 OK):**

```json
[
    {
        "id": 1,
        "type": "shipping",
        "is_default": true,
        "company_name": null,
        "recipient_name": "John Doe",
        "phone_number": "+1234567890",
        "street": "123 Main St",
        "apartment_suite": "Apt 4B",
        "city": "New York",
        "state": "NY",
        "zip_code": "10001",
        "country": "USA"
    },
    {
        "id": 2,
        "type": "billing",
        "is_default": false,
        "company_name": "Acme Corp",
        "recipient_name": "John Doe",
        "phone_number": "+1234567890",
        "street": "456 Business Ave",
        "apartment_suite": null,
        "city": "New York",
        "state": "NY",
        "zip_code": "10002",
        "country": "USA"
    }
]
```

---

### 1.5 Create Address

**Description:** Creates a new address for the authenticated user.

**HTTP Method:** `POST`

**Endpoint:** `/addresses/`

**Authentication:** Required (Basic Auth)

#### CURL Request:

```bash
curl --location 'http://127.0.0.1:8000/api/v1/addresses/' \
--header 'Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw==' \
--header 'Content-Type: application/json' \
--data-raw '{
    "type": "shipping",
    "recipient_name": "John Doe",
    "street": "123 Main St",
    "city": "New York",
    "state": "NY",
    "zip_code": "10001",
    "country": "USA",
    "phone_number": "+1234567890",
    "is_default": true
}'
```

#### Request:

```json
{
    "type": "shipping",
    "recipient_name": "John Doe",
    "street": "123 Main St",
    "apartment_suite": "Apt 4B",
    "city": "New York",
    "state": "NY",
    "zip_code": "10001",
    "country": "USA",
    "phone_number": "+1234567890",
    "is_default": true
}
```

#### Parameter Details:

| Parameter Name  | Type         | Mandatory | Size (up to) | Description                              |
|-----------------|--------------|-----------|--------------|------------------------------------------|
| type            | Enum         | M         | 20           | Address type (shipping, billing)         |
| recipient_name  | Alphanumeric | M         | 255          | Name of recipient                        |
| street          | Alphanumeric | M         | 255          | Street address                           |
| apartment_suite | Alphanumeric | O         | 100          | Apartment/Suite number                   |
| city            | Alphanumeric | M         | 100          | City name                                |
| state           | Alphanumeric | O         | 100          | State/Province                           |
| zip_code        | Alphanumeric | M         | 20           | Postal/ZIP code                          |
| country         | Alphanumeric | M         | 100          | Country name                             |
| phone_number    | Alphanumeric | O         | 20           | Contact phone                            |
| is_default      | Boolean      | O         | -            | Set as default address (true/false)      |

#### Response:

**Success (201 Created):**

```json
{
    "id": 1,
    "type": "shipping",
    "is_default": true,
    "company_name": null,
    "recipient_name": "John Doe",
    "phone_number": "+1234567890",
    "street": "123 Main St",
    "apartment_suite": "Apt 4B",
    "city": "New York",
    "state": "NY",
    "zip_code": "10001",
    "country": "USA"
}
```

---

### 1.6 Update Address

**Description:** Updates an existing address.

**HTTP Method:** `PATCH`

**Endpoint:** `/addresses/{id}/`

**Authentication:** Required (Basic Auth)

#### CURL Request:

```bash
curl --location --request PATCH 'http://127.0.0.1:8000/api/v1/addresses/1/' \
--header 'Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw==' \
--header 'Content-Type: application/json' \
--data-raw '{
    "street": "789 New Street",
    "is_default": false
}'
```

#### Request:

```json
{
    "street": "789 New Street",
    "is_default": false
}
```

#### Response:

**Success (200 OK):**

```json
{
    "id": 1,
    "type": "shipping",
    "is_default": false,
    "company_name": null,
    "recipient_name": "John Doe",
    "phone_number": "+1234567890",
    "street": "789 New Street",
    "apartment_suite": "Apt 4B",
    "city": "New York",
    "state": "NY",
    "zip_code": "10001",
    "country": "USA"
}
```

---

### 1.7 Delete Address

**Description:** Deletes an address.

**HTTP Method:** `DELETE`

**Endpoint:** `/addresses/{id}/`

**Authentication:** Required (Basic Auth)

#### CURL Request:

```bash
curl --location --request DELETE 'http://127.0.0.1:8000/api/v1/addresses/1/' \
--header 'Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw=='
```

#### Response:

**Success (204 No Content):**

No response body.

---

## Module B: Catalog Management

### 2.1 List All Categories

**Description:** Retrieves all active root categories with their subcategories.

**HTTP Method:** `GET`

**Endpoint:** `/categories/`

**Authentication:** Not Required

#### CURL Request:

```bash
curl --location 'http://127.0.0.1:8000/api/v1/categories/'
```

#### Request:

No request body.

#### Response:

**Success (200 OK):**

```json
[
    {
        "id": 1,
        "name": "Marketing Materials",
        "slug": "marketing-materials",
        "description": "Promotional and marketing products",
        "image": null,
        "subcategories": [
            {
                "id": 1,
                "name": "Business Cards",
                "slug": "business-cards",
                "description": "All types of business cards",
                "image": null,
                "category": 1
            },
            {
                "id": 2,
                "name": "Flyers",
                "slug": "flyers",
                "description": "Promotional flyers",
                "image": null,
                "category": 1
            }
        ]
    },
    {
        "id": 2,
        "name": "Promotional Items",
        "slug": "promotional-items",
        "description": "Branded merchandise",
        "image": null,
        "subcategories": []
    }
]
```

---

### 2.2 Create Category (Root)

**Description:** Creates a new root category.

**HTTP Method:** `POST`

**Endpoint:** `/categories/`

**Authentication:** Required (Basic Auth)

#### CURL Request:

```bash
curl --location 'http://127.0.0.1:8000/api/v1/categories/' \
--header 'Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw==' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Marketing Materials",
    "slug": "marketing-materials",
    "description": "Promotional and marketing products",
    "display_order": 1
}'
```

#### Request:

```json
{
    "name": "Marketing Materials",
    "slug": "marketing-materials",
    "description": "Promotional and marketing products",
    "display_order": 1
}
```

#### Parameter Details:

| Parameter Name | Type         | Mandatory | Size (up to) | Description                     |
|----------------|--------------|-----------|--------------|---------------------------------|
| name           | Alphanumeric | M         | 100          | Category name                   |
| slug           | Alphanumeric | M         | 50           | URL-friendly unique identifier  |
| description    | Text         | O         | 2000         | Category description            |
| display_order  | Integer      | O         | -            | Display order (default: 0)      |

#### Response:

**Success (201 Created):**

```json
{
    "id": 1,
    "name": "Marketing Materials",
    "slug": "marketing-materials",
    "description": "Promotional and marketing products",
    "image": null,
    "subcategories": []
}
```

---

### 2.3 List All Subcategories

**Description:** Retrieves all active subcategories.

**HTTP Method:** `GET`

**Endpoint:** `/subcategories/`

**Authentication:** Not Required

#### CURL Request:

```bash
curl --location 'http://127.0.0.1:8000/api/v1/subcategories/'
```

#### Response:

**Success (200 OK):**

```json
[
    {
        "id": 1,
        "name": "Business Cards",
        "slug": "business-cards",
        "description": "All types of business cards",
        "image": null,
        "category": 1
    },
    {
        "id": 2,
        "name": "Flyers",
        "slug": "flyers",
        "description": "Promotional flyers",
        "image": null,
        "category": 1
    }
]
```

---

### 2.4 Create Subcategory

**Description:** Creates a new subcategory under a parent category.

**HTTP Method:** `POST`

**Endpoint:** `/subcategories/`

**Authentication:** Required (Basic Auth)

#### CURL Request:

```bash
curl --location 'http://127.0.0.1:8000/api/v1/subcategories/' \
--header 'Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw==' \
--header 'Content-Type: application/json' \
--data-raw '{
    "category": 1,
    "name": "Business Cards",
    "slug": "business-cards",
    "description": "All types of business cards",
    "display_order": 1
}'
```

#### Request:

```json
{
    "category": 1,
    "name": "Business Cards",
    "slug": "business-cards",
    "description": "All types of business cards",
    "display_order": 1
}
```

#### Parameter Details:

| Parameter Name | Type         | Mandatory | Size (up to) | Description                     |
|----------------|--------------|-----------|--------------|---------------------------------|
| category       | Integer      | M         | -            | Parent category ID              |
| name           | Alphanumeric | M         | 100          | Subcategory name                |
| slug           | Alphanumeric | M         | 50           | URL-friendly unique identifier  |
| description    | Text         | O         | 2000         | Subcategory description         |
| display_order  | Integer      | O         | -            | Display order (default: 0)      |

#### Response:

**Success (201 Created):**

```json
{
    "id": 1,
    "name": "Business Cards",
    "slug": "business-cards",
    "description": "All types of business cards",
    "image": null,
    "category": 1
}
```

---

### 2.5 List All Products

**Description:** Retrieves all active products.

**HTTP Method:** `GET`

**Endpoint:** `/products/`

**Authentication:** Not Required

**Query Parameters:**
- `subcategory` - Filter by subcategory slug
- `category` - Filter by parent category slug
- `search` - Search in name, SKU, or description

#### CURL Request:

```bash
curl --location 'http://127.0.0.1:8000/api/v1/products/'
```

#### Response:

**Success (200 OK):**

```json
[
    {
        "id": 1,
        "subcategory": 1,
        "subcategory_name": "Business Cards",
        "name": "Premium Business Card",
        "slug": "premium-business-card",
        "sku": "BC-PREM-001",
        "description": "High quality business cards",
        "base_price": "15.00",
        "stock_quantity": 1000,
        "attributes": [
            {
                "id": 1,
                "name": "Paper Type",
                "display_name": "Paper Type",
                "attribute_type": "text",
                "is_required": true,
                "values": [
                    {
                        "id": 1,
                        "value": "Matte",
                        "display_value": "Matte Finish",
                        "price_adjustment": "0.00",
                        "is_default": true,
                        "swatch_color": null,
                        "swatch_image": null
                    },
                    {
                        "id": 2,
                        "value": "Glossy",
                        "display_value": "Glossy Finish",
                        "price_adjustment": "5.00",
                        "is_default": false,
                        "swatch_color": null,
                        "swatch_image": null
                    }
                ]
            }
        ],
        "print_specs": {
            "width_mm": 89.0,
            "height_mm": 51.0,
            "bleed_margin_mm": 3.0,
            "safe_zone_mm": 3.0,
            "format_template_url": "",
            "allowed_file_types": "pdf,jpg,png,svg"
        },
        "meta_title": "Buy Premium Business Cards",
        "meta_description": "Best business cards in town"
    }
]
```

---

### 2.6 Create Product

**Description:** Creates a new product with optional attributes and print specifications.

**HTTP Method:** `POST`

**Endpoint:** `/products/`

**Authentication:** Required (Basic Auth)

#### CURL Request:

```bash
curl --location 'http://127.0.0.1:8000/api/v1/products/' \
--header 'Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw==' \
--header 'Content-Type: application/json' \
--data-raw '{
    "subcategory": 1,
    "name": "Premium Business Card",
    "slug": "premium-business-card",
    "sku": "BC-PREM-001",
    "description": "High quality business cards",
    "base_price": "15.00",
    "stock_quantity": 1000,
    "print_specs": {
        "width_mm": 89,
        "height_mm": 51,
        "bleed_margin_mm": 3
    },
    "attributes": [
        {
            "name": "Paper Type",
            "attribute_type": "text",
            "values": [
                {"value": "Matte", "price_adjustment": "0.00"},
                {"value": "Glossy", "price_adjustment": "5.00"}
            ]
        }
    ]
}'
```

#### Request:

```json
{
    "subcategory": 1,
    "name": "Premium Business Card",
    "slug": "premium-business-card",
    "sku": "BC-PREM-001",
    "description": "High quality business cards",
    "base_price": "15.00",
    "stock_quantity": 1000,
    "print_specs": {
        "width_mm": 89,
        "height_mm": 51,
        "bleed_margin_mm": 3,
        "safe_zone_mm": 3,
        "format_template_url": "",
        "allowed_file_types": "pdf,jpg,png,svg"
    },
    "attributes": [
        {
            "name": "Paper Type",
            "display_name": "Paper Type",
            "attribute_type": "text",
            "is_required": true,
            "values": [
                {
                    "value": "Matte",
                    "display_value": "Matte Finish",
                    "price_adjustment": "0.00",
                    "is_default": true
                },
                {
                    "value": "Glossy",
                    "display_value": "Glossy Finish",
                    "price_adjustment": "5.00",
                    "is_default": false
                }
            ]
        }
    ],
    "meta_title": "Buy Premium Business Cards",
    "meta_description": "Best business cards in town"
}
```

#### Parameter Details:

| Parameter Name | Type         | Mandatory | Size (up to) | Description                          |
|----------------|--------------|-----------|--------------|--------------------------------------|
| subcategory    | Integer      | M         | -            | Subcategory ID                       |
| name           | Alphanumeric | M         | 200          | Product name                         |
| slug           | Alphanumeric | M         | 50           | URL-friendly unique identifier       |
| sku            | Alphanumeric | M         | 50           | Stock Keeping Unit (unique)          |
| description    | Text         | O         | 5000         | Detailed product description         |
| base_price     | Decimal      | M         | 10,2         | Base price (before attributes)       |
| stock_quantity | Integer      | O         | -            | Available stock quantity             |
| print_specs    | Object       | O         | -            | Print specifications (nested)        |
| attributes     | Array        | O         | -            | Product attributes (nested)          |
| meta_title     | Alphanumeric | O         | 255          | SEO title                            |
| meta_description| Text        | O         | 500          | SEO description                      |

**Nested Object - print_specs:**

| Parameter Name       | Type    | Mandatory | Description                    |
|----------------------|---------|-----------|--------------------------------|
| width_mm             | Float   | M         | Product width in millimeters   |
| height_mm            | Float   | M         | Product height in millimeters  |
| bleed_margin_mm      | Float   | O         | Bleed margin (default: 3.0)    |
| safe_zone_mm         | Float   | O         | Safe zone margin (default: 3.0)|
| format_template_url  | URL     | O         | Link to template file          |
| allowed_file_types   | String  | O         | Comma-separated file types     |

**Nested Array - attributes:**

Each attribute object contains:

| Parameter Name | Type    | Mandatory | Description                              |
|----------------|---------|-----------|------------------------------------------|
| name           | String  | M         | Attribute name (e.g., "Paper Type")      |
| display_name   | String  | O         | Display name for frontend                |
| attribute_type | Enum    | O         | Type: text, color, image (default: text) |
| is_required    | Boolean | O         | Is this attribute required (default: true)|
| values         | Array   | O         | Array of value objects                   |

**Nested Array - attributes[].values:**

| Parameter Name   | Type    | Mandatory | Description                        |
|------------------|---------|-----------|------------------------------------|
| value            | String  | M         | Attribute value (e.g., "Matte")    |
| display_value    | String  | O         | Display value for frontend         |
| price_adjustment | Decimal | O         | Price modifier (default: 0.00)     |
| is_default       | Boolean | O         | Is default value (default: false)  |
| swatch_color     | String  | O         | Hex color code for color swatches  |

#### Response:

**Success (201 Created):**

```json
{
    "id": 1,
    "subcategory": 1,
    "subcategory_name": "Business Cards",
    "name": "Premium Business Card",
    "slug": "premium-business-card",
    "sku": "BC-PREM-001",
    "description": "High quality business cards",
    "base_price": "15.00",
    "stock_quantity": 1000,
    "attributes": [
        {
            "id": 1,
            "name": "Paper Type",
            "display_name": "Paper Type",
            "attribute_type": "text",
            "is_required": true,
            "values": [
                {
                    "id": 1,
                    "value": "Matte",
                    "display_value": "Matte Finish",
                    "price_adjustment": "0.00",
                    "is_default": true,
                    "swatch_color": null,
                    "swatch_image": null
                },
                {
                    "id": 2,
                    "value": "Glossy",
                    "display_value": "Glossy Finish",
                    "price_adjustment": "5.00",
                    "is_default": false,
                    "swatch_color": null,
                    "swatch_image": null
                }
            ]
        }
    ],
    "print_specs": {
        "width_mm": 89.0,
        "height_mm": 51.0,
        "bleed_margin_mm": 3.0,
        "safe_zone_mm": 3.0,
        "format_template_url": "",
        "allowed_file_types": "pdf,jpg,png,svg"
    },
    "meta_title": "Buy Premium Business Cards",
    "meta_description": "Best business cards in town"
}
```

---

### 2.7 Get Product Detail

**Description:** Retrieves detailed information about a specific product.

**HTTP Method:** `GET`

**Endpoint:** `/products/{id}/`

**Authentication:** Not Required

#### CURL Request:

```bash
curl --location 'http://127.0.0.1:8000/api/v1/products/1/'
```

#### Response:

**Success (200 OK):**

Same as Create Product response.

**Error (404 Not Found):**

```json
{
    "detail": "Not found."
}
```

---

### 2.8 Update Product

**Description:** Updates an existing product (full or partial update).

**HTTP Method:** `PATCH` or `PUT`

**Endpoint:** `/products/{id}/`

**Authentication:** Required (Basic Auth)

#### CURL Request:

```bash
curl --location --request PATCH 'http://127.0.0.1:8000/api/v1/products/1/' \
--header 'Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw==' \
--header 'Content-Type: application/json' \
--data-raw '{
    "base_price": "20.00",
    "stock_quantity": 800
}'
```

#### Response:

**Success (200 OK):**

Returns updated product object.

---

### 2.9 Delete Product

**Description:** Deletes a product.

**HTTP Method:** `DELETE`

**Endpoint:** `/products/{id}/`

**Authentication:** Required (Basic Auth)

#### CURL Request:

```bash
curl --location --request DELETE 'http://127.0.0.1:8000/api/v1/products/1/' \
--header 'Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw=='
```

#### Response:

**Success (204 No Content):**

No response body.

---

## Module C: Design Engine

### 3.1 List My Designs

**Description:** Retrieves all saved designs for the authenticated user.

**HTTP Method:** `GET`

**Endpoint:** `/my-designs/`

**Authentication:** Required (Basic Auth)

#### CURL Request:

```bash
curl --location 'http://127.0.0.1:8000/api/v1/my-designs/' \
--header 'Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw=='
```

#### Response:

**Success (200 OK):**

```json
[
    {
        "id": 1,
        "user": 1,
        "product": 1,
        "name": "Summer Campaign Flyer",
        "design_json": {
            "version": "1.0",
            "canvas": "...",
            "objects": []
        },
        "preview_image": "/media/previews/design_1.jpg",
        "version": 1,
        "tags": ["summer", "promo"],
        "created_at": "2025-12-16T08:00:00Z",
        "updated_at": "2025-12-16T09:00:00Z"
    }
]
```

---

### 3.2 Create New Design

**Description:** Creates a new saved design.

**HTTP Method:** `POST`

**Endpoint:** `/my-designs/`

**Authentication:** Required (Basic Auth)

#### CURL Request:

```bash
curl --location 'http://127.0.0.1:8000/api/v1/my-designs/' \
--header 'Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw==' \
--header 'Content-Type: application/json' \
--data-raw '{
    "product": 1,
    "name": "Summer Campaign Flyer",
    "design_json": {
        "version": "1.0",
        "canvas": "...",
        "objects": []
    },
    "tags": ["summer", "promo"]
}'
```

#### Request:

```json
{
    "product": 1,
    "name": "Summer Campaign Flyer",
    "design_json": {
        "version": "1.0",
        "canvas": "...",
        "objects": []
    },
    "tags": ["summer", "promo"]
}
```

#### Parameter Details:

| Parameter Name | Type     | Mandatory | Size (up to) | Description                          |
|----------------|----------|-----------|--------------|--------------------------------------|
| product        | Integer  | M         | -            | Product ID this design is for        |
| name           | String   | O         | 255          | Design name (default: "Untitled")    |
| design_json    | JSON     | M         | -            | Canvas state (Fabric.js format)      |
| tags           | Array    | O         | -            | Array of tag strings                 |

#### Response:

**Success (201 Created):**

```json
{
    "id": 1,
    "user": 1,
    "product": 1,
    "name": "Summer Campaign Flyer",
    "design_json": {
        "version": "1.0",
        "canvas": "...",
        "objects": []
    },
    "preview_image": null,
    "version": 1,
    "tags": ["summer", "promo"],
    "created_at": "2025-12-16T08:00:00Z",
    "updated_at": "2025-12-16T08:00:00Z"
}
```

---

### 3.3 Update Design

**Description:** Updates an existing saved design.

**HTTP Method:** `PATCH`

**Endpoint:** `/my-designs/{id}/`

**Authentication:** Required (Basic Auth)

#### CURL Request:

```bash
curl --location --request PATCH 'http://127.0.0.1:8000/api/v1/my-designs/1/' \
--header 'Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw==' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Updated Summer Campaign",
    "design_json": {
        "version": "1.0",
        "canvas": "...",
        "objects": []
    }
}'
```

#### Response:

**Success (200 OK):**

Returns updated design object.

---

### 3.4 Delete Design

**Description:** Deletes a saved design.

**HTTP Method:** `DELETE`

**Endpoint:** `/my-designs/{id}/`

**Authentication:** Required (Basic Auth)

#### CURL Request:

```bash
curl --location --request DELETE 'http://127.0.0.1:8000/api/v1/my-designs/1/' \
--header 'Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw=='
```

#### Response:

**Success (204 No Content):**

No response body.

---

### 3.5 List Templates (Public)

**Description:** Retrieves all public templates.

**HTTP Method:** `GET`

**Endpoint:** `/templates/`

**Authentication:** Not Required

**Query Parameters:**
- `search` - Search in name, subcategory name, or tags

#### CURL Request:

```bash
curl --location 'http://127.0.0.1:8000/api/v1/templates/'
```

#### Response:

**Success (200 OK):**

```json
[
    {
        "id": 1,
        "product": 1,
        "name": "Modern Business Card Template",
        "description": "Clean and modern business card design",
        "design_json": {
            "version": "1.0",
            "canvas": "...",
            "objects": []
        },
        "subcategory": 1,
        "subcategory_name": "Business Cards",
        "tags": ["business", "modern"],
        "preview_image": "/media/templates/template_1.jpg"
    }
]
```

---

### 3.6 Create Template

**Description:** Creates a new public template.

**HTTP Method:** `POST`

**Endpoint:** `/templates/`

**Authentication:** Required (Basic Auth)

#### CURL Request:

```bash
curl --location 'http://127.0.0.1:8000/api/v1/templates/' \
--header 'Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw==' \
--header 'Content-Type: application/json' \
--data-raw '{
    "product": 1,
    "name": "Modern Business Card Template",
    "description": "Clean and modern business card design",
    "subcategory": 1,
    "design_json": {
        "version": "1.0",
        "canvas": "...",
        "objects": []
    },
    "tags": ["business", "modern"]
}'
```

#### Request:

```json
{
    "product": 1,
    "name": "Modern Business Card Template",
    "description": "Clean and modern business card design",
    "subcategory": 1,
    "design_json": {
        "version": "1.0",
        "canvas": "...",
        "objects": []
    },
    "tags": ["business", "modern"]
}
```

#### Parameter Details:

| Parameter Name | Type    | Mandatory | Size (up to) | Description                       |
|----------------|---------|-----------|--------------|-----------------------------------|
| product        | Integer | M         | -            | Product ID this template is for   |
| name           | String  | M         | 100          | Template name                     |
| description    | Text    | O         | 2000         | Template description              |
| subcategory    | Integer | O         | -            | Subcategory ID for organization   |
| design_json    | JSON    | M         | -            | Canvas state (Fabric.js format)   |
| tags           | Array   | O         | -            | Array of tag strings              |

#### Response:

**Success (201 Created):**

```json
{
    "id": 1,
    "product": 1,
    "name": "Modern Business Card Template",
    "description": "Clean and modern business card design",
    "design_json": {
        "version": "1.0",
        "canvas": "...",
        "objects": []
    },
    "subcategory": 1,
    "subcategory_name": "Business Cards",
    "tags": ["business", "modern"],
    "preview_image": null
}
```

---

### 3.7 Upload Asset (Image/Logo)

**Description:** Uploads a design asset (image, logo, vector).

**HTTP Method:** `POST`

**Endpoint:** `/assets/`

**Authentication:** Required (Basic Auth)

**Content-Type:** `multipart/form-data`

#### CURL Request:

```bash
curl --location 'http://127.0.0.1:8000/api/v1/assets/' \
--header 'Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw==' \
--form 'file=@"/path/to/logo.png"' \
--form 'type="logo"'
```

#### Request (Form Data):

| Parameter Name | Type   | Mandatory | Description                           |
|----------------|--------|-----------|---------------------------------------|
| file           | File   | M         | Binary file (PNG, JPG, SVG, etc.)     |
| type           | String | M         | Asset type (logo, image, vector)      |

#### Response:

**Success (201 Created):**

```json
{
    "id": 1,
    "user": 1,
    "file": "/media/assets/logo_abc123.png",
    "type": "logo",
    "original_filename": "logo.png",
    "size_bytes": 45678,
    "mime_type": "image/png",
    "resolution_dpi": 300,
    "created_at": "2025-12-16T10:00:00Z"
}
```

---

### 3.8 List My Assets

**Description:** Retrieves all uploaded assets for the authenticated user.

**HTTP Method:** `GET`

**Endpoint:** `/assets/`

**Authentication:** Required (Basic Auth)

#### CURL Request:

```bash
curl --location 'http://127.0.0.1:8000/api/v1/assets/' \
--header 'Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw=='
```

#### Response:

**Success (200 OK):**

```json
[
    {
        "id": 1,
        "user": 1,
        "file": "/media/assets/logo_abc123.png",
        "type": "logo",
        "original_filename": "logo.png",
        "size_bytes": 45678,
        "mime_type": "image/png",
        "resolution_dpi": 300,
        "created_at": "2025-12-16T10:00:00Z"
    }
]
```

---

### 3.9 List Fonts (Public)

**Description:** Retrieves all available fonts.

**HTTP Method:** `GET`

**Endpoint:** `/fonts/`

**Authentication:** Not Required

#### CURL Request:

```bash
curl --location 'http://127.0.0.1:8000/api/v1/fonts/'
```

#### Response:

**Success (200 OK):**

```json
[
    {
        "id": 1,
        "name": "Roboto Regular",
        "family": "Roboto",
        "file": "/media/fonts/roboto-regular.ttf",
        "weight": "400",
        "style": "normal"
    },
    {
        "id": 2,
        "name": "Roboto Bold",
        "family": "Roboto",
        "file": "/media/fonts/roboto-bold.ttf",
        "weight": "700",
        "style": "normal"
    }
]
```

---

## Module D: Orders & Fulfillment

### 4.1 List My Orders

**Description:** Retrieves all orders for the authenticated user.

**HTTP Method:** `GET`

**Endpoint:** `/orders/`

**Authentication:** Required (Basic Auth)

#### CURL Request:

```bash
curl --location 'http://127.0.0.1:8000/api/v1/orders/' \
--header 'Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw=='
```

#### Response:

**Success (200 OK):**

```json
[
    {
        "id": 1,
        "user": 1,
        "order_number": "ORD-2025-000001",
        "status": "pending",
        "shipping_address": {
            "id": 1,
            "recipient_name": "John Doe",
            "street": "123 Main St",
            "city": "New York",
            "state": "NY",
            "zip_code": "10001",
            "country": "USA"
        },
        "items": [
            {
                "id": 1,
                "product": 1,
                "product_name_snapshot": "Premium Business Card",
                "sku_snapshot": "BC-PREM-001",
                "quantity": 1000,
                "unit_price": "15.00",
                "total_price": "15000.00",
                "design": 1,
                "frozen_canvas_state": {
                    "version": "1.0",
                    "canvas": "..."
                },
                "print_file_url": null,
                "render_status": "pending"
            }
        ],
        "subtotal": "15000.00",
        "shipping_cost": "25.00",
        "tax": "1200.00",
        "total_amount": "16225.00",
        "payment_status": "pending",
        "payment_method": null,
        "created_at": "2025-12-16T11:00:00Z",
        "updated_at": "2025-12-16T11:00:00Z"
    }
]
```

---

### 4.2 Get Order Detail

**Description:** Retrieves detailed information about a specific order.

**HTTP Method:** `GET`

**Endpoint:** `/orders/{id}/`

**Authentication:** Required (Basic Auth)

#### CURL Request:

```bash
curl --location 'http://127.0.0.1:8000/api/v1/orders/1/' \
--header 'Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw=='
```

#### Response:

**Success (200 OK):**

Same as List My Orders response (individual order object).

---

### 4.3 Create Order (Checkout)

**Description:** Creates a new order with one or more items.

**HTTP Method:** `POST`

**Endpoint:** `/orders/`

**Authentication:** Required (Basic Auth)

#### CURL Request:

```bash
curl --location 'http://127.0.0.1:8000/api/v1/orders/' \
--header 'Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw==' \
--header 'Content-Type: application/json' \
--data-raw '{
    "shipping_address": 1,
    "items": [
        {
            "product": 1,
            "quantity": 1000,
            "design": 1
        }
    ]
}'
```

#### Request:

```json
{
    "shipping_address": 1,
    "items": [
        {
            "product": 1,
            "quantity": 1000,
            "design": 1
        },
        {
            "product": 2,
            "quantity": 500,
            "design": 2
        }
    ]
}
```

#### Parameter Details:

| Parameter Name    | Type    | Mandatory | Description                          |
|-------------------|---------|-----------|--------------------------------------|
| shipping_address  | Integer | O         | Shipping address ID                  |
| items             | Array   | M         | Array of order item objects          |

**Nested Array - items:**

| Parameter Name | Type    | Mandatory | Description                            |
|----------------|---------|-----------|----------------------------------------|
| product        | Integer | M         | Product ID                             |
| quantity       | Integer | M         | Order quantity                         |
| design         | Integer | O         | Saved design ID (if applicable)        |

**Note:** The system automatically:
- Calculates `unit_price` from product's `base_price`
- Freezes `design_json` as `frozen_canvas_state`
- Snapshots `product_name` and `sku` for historical record
- Calculates `total_price` (quantity × unit_price)
- Calculates order `subtotal`, `tax`, and `total_amount`

#### Response:

**Success (201 Created):**

```json
{
    "id": 1,
    "user": 1,
    "order_number": "ORD-2025-000001",
    "status": "pending",
    "shipping_address": {
        "id": 1,
        "recipient_name": "John Doe",
        "street": "123 Main St",
        "city": "New York",
        "state": "NY",
        "zip_code": "10001",
        "country": "USA"
    },
    "items": [
        {
            "id": 1,
            "product": 1,
            "product_name_snapshot": "Premium Business Card",
            "sku_snapshot": "BC-PREM-001",
            "quantity": 1000,
            "unit_price": "15.00",
            "total_price": "15000.00",
            "design": 1,
            "frozen_canvas_state": {
                "version": "1.0",
                "canvas": "..."
            },
            "print_file_url": null,
            "render_status": "pending"
        }
    ],
    "subtotal": "15000.00",
    "shipping_cost": "25.00",
    "tax": "1200.00",
    "total_amount": "16225.00",
    "payment_status": "pending",
    "payment_method": null,
    "created_at": "2025-12-16T11:00:00Z",
    "updated_at": "2025-12-16T11:00:00Z"
}
```

**Error (400 Bad Request):**

```json
{
    "items": [
        "This field is required."
    ]
}
```

---

### 4.4 Update Order Status

**Description:** Updates an order's status (admin/staff only).

**HTTP Method:** `PATCH`

**Endpoint:** `/orders/{id}/`

**Authentication:** Required (Basic Auth + Staff Permissions)

#### CURL Request:

```bash
curl --location --request PATCH 'http://127.0.0.1:8000/api/v1/orders/1/' \
--header 'Authorization: Basic YWRtaW46YWRtaW5wYXNz' \
--header 'Content-Type: application/json' \
--data-raw '{
    "status": "processing"
}'
```

#### Request:

```json
{
    "status": "processing"
}
```

#### Parameter Details:

| Parameter Name  | Type | Mandatory | Description                                        |
|-----------------|------|-----------|----------------------------------------------------|
| status          | Enum | O         | Order status: pending, processing, shipped, delivered, cancelled |
| payment_status  | Enum | O         | Payment status: pending, paid, failed, refunded    |

#### Response:

**Success (200 OK):**

Returns updated order object.

---

## Common Error Codes

| HTTP Status | Error Code       | Description                                  |
|-------------|------------------|----------------------------------------------|
| 400         | Bad Request      | Invalid request parameters or body           |
| 401         | Unauthorized     | Authentication credentials not provided      |
| 403         | Forbidden        | User does not have permission                |
| 404         | Not Found        | Resource not found                           |
| 500         | Internal Error   | Server error                                 |

---

## Authentication Guide

### Basic Authentication

All protected endpoints require Basic Authentication.

**Format:** `Authorization: Basic <base64(username:password)>`

**Example:**
```bash
# Username: john_doe
# Password: SecurePass123
# Base64 encoded: am9obl9kb2U6U2VjdXJlUGFzczEyMw==

curl --location 'http://127.0.0.1:8000/api/v1/users/me/' \
--header 'Authorization: Basic am9obl9kb2U6U2VjdXJlUGFzczEyMw=='
```

---

## Testing with Postman

1. **Import Collection:** Import `postman/vistaprint_api.postman_collection.json`
2. **Set Base URL:** Variable `base_url` = `http://127.0.0.1:8000/api/v1`
3. **Configure Auth:** 
   - Go to Collection Settings → Authorization
   - Type: Basic Auth
   - Username: Your registered username
   - Password: Your password
4. **Test Endpoints:** Run requests in order:
   - Register User
   - Get My Profile
   - Create Category → Subcategory → Product
   - Create Design/Template
   - Create Order

---

## Appendix: Data Flow

### Product Creation Workflow

```
1. Create Category (Root)
   ↓
2. Create Subcategory (Under Category)
   ↓
3. Create Product (Under Subcategory)
   ↓
4. Product includes:
   - Print Specs (dimensions, bleed, safe zone)
   - Attributes (Paper Type, Size, etc.)
   - Attribute Values (Matte, Glossy, etc.)
```

### Order Creation Workflow

```
1. User Registers → Gets User ID
   ↓
2. User Creates Address → Gets Address ID
   ↓
3. User Creates/Selects Design → Gets Design ID
   ↓
4. User Creates Order:
   - References Product ID
   - References Design ID (optional)
   - References Address ID
   ↓
5. System Automatically:
   - Freezes design_json as frozen_canvas_state
   - Snapshots product_name and SKU
   - Calculates unit_price from product.base_price
   - Calculates totals (subtotal, tax, shipping)
   ↓
6. Order Created with Status: "pending"
```

---

**Document End**

*For technical support or API questions, contact the development team.*
