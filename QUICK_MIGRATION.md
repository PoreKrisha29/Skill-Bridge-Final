# 🚀 Quick PostgreSQL Migration - SkillBridge

## ⚡ Fast Setup (5 Minutes)

### Step 1: Create Database in pgAdmin
1. Open **pgAdmin 4**
2. Right-click **Databases** → **Create** → **Database**
3. Name: `skillbridge`
4. Click **Save**

### Step 2: Update .env File
Edit the `.env` file (already created for you):
```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/skillbridge
```
Replace `YOUR_PASSWORD` with your PostgreSQL password.

### Step 3: Run Migration
```bash
python migrate_to_postgres.py
```

### Step 4: Start Application
```bash
python app.py
```

### Step 5: Login
- **URL:** http://localhost:5000
- **Email:** admin@skillbridge.com
- **Password:** admin123

---

## ✅ What's Been Done

- ✓ Added `psycopg2-binary` to requirements.txt
- ✓ Updated `config.py` to use PostgreSQL
- ✓ Created `.env` file with PostgreSQL configuration
- ✓ Created migration script (`migrate_to_postgres.py`)
- ✓ Installed PostgreSQL driver

---

## 🔧 Troubleshooting

**Can't connect to PostgreSQL?**
- Make sure PostgreSQL service is running
- Check your password in `.env`
- Verify database exists in pgAdmin

**Need detailed help?**
- See `POSTGRESQL_MIGRATION.md` for full guide

---

## 📊 Database Comparison

| SQLite | PostgreSQL |
|--------|------------|
| File-based | Server-based |
| Single user | Multi-user |
| Good for dev | Production-ready |

---

**That's it! Your app is now using PostgreSQL! 🎉**
