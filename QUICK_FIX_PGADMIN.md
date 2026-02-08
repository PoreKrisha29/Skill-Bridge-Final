# 🔧 Quick Fix - Connect pgAdmin to Local PostgreSQL

## Step 1: Close the Error Dialog
Click "Close" on the current error

## Step 2: Register Local PostgreSQL Server

1. In pgAdmin, right-click "Servers" → "Register" → "Server"

2. Fill in these details:

### General Tab:
```
Name: Local - SkillBridge
```

### Connection Tab:
```
Host name/address:  localhost
Port:               5432
Maintenance database: postgres
Username:           postgres
Password:           180975
```
✅ Check "Save password"

### SSL Tab:
```
SSL mode: Prefer
```

3. Click "Save"

## Step 3: Create SkillBridge Database

1. Expand "Local - SkillBridge" server
2. Right-click "Databases" → "Create" → "Database"
3. Name: `skillbridge`
4. Click "Save"

## Step 4: Run Migration

Open terminal in your project folder:
```bash
python migrate_to_postgres.py
```

## Step 5: Start Your App

```bash
python app.py
```

Visit: http://localhost:5000

---

## ✅ Success!

You now have:
- ✅ Local PostgreSQL connected in pgAdmin
- ✅ SkillBridge database created
- ✅ Tables initialized
- ✅ App running locally

---

## 🌐 For Render Deployment Later:

When you deploy to Render:
1. Deploy app first (follow DEPLOYMENT_CHECKLIST.md)
2. Get External Database URL from Render
3. Register as a SECOND server in pgAdmin
4. Use SSL Mode: Require

You can have BOTH local and Render databases in pgAdmin!
