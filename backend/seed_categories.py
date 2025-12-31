from django.db import connection

cursor = connection.cursor()

# Add missing columns to catalog_category table
try:
    # Check which columns exist
    cursor.execute("PRAGMA table_info(catalog_category)")
    existing = [row[1] for row in cursor.fetchall()]
    print(f"Current columns: {existing}")
    
    # Add missing columns one by one
    if 'description' not in existing:
        cursor.execute("ALTER TABLE catalog_category ADD COLUMN description TEXT DEFAULT ''")
        print("✓ Added description column")
    
    if 'image' not in existing:
        cursor.execute("ALTER TABLE catalog_category ADD COLUMN image VARCHAR(100)")
        print("✓ Added image column")
    
    if 'is_active' not in existing:
        cursor.execute("ALTER TABLE catalog_category ADD COLUMN is_active BOOLEAN DEFAULT 1")
        print("✓ Added is_active column")
    
    if 'display_order' not in existing:
        cursor.execute("ALTER TABLE catalog_category ADD COLUMN display_order INTEGER DEFAULT 0")
        print("✓ Added display_order column")
    
    if 'created_at' not in existing:
        cursor.execute("ALTER TABLE catalog_category ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
        print("✓ Added created_at column")
    
    if 'updated_at' not in existing:
        cursor.execute("ALTER TABLE catalog_category ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
        print("✓ Added updated_at column")
        
    print("\n✅ Schema updated successfully!")
    
except Exception as e:
    print(f"❌ Error updating schema: {e}")

# Now create the categories
from apps.catalog.models import Category

try:
    # Create Business Cards category
    cat1, created1 = Category.objects.get_or_create(
        slug='business-cards',
        defaults={
            'name': 'Business Cards',
            'description': 'Professional business cards for all your networking needs',
            'is_active': True,
            'display_order': 1
        }
    )
    status1 = "Created" if created1 else "Already exists"
    print(f"\n{status1}: {cat1.name} (ID: {cat1.id})")
    
    # Create Marketing Materials category
    cat2, created2 = Category.objects.get_or_create(
        slug='marketing-materials',
        defaults={
            'name': 'Marketing Materials',
            'description': 'Promotional and marketing materials to grow your business',
            'is_active': True,
            'display_order': 2
        }
    )
    status2 = "Created" if created2 else "Already exists"
    print(f"{status2}: {cat2.name} (ID: {cat2.id})")
    
    print(f"\n✅ Total categories in database: {Category.objects.count()}")
    
except Exception as e:
    print(f"❌ Error creating categories: {e}")
