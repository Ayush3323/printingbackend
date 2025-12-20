# Database Sharing Strategy - Temporary Solution

## ✅ Your Approach is VALID!

Yes, your teammate can clone the project, add data via the admin frontend, and share the SQLite database back. This is a common approach for development/testing.

## Step-by-Step Guide

### For Your Teammate (Data Entry Person)

#### 1. Clone the Project
```bash
git clone <your-repo-url>
cd vistaprint
```

#### 2. Setup Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser
# Username: admin
# Email: admin@vistaprint.com
# Password: (choose a password)

# Start server
python manage.py runserver
```

#### 3. Setup Frontend
```bash
cd ../admin
npm install
npm run dev
```

#### 4. Add Data
- Open: `http://localhost:5173`
- Login with admin credentials
- Add data via the admin dashboard:
  - Categories & Subcategories
  - Products with attributes
  - Print specs
  - Product images (S3 URLs)
  - Discounts

#### 5. Share Database
**Location:** [backend/db.sqlite3](file:///C:/Users/HP/Desktop/vistaprint/backend/db.sqlite3)

**Options:**
- **Email/Drive**: Share the [db.sqlite3](file:///C:/Users/HP/Desktop/vistaprint/backend/db.sqlite3) file (usually < 10MB for initial data)
- **GitHub**: Commit to a private branch
- **Cloud**: Upload to Google Drive/Dropbox

### For You (Receiving the Database)

#### 1. Backup Current Database
```bash
cd backend
copy db.sqlite3 db.sqlite3.backup
```

#### 2. Replace Database
```bash
# Delete old database
del db.sqlite3

# Copy new database from teammate
copy path\to\received\db.sqlite3 db.sqlite3
```

#### 3. Verify Data
```bash
python manage.py runserver
# Check admin dashboard
```

## ⚠️ Important Notes

### 1. **Git Ignore**
Ensure [.gitignore](file:///c:/Users/HP/Desktop/vistaprint/.gitignore) includes:
```
*.sqlite3
*.pyc
__pycache__/
venv/
node_modules/
```

**DO NOT** commit [db.sqlite3](file:///C:/Users/HP/Desktop/vistaprint/backend/db.sqlite3) to main branch unless intentional.

### 2. **Schema Synchronization**
- Both should use **same code version** (same migrations)
- Before sharing data, ensure teammate has run all migrations
- Check migration status:
  ```bash
  python manage.py showmigrations
  ```

### 3. **User Accounts**
- Teammate's superuser won't exist in your database
- You may need to create your own admin after receiving database
- Or ask teammate to create an account for you

### 4. **File Uploads**
- Since using **S3 URLs** (not local uploads), no file sync needed! ✅
- Just ensure S3 URLs are accessible

## Better Alternative (When Ready)

For production or permanent solution:

### Option A: Shared Development Database
- Use **PostgreSQL** on cloud (Heroku, Railway, Supabase)
- Both connect to same database
- Real-time sync

### Option B: Database Fixtures
```bash
# Teammate exports data
python manage.py dumpdata catalog users > data_fixtures.json

# You import data
python manage.py loaddata data_fixtures.json
```

### Option C: Simple Deployment
- Deploy to **Railway** or **Render** (free tier)
- Teammate adds data to live admin
- No file sharing needed

## Troubleshooting

### "Table doesn't exist" Error
```bash
# Ensure migrations are synced
python manage.py migrate
```

### "User already exists" Error
- Different admin users, OK
- Just login with credentials teammate provides

### Database Too Large
- SQLite supports databases up to **140TB**
- For initial data entry, won't be an issue
- If > 100MB, consider PostgreSQL migration

## Example Workflow

```
Day 1: You develop features
↓
Day 2: Push code to GitHub
↓
Day 3: Teammate clones, runs migrations
↓
Day 4-7: Teammate adds data via admin
↓
Day 8: Teammate shares db.sqlite3
↓
Day 9: You replace your db.sqlite3
✅ Done!
```

## Summary
✅ **Totally valid** temporary solution  
✅ **No deployment needed** for data entry  
✅ **S3 images** make it easier (no file sync)  
⚠️ **Same code version** required  
⚠️ **Don't commit database** to git  
