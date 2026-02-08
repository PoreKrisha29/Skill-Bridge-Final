"""
Database Migration Script: SQLite to PostgreSQL

This script helps migrate your SkillBridge application from SQLite to PostgreSQL.

Usage:
    python migrate_to_postgres.py

Before running:
    1. Install PostgreSQL and pgAdmin
    2. Create a new database in pgAdmin (e.g., 'skillbridge')
    3. Update the .env file with your PostgreSQL credentials
    4. Run this script to create tables and optionally migrate data

Author: SkillBridge Team
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def check_postgresql_connection():
    """Check if PostgreSQL connection is properly configured"""
    database_url = os.environ.get('DATABASE_URL')
    
    if not database_url:
        print("❌ ERROR: DATABASE_URL not found in .env file")
        print("\nPlease update your .env file with PostgreSQL connection details:")
        print("DATABASE_URL=postgresql://username:password@localhost:5432/database_name")
        return False
    
    if 'postgresql' not in database_url.lower():
        print("⚠️  WARNING: DATABASE_URL does not appear to be a PostgreSQL connection")
        print(f"Current DATABASE_URL: {database_url}")
        response = input("\nDo you want to continue anyway? (y/n): ")
        if response.lower() != 'y':
            return False
    
    print(f"✓ Found PostgreSQL connection: {database_url.split('@')[1] if '@' in database_url else 'configured'}")
    return True

def test_connection():
    """Test the PostgreSQL connection"""
    try:
        from sqlalchemy import create_engine
        database_url = os.environ.get('DATABASE_URL')
        
        print("\n🔄 Testing PostgreSQL connection...")
        engine = create_engine(database_url)
        connection = engine.connect()
        connection.close()
        print("✓ Successfully connected to PostgreSQL!")
        return True
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")
        print("\nCommon issues:")
        print("1. PostgreSQL service is not running")
        print("2. Wrong username/password in .env file")
        print("3. Database does not exist (create it in pgAdmin first)")
        print("4. Wrong host or port number")
        return False

def create_tables():
    """Create all database tables in PostgreSQL"""
    try:
        print("\n🔄 Creating database tables...")
        from app import create_app
        from models import db
        
        app = create_app('development')
        with app.app_context():
            # Drop all existing tables (be careful!)
            print("⚠️  Dropping existing tables (if any)...")
            db.drop_all()
            
            # Create all tables
            print("🔄 Creating new tables...")
            db.create_all()
            
            # Initialize default data
            from init_db import create_default_admin, seed_categories
            print("🔄 Creating default admin user...")
            create_default_admin(app)
            
            print("🔄 Seeding categories...")
            seed_categories()
            
        print("✓ Database tables created successfully!")
        return True
    except Exception as e:
        print(f"❌ Error creating tables: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def migrate_sqlite_data():
    """Migrate data from SQLite to PostgreSQL (optional)"""
    sqlite_path = os.path.join(os.path.dirname(__file__), 'instance', 'skillbridge.db')
    
    if not os.path.exists(sqlite_path):
        print(f"\n⚠️  SQLite database not found at: {sqlite_path}")
        print("Skipping data migration. Starting with fresh database.")
        return True
    
    print(f"\n📊 Found existing SQLite database: {sqlite_path}")
    response = input("Do you want to migrate data from SQLite to PostgreSQL? (y/n): ")
    
    if response.lower() != 'y':
        print("Skipping data migration.")
        return True
    
    try:
        print("\n🔄 Migrating data from SQLite to PostgreSQL...")
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        from models import User, Service, Category, Order, Review, Community, CommunityMember
        
        # Connect to SQLite
        sqlite_engine = create_engine(f'sqlite:///{sqlite_path}')
        SQLiteSession = sessionmaker(bind=sqlite_engine)
        sqlite_session = SQLiteSession()
        
        # Connect to PostgreSQL
        postgres_url = os.environ.get('DATABASE_URL')
        postgres_engine = create_engine(postgres_url)
        PostgresSession = sessionmaker(bind=postgres_engine)
        postgres_session = PostgresSession()
        
        # Migrate each table
        tables_to_migrate = [
            ('Users', User),
            ('Categories', Category),
            ('Services', Service),
            ('Orders', Order),
            ('Reviews', Review),
            ('Communities', Community),
            ('Community Members', CommunityMember),
        ]
        
        for table_name, model in tables_to_migrate:
            try:
                print(f"  🔄 Migrating {table_name}...")
                records = sqlite_session.query(model).all()
                
                if records:
                    for record in records:
                        # Create a new instance with the same data
                        postgres_session.merge(record)
                    
                    postgres_session.commit()
                    print(f"  ✓ Migrated {len(records)} {table_name}")
                else:
                    print(f"  ⚠️  No {table_name} to migrate")
            except Exception as e:
                print(f"  ⚠️  Error migrating {table_name}: {str(e)}")
                postgres_session.rollback()
        
        sqlite_session.close()
        postgres_session.close()
        
        print("✓ Data migration completed!")
        return True
        
    except Exception as e:
        print(f"❌ Error during data migration: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main migration process"""
    print("="*60)
    print("🚀 SkillBridge: SQLite to PostgreSQL Migration")
    print("="*60)
    
    # Step 1: Check PostgreSQL configuration
    if not check_postgresql_connection():
        sys.exit(1)
    
    # Step 2: Test connection
    if not test_connection():
        sys.exit(1)
    
    # Step 3: Create tables
    if not create_tables():
        sys.exit(1)
    
    # Step 4: Migrate data (optional)
    migrate_sqlite_data()
    
    print("\n" + "="*60)
    print("✅ Migration completed successfully!")
    print("="*60)
    print("\n📝 Next steps:")
    print("1. Verify your .env file has the correct DATABASE_URL")
    print("2. Run your application: python app.py")
    print("3. Login with default admin credentials:")
    print("   Email: admin@skillbridge.com")
    print("   Password: admin123")
    print("\n⚠️  Note: If you migrated data, the admin password from SQLite will be used.")
    print("="*60 + "\n")

if __name__ == '__main__':
    main()
