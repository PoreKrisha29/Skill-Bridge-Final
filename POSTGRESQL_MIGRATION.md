# PostgreSQL Migration Guide for SkillBridge

## Quick Setup Steps

### 1. Install PostgreSQL
- Download and install PostgreSQL from: https://www.postgresql.org/download/
- During installation, remember your PostgreSQL password (you'll need it!)
- pgAdmin 4 is included with PostgreSQL installation

### 2. Create Database in pgAdmin
1. Open pgAdmin 4
2. Connect to your PostgreSQL server (localhost)
3. Right-click on "Databases" → "Create" → "Database"
4. Database name: `skillbridge`
5. Click "Save"

### 3. Update .env File
Open the `.env` file and update the DATABASE_URL with your PostgreSQL credentials:

```
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/skillbridge
```

Replace:
- `YOUR_PASSWORD` with your PostgreSQL password
- `skillbridge` with your database name (if different)

### 4. Run Migration Script
```bash
python migrate_to_postgres.py
```

This script will:
- ✓ Test PostgreSQL connection
- ✓ Create all database tables
- ✓ Create default admin user
- ✓ Seed initial categories
- ✓ Optionally migrate data from SQLite (if exists)

### 5. Start Your Application
```bash
python app.py
```

### 6. Login
- URL: http://localhost:5000
- Email: admin@skillbridge.com
- Password: admin123

---

## Troubleshooting

### Connection Error: "could not connect to server"
**Solution:** Make sure PostgreSQL service is running
- Windows: Open Services → Find "postgresql-x64-XX" → Start
- Or restart your computer

### Authentication Error: "password authentication failed"
**Solution:** Check your password in .env file
- The password should match what you set during PostgreSQL installation

### Database Does Not Exist
**Solution:** Create the database in pgAdmin first
- Follow Step 2 above

### Port Already in Use
**Solution:** PostgreSQL default port is 5432
- Check if another service is using this port
- Or change the port in DATABASE_URL

---

## PostgreSQL vs SQLite - What Changed?

| Feature | SQLite | PostgreSQL |
|---------|--------|------------|
| Database Type | File-based | Server-based |
| Concurrent Users | Limited | Excellent |
| Performance | Good for small apps | Excellent for production |
| Data Integrity | Basic | Advanced (ACID compliant) |
| Scalability | Limited | Highly scalable |

---

## Verifying the Migration

### Check Database Connection
```python
python -c "from app import create_app; from models import db; app = create_app(); app.app_context().push(); print('Connected to:', db.engine.url)"
```

### Check Tables Created
Open pgAdmin → skillbridge database → Schemas → public → Tables

You should see:
- user
- service
- category
- order
- review
- community
- community_member
- etc.

---

## Backup Your Data

### Export PostgreSQL Database
```bash
pg_dump -U postgres -d skillbridge > backup.sql
```

### Restore PostgreSQL Database
```bash
psql -U postgres -d skillbridge < backup.sql
```

---

## Need Help?

If you encounter any issues:
1. Check the error message in the terminal
2. Verify PostgreSQL service is running
3. Double-check your .env file credentials
4. Make sure the database exists in pgAdmin

---

**Note:** After successful migration, you can keep the SQLite database as a backup or delete it.
