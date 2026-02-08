# 🎓 SkillBridge - Freelance Marketplace Platform

A modern, full-featured freelance marketplace built with Flask and PostgreSQL.

## 🚀 Quick Start - Deploy to Render (Recommended!)

**The fastest way to get started:**

1. **Read This First:** [`MASTERSTROKE_SUMMARY.md`](MASTERSTROKE_SUMMARY.md) - Complete overview
2. **Follow Checklist:** [`DEPLOYMENT_CHECKLIST.md`](DEPLOYMENT_CHECKLIST.md) - Step-by-step deployment
3. **Connect pgAdmin:** [`PGADMIN_CONNECTION_GUIDE.md`](PGADMIN_CONNECTION_GUIDE.md) - Database management

**Total Time: ~20 minutes** ⏱️

---

## 📚 Documentation

### Deployment Guides
- 🎯 **[MASTERSTROKE_SUMMARY.md](MASTERSTROKE_SUMMARY.md)** - Start here! Complete overview
- ✅ **[DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)** - Interactive deployment checklist
- 🌐 **[RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md)** - Detailed Render deployment guide
- 🔌 **[PGADMIN_CONNECTION_GUIDE.md](PGADMIN_CONNECTION_GUIDE.md)** - Connect pgAdmin to Render

### Alternative Setup
- ⚡ **[QUICK_MIGRATION.md](QUICK_MIGRATION.md)** - Quick local PostgreSQL setup
- 🗄️ **[POSTGRESQL_MIGRATION.md](POSTGRESQL_MIGRATION.md)** - Detailed local PostgreSQL guide

---

## ✨ Features

- 👥 **User Management:** Registration, login, profiles, OAuth
- 🛍️ **Service Marketplace:** Browse, search, filter services
- 💼 **Provider Dashboard:** Manage services, orders, earnings
- 🛒 **Buyer Experience:** Order services, track progress, reviews
- ⭐ **Rating System:** 5-star reviews and feedback
- 💬 **Real-time Chat:** Socket.IO messaging
- 👨‍💼 **Admin Panel:** User management, service moderation
- 🎨 **Responsive Design:** Mobile-friendly interface
- 🔐 **Secure Authentication:** Password hashing, session management

---

## 🛠️ Tech Stack

### Backend
- **Framework:** Flask 3.0.0
- **Database:** PostgreSQL (via Render)
- **ORM:** SQLAlchemy 2.0.23
- **Authentication:** Flask-Login, OAuth (Google)
- **Real-time:** Flask-SocketIO
- **Production Server:** Gunicorn

### Frontend
- **HTML5/CSS3**
- **JavaScript (Vanilla)**
- **Responsive Design**

### Deployment
- **Platform:** Render
- **Database:** Render PostgreSQL
- **SSL:** Automatic HTTPS
- **CI/CD:** Auto-deploy on git push

---

## 📦 Project Structure

```
SkillBridge/
├── 📄 app.py                          # Main Flask application
├── 📄 config.py                       # Configuration settings
├── 📄 models.py                       # Database models
├── 📄 routes.py                       # Application routes
├── 📄 events.py                       # Socket.IO events
├── 📄 extensions.py                   # Flask extensions
├── 📄 email_utils.py                  # Email utilities
├── 📄 init_db.py                      # Database initialization
├── 📄 managers.py                     # Business logic managers
│
├── 🚀 Deployment Files
│   ├── Procfile                       # Render process config
│   ├── build.sh                       # Build script
│   ├── render.yaml                    # Render configuration
│   ├── migrate_render.py              # Database initialization
│   └── requirements.txt               # Python dependencies
│
├── 📚 Documentation
│   ├── MASTERSTROKE_SUMMARY.md        # Complete overview
│   ├── DEPLOYMENT_CHECKLIST.md        # Deployment steps
│   ├── RENDER_DEPLOYMENT.md           # Render guide
│   ├── PGADMIN_CONNECTION_GUIDE.md    # pgAdmin setup
│   ├── QUICK_MIGRATION.md             # Quick local setup
│   └── POSTGRESQL_MIGRATION.md        # Detailed local setup
│
├── 📁 templates/                      # HTML templates
├── 📁 static/                         # CSS, JS, images
└── 📁 instance/                       # Instance-specific files
```

---

## 🎯 Deployment Options

### Option 1: Render (Recommended) 🌟
**Best for:** Production deployment, portfolio projects

- ✅ No local PostgreSQL installation needed
- ✅ Free tier available
- ✅ Automatic SSL/HTTPS
- ✅ Managed database with backups
- ✅ Connect pgAdmin for local management

