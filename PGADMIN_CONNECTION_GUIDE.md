# 🔌 Connect pgAdmin to Render PostgreSQL - Visual Guide

## 📋 What You'll Need

From your Render PostgreSQL Dashboard, copy these 5 things:

```
Hostname:  dpg-xxxxxxxxxxxxx-a.oregon-postgres.render.com
Port:      5432
Database:  skillbridge
Username:  skillbridge_user
Password:  [long random string shown in Render]
```

---

## 🎯 Step-by-Step Connection

### Step 1: Open pgAdmin 4
- Launch pgAdmin from your Start Menu
- Wait for it to load in your browser

### Step 2: Register New Server
```
Right-click "Servers" 
  → Click "Register" 
    → Click "Server..."
```

### Step 3: Fill in the Form

#### 📝 General Tab
```
Name: Render - SkillBridge
```
(You can name it anything you want)

#### 🔌 Connection Tab
```
Host name/address:  [Paste Hostname from Render]
Port:               5432
Maintenance database: skillbridge
Username:           [Paste Username from Render]
Password:           [Paste Password from Render]

✅ Check "Save password?" (so you don't have to enter it every time)
```

#### 🔒 SSL Tab
```
SSL mode: Require
```
**IMPORTANT:** This must be "Require" or connection will fail!

### Step 4: Save and Connect
- Click **"Save"** button
- pgAdmin will connect to your Render database
- You'll see "Render - SkillBridge" appear in the server list

---

## ✅ Verify Connection

### Check 1: Expand the Server
```
Render - SkillBridge
  └── Databases (1)
      └── skillbridge
          └── Schemas
              └── public
                  └── Tables (7+)
```

### Check 2: View Tables
You should see these tables:
- `user`
- `service`
- `category`
- `order`
- `review`
- `community`
- `community_member`
- And more...

### Check 3: Run a Test Query
1. Right-click **skillbridge** database
2. Click **"Query Tool"**
3. Paste this query:
```sql
SELECT email, is_admin, created_at 
FROM "user" 
WHERE is_admin = true;
```
4. Click **Execute** (▶️ button)
5. You should see your admin user!

---

## 🎨 Visual Layout

```
┌─────────────────────────────────────────────────────┐
│  pgAdmin 4                                      ─ □ ×│
├─────────────────────────────────────────────────────┤
│ File  Object  Tools  Help                           │
├──────────────┬──────────────────────────────────────┤
│              │                                       │
│ 🖥️ Servers   │  Dashboard                           │
│   └─ 🌐 Render│                                      │
│      SkillBr │  Server: Render - SkillBridge        │
│      idge    │  Database: skillbridge               │
│      └─ 📊 Da│  User: skillbridge_user              │
│         tabas│                                       │
│         es   │  ✅ Connected                         │
│         └─ sk│                                       │
│            il│  Tables: 7                            │
│            lb│  Size: 8.2 MB                         │
│            ri│  Connections: 1                       │
│            dg│                                       │
│            e │                                       │
│            └─│                                       │
│              │                                       │
└──────────────┴──────────────────────────────────────┘
```

---

## 🔍 What You Can Do Now

### 1. View All Users
```sql
SELECT * FROM "user" ORDER BY created_at DESC;
```

### 2. View All Services
```sql
SELECT title, price, provider_id, created_at 
FROM service 
ORDER BY created_at DESC;
```

### 3. Check Orders
```sql
SELECT o.id, u.email, s.title, o.total_amount, o.status
FROM "order" o
JOIN "user" u ON o.buyer_id = u.id
JOIN service s ON o.service_id = s.id
ORDER BY o.created_at DESC;
```

### 4. View Data Visually
- Right-click any table
- Click **"View/Edit Data"** → **"All Rows"**
- See data in spreadsheet format
- Edit directly if needed!

### 5. Export Data
```sql
-- Right-click query results
-- Click "Download as CSV"
```

---

## 🎯 Common Tasks

### Add New Admin User (via pgAdmin)
```sql
-- First, get the hashed password from your app
-- Then insert:
INSERT INTO "user" (email, password, is_admin, created_at)
VALUES ('newadmin@skillbridge.com', 'hashed_password_here', true, NOW());
```

### Check Database Size
```sql
SELECT pg_size_pretty(pg_database_size('skillbridge'));
```

### View Active Connections
```sql
SELECT * FROM pg_stat_activity 
WHERE datname = 'skillbridge';
```

### Backup Database
1. Right-click **skillbridge** database
2. Click **"Backup..."**
3. Choose filename and location
4. Click **"Backup"**

---

## 🆘 Troubleshooting

### ❌ "Could not connect to server"
**Causes:**
- Wrong hostname
- Firewall blocking port 5432
- Render database not running

**Solutions:**
1. Double-check hostname from Render
2. Try External URL (not Internal)
3. Check Render database status
4. Disable VPN temporarily

---

### ❌ "Password authentication failed"
**Causes:**
- Wrong password
- Password copied with extra spaces

**Solutions:**
1. Copy password again from Render
2. Make sure no spaces before/after
3. Try typing it manually

---

### ❌ "SSL connection required"
**Cause:**
- SSL mode not set to "Require"

**Solution:**
1. Edit server connection
2. Go to SSL tab
3. Set SSL mode to **"Require"**
4. Save

---

### ❌ "Database does not exist"
**Cause:**
- Wrong database name
- Database not created yet

**Solution:**
1. Check Render dashboard
2. Verify database name is "skillbridge"
3. Make sure deployment completed

---

## 💡 Pro Tips

### Tip 1: Save Connection
✅ Always check "Save password" to avoid re-entering

### Tip 2: Use External URL
🌐 For pgAdmin, always use the **External Database URL** from Render

### Tip 3: Bookmark Queries
📌 Save frequently used queries:
- Right-click in Query Tool
- Click "Save"
- Name it and save

### Tip 4: Multiple Connections
🔗 You can connect to:
- Render PostgreSQL (production)
- Local PostgreSQL (development)
- Both at the same time!

### Tip 5: Monitor Performance
📊 Use pgAdmin's Dashboard to:
- See active connections
- Monitor query performance
- Check database size

---

## 🎉 You're Connected!

Now you have:
- ✅ Production database on Render
- ✅ Local management via pgAdmin
- ✅ Full SQL access
- ✅ Visual data editing
- ✅ Backup capabilities

**Best of both worlds! 🌟**

---

## 📚 Learn More

### pgAdmin Documentation
- https://www.pgadmin.org/docs/

### PostgreSQL Queries
- https://www.postgresql.org/docs/current/sql.html

### Render PostgreSQL
- https://render.com/docs/databases

---

**Need help? Check the troubleshooting section above! 🚀**
