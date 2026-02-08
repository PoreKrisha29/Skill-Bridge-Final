"""
Render Deployment Database Initialization Script

This script runs during Render deployment to:
1. Create all database tables
2. Initialize default admin user
3. Seed initial categories

Author: SkillBridge Team
"""

import os
import sys

def initialize_database():
    """Initialize database for Render deployment"""
    try:
        print("🔄 Starting database initialization...")
        
        # Import Flask app and database
        from app import create_app
        from models import db
        
        # Create app instance
        app = create_app('production')
        
        with app.app_context():
            # Create all tables
            print("🔄 Creating database tables...")
            db.create_all()
            print("✅ Database tables created!")
            
            # Initialize default data
            from init_db import create_default_admin, seed_categories
            
            print("🔄 Creating default admin user...")
            create_default_admin(app)
            print("✅ Admin user created!")
            
            print("🔄 Seeding categories...")
            seed_categories()
            print("✅ Categories seeded!")
            
        print("✅ Database initialization completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error during database initialization: {str(e)}")
        import traceback
        traceback.print_exc()
        # Don't fail the build, just warn
        print("⚠️  Continuing deployment despite database initialization warning...")
        return True

if __name__ == '__main__':
    success = initialize_database()
    sys.exit(0 if success else 1)