**Guide:** [`DEPLOYMENT_CHECKLIST.md`](DEPLOYMENT_CHECKLIST.md)

### Option 2: Local Development
**Best for:** Development, testing

- ✅ Quick setup with SQLite
- ✅ Or use local PostgreSQL
- ✅ Full control over environment

**Guide:** [`QUICK_MIGRATION.md`](QUICK_MIGRATION.md)

---

## 🚀 Quick Deploy to Render

```bash
# 1. Push to GitHub
git init
git add .
git commit -m "Deploy to Render"
git remote add origin https://github.com/YOUR_USERNAME/Skill-Bridge-v2.0.git
git push -u origin main

# 2. Go to Render
# Visit: https://render.com
# Click: "New +" → "Blueprint"
# Select your repository
# Click: "Apply"

# 3. Done! Your app is live!
```

**Detailed steps:** [`DEPLOYMENT_CHECKLIST.md`](DEPLOYMENT_CHECKLIST.md)

---

## 💻 Local Development

### Prerequisites
- Python 3.11+
- Git

### Setup
```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/Skill-Bridge-v2.0.git
cd Skill-Bridge-v2.0

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Create .env file (copy from .env.example)
copy .env.example .env  # Windows
# cp .env.example .env  # Mac/Linux

# Run application
python app.py
```

Visit: http://localhost:5000

**Default Admin Login:**
- Email: admin@skillbridge.com
- Password: admin123

---

## 🔐 Environment Variables

Create a `.env` file (see `.env.example`):

```env
# Flask
SECRET_KEY=your-secret-key
FLASK_ENV=development

# Database (Render provides this automatically)
DATABASE_URL=postgresql://user:pass@host:5432/dbname

# Admin
ADMIN_EMAIL=admin@skillbridge.com
ADMIN_PASSWORD=admin123

# OAuth (Optional)
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_client_secret

# Email (Optional)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
```

---

## 📊 Database Management

### Using pgAdmin with Render PostgreSQL

1. **Get credentials from Render dashboard**
2. **Open pgAdmin 4**
3. **Register new server:**
   - Host: [from Render]
   - Port: 5432
   - Database: skillbridge
   - Username: [from Render]
   - Password: [from Render]
   - SSL Mode: Require

**Detailed guide:** [`PGADMIN_CONNECTION_GUIDE.md`](PGADMIN_CONNECTION_GUIDE.md)

---

## 🎓 Learning Resources

This project demonstrates:
- ✅ **OOP Concepts:** Inheritance, Encapsulation, Polymorphism
- ✅ **Design Patterns:** Factory, Singleton, Repository
- ✅ **Database Design:** Relationships, Normalization
- ✅ **Authentication:** Sessions, OAuth, Password hashing
- ✅ **RESTful APIs:** CRUD operations
- ✅ **Real-time Communication:** WebSockets
- ✅ **Cloud Deployment:** CI/CD, Environment variables
- ✅ **Database Management:** PostgreSQL, pgAdmin

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📝 License

This project is licensed under the MIT License.

---

## 🆘 Support

### Documentation
- 📖 **[MASTERSTROKE_SUMMARY.md](MASTERSTROKE_SUMMARY.md)** - Complete overview
- ✅ **[DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)** - Step-by-step guide
- 🔧 **Troubleshooting:** Check individual guide files

### Community
- 💬 **Issues:** Open an issue on GitHub
- 📧 **Email:** support@skillbridge.com

---

## 🎉 Quick Links

| Resource | Description |
|----------|-------------|
| [🎯 Masterstroke Summary](MASTERSTROKE_SUMMARY.md) | Complete deployment overview |
| [✅ Deployment Checklist](DEPLOYMENT_CHECKLIST.md) | Interactive step-by-step guide |
| [🌐 Render Deployment](RENDER_DEPLOYMENT.md) | Detailed Render guide |
| [🔌 pgAdmin Guide](PGADMIN_CONNECTION_GUIDE.md) | Database management setup |
| [⚡ Quick Migration](QUICK_MIGRATION.md) | Fast local setup |
| [🗄️ PostgreSQL Guide](POSTGRESQL_MIGRATION.md) | Detailed local setup |

---

## 🌟 Features Roadmap

- [ ] Payment Integration (Stripe/PayPal)
- [ ] Advanced Search & Filters
- [ ] Service Categories Expansion
- [ ] Mobile App (React Native)
- [ ] AI-powered Service Recommendations
- [ ] Multi-language Support
- [ ] Advanced Analytics Dashboard

---

**Made with ❤️ by the SkillBridge Team**

**Ready to deploy? Start here:** [`MASTERSTROKE_SUMMARY.md`](MASTERSTROKE_SUMMARY.md) 🚀
