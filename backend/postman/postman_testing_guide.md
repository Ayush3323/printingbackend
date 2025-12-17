# 🎓 Ultimate Beginner's Guide into Postman Testing
### For Vistaprint Clone API

Welcome! This guide is designed for someone who has **never used Postman before**. 

If you just created a user but can't find them, it's likely because **Postman is still "logged in" as the default test user**. This guide will show you exactly how to fix that.

---

## 🛑 The "Missing User" Problem (Read This First)
**Scenario**: You used the "Register User" request to create a new account (e.g., `jane_doe`), but when you run "Get My Profile", it still shows `testuser`.

**The Reason**: 
This API uses **Basic Authentication**. Postman sends a "username" and "password" with *every* request. currently, it is configured to send the default credentials (`testuser` / `password123`) for everything.

**The Fix**: 
After you register a new user, you must **tell Postman to start using that new user's password**.

---

## 🚀 Step-by-Step Testing Flow

### Phase 1: Setup
1.  **Import**: Drag and drop `vistaprint_api.postman_collection.json` into Postman.
2.  **Environment**: You don't need to configure anything yet. The collection uses `http://127.0.0.1:8000/api/v1` by default.

### Phase 2: Registration (Creating your Account)
1.  Expand **Module A: Users** -> **POST Operations**.
2.  Click **Register User**.
3.  Click the **Body** tab (below the URL bar).
4.  Change the JSON data to your desired username/password:
    ```json
    {
        "username": "my_new_user",
        "password": "my_secret_password",
        "email": "me@example.com",
        "company_name": "My Startup"
    }
    ```
5.  Click **Send**.
6.  **Success?** You should see a `201 Created` response at the bottom.

### Phase 3: "Logging In" (Crucial Step!)
Now that `my_new_user` exists, let's switch to them.

1.  **Click on the Collection Name** explicitly:
    *   In the left sidebar, click the top-level folder name: **"Vistaprint Clone API (Structured)"**.
2.  Click the **Authorization** tab (in the main center panel).
3.  You will see "Type: Basic Auth".
4.  **Update the Credentials**:
    *   **Username**: Change `testuser` -> `my_new_user`
    *   **Password**: Change `password123` -> `my_secret_password`
5.  **Click SAVE** (Floppy disk icon or Ctrl+S).
    *   *If you don't save, the changes won't apply!*

### Phase 4: Verifying You Are Logged In
1.  Expand **Module A: Users** -> **GET Operations**.
2.  Click **Get My Profile**.
3.  Click **Send**.
4.  **Check the Response**: 
    *   It should now say `"username": "my_new_user"`.
    *   ✅ success! You are now fully authenticated as your new user.

---

## 📦 Testing the Rest of the App

Now that you are logged in as `my_new_user`, all other requests will use this IDENTITY.

### 1. Create a Shipping Address (Required for Orders)
1.  Go to **Module A** -> **POST Operations** -> **Add Address**.
2.  **Body**:
    ```json
    {
        "type": "shipping",
        "recipient_name": "Me",
        "street": "123 Test St",
        "city": "Test City",
        "state": "NY",
        "zip_code": "10001",
        "country": "USA",
        "phone_number": "555-1234",
        "is_default": true
    }
    ```
3.  Click **Send**. 
4.  **Note the ID**: Look at the response `id`. It will likely be `1` or `2`. You need this number.

### 2. View Products
1.  Go to **Module B** -> **GET Operations** -> **List All Products**.
2.  Click **Send**.
3.  **Note the ID**: Find a product you want to buy (e.g., `id: 1`).

### 3. Place an Order
1.  Go to **Module D** -> **POST Operations** -> **Create Order**.
2.  **Body**: Update the IDs to match what you found in previous steps.
    ```json
    {
        "shipping_address": 1, 
        "items": [
            {
                "product": 1,
                "quantity": 500
            }
        ]
    }
    ```
    *(If your address ID was 2, change `"shipping_address": 2`)*.
3.  Click **Send**.
4.  **Success**: You should see a total price calculated and an Order ID returned.

---

## ❓ Common Errors

| Error Code | Meaning | Solution |
| :--- | :--- | :--- |
| **401 Unauthorized** | "Invalid Username/Password" | Go back to **Phase 3** and double-check your spelling in the Collection Authorization tab. Don't forget to SAVE. |
| **403 Forbidden** | "You don't have permission" | You might be trying to access someone else's order or design. You can only see objects you created. |
| **400 Bad Request** | "Invalid Data" | Check the **Response Body** at the bottom. It will tell you exactly which field is missing or wrong (e.g., "This field is required"). |
| **Connection Refused** | "Server Down" | Make sure your black terminal window running `python manage.py runserver` is still open and running. |
