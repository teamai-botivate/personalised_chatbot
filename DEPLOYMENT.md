# 🚀 Employee Portal - Deployment Guide

## Quick Summary
- **Single Backend Service** (FastAPI) serving both API and Static Frontend
- **No Docker Needed** - Pure Python 3.10
- **Auto-Setup** - Database initializes on first startup
- **Single .env File** - All configuration in one place

---

## 📋 Pre-Deployment Checklist

### Required Files
- ✅ `backend/app/` - Backend source code
- ✅ `backend/static/index.html` - Vanilla JS frontend
- ✅ `backend/requirements.txt` - Python dependencies
- ✅ `.env` - Configuration (create new)

### Required Credentials
- 📄 **Google Service Account JSON** (from Google Cloud)
- 🔑 **OpenAI API Key** (from OpenAI)
- 📊 **Google Sheets ID** (the sheet with employee data)

---

## 🛠️ Local Setup (Testing)

### Step 1: Install Python 3.10
```bash
# Windows
# Download from https://www.python.org/downloads/
# Make sure to check "Add to PATH" during installation

# Verify installation
python --version  # Should show 3.10.x
```

### Step 2: Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### Step 3: Create `.env` File
```bash
# In HR_Support directory, create .env with:
DATABASE_URL=sqlite+aiosqlite:///./botivate_master.db
JWT_SECRET_KEY=your-secret-key-here-minimum-32-chars
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx
OPENAI_MODEL=gpt-4o-mini
APP_NAME=Employee Portal
GOOGLE_SHEET_ID=1SRVhz6oD35pb-wLHOd6TyxSRJcvwvFYeGhlXuScHLHY
GOOGLE_SERVICE_ACCOUNT_JSON={"type":"service_account",...}
```

### Step 4: Run Locally
```bash
cd backend
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Open browser: `http://localhost:8000`

---

## 🌐 Render Deployment (Production)

### Step 1: Create New Web Service on Render
1. Go to https://dashboard.render.com
2. Click "New Web Service"
3. Connect your GitHub repository
4. Select branch: `main`

### Step 2: Configure Service
```
Name: employee-portal
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: cd backend && python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Step 3: Set Environment Variables
In Render dashboard, add:
```
DATABASE_URL=sqlite+aiosqlite:///./botivate_master.db
JWT_SECRET_KEY=use-same-as-local-or-generate-new
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx
OPENAI_MODEL=gpt-4o-mini
APP_NAME=Employee Portal
GOOGLE_SHEET_ID=1SRVhz6oD35pb-wLHOd6TyxSRJcvwvFYeGhlXuScHLHY
GOOGLE_SERVICE_ACCOUNT_JSON={"type":"service_account",...}
SKIP_GOOGLE_AUTH=false
```

### Step 4: Deploy
Click "Create Web Service" and watch deployment logs.

**Your app will be live at:** `https://employee-portal-xxxxx.onrender.com`

---

## ✅ Database Setup (Automatic)

On **first startup** (local or production), the system will:
1. Create tables from SQLAlchemy models
2. Create company record: `company-1`
3. Create database connection pointing to your Google Sheet
4. Print confirmation message

**No manual setup needed!** Just set `.env` variables correctly.

---

## 📱 First Login Test

Once deployed:
1. Open app in browser
2. Enter mobile number from your Google Sheet
3. Login success → See dashboard with chat
4. Ask questions about your data

---

## 🔧 Environment Variables Explained

| Variable | Example | Notes |
|----------|---------|-------|
| `DATABASE_URL` | `sqlite+aiosqlite:///./botivate_master.db` | SQLite for local, works on Render |
| `JWT_SECRET_KEY` | Random 32+ chars | Generate: `python -c "import secrets; print(secrets.token_hex(32))"` |
| `OPENAI_API_KEY` | `sk-proj-...` | From https://platform.openai.com |
| `GOOGLE_SHEET_ID` | `1SRVhz6o...` | From Google Sheet URL: `spreadsheets/d/{ID}/` |
| `GOOGLE_SERVICE_ACCOUNT_JSON` | Full JSON object | From Google Cloud (single-line JSON) |
| `SKIP_GOOGLE_AUTH` | `false` | Keep as `false` for production |

---

## 🐛 Troubleshooting

### "Unable to load PEM file" Error
**Solution:** Verify `GOOGLE_SERVICE_ACCOUNT_JSON` is valid JSON (one line, no line breaks)

### "GOOGLE_SHEET_ID not found"
**Solution:** Set `GOOGLE_SHEET_ID` in `.env` (not in database connection)

### Database not initializing
**Solution:** Check app logs - auto-setup runs on first startup and logs status

### "No active company found"
**Solution:** Auto-setup failed - check `.env` and logs. Restart app once `GOOGLE_SHEET_ID` is set.

---

## 📊 Project Structure
```
HR_Support/
├── backend/
│   ├── app/
│   │   ├── main.py           (FastAPI + auto-setup)
│   │   ├── config.py         (Settings from .env)
│   │   ├── database.py       (SQLAlchemy)
│   │   ├── routers/          (API routes)
│   │   ├── models/           (Database models)
│   │   ├── adapters/         (Google Sheets adapter)
│   │   ├── agents/           (LangGraph agent)
│   │   └── services/         (auto_setup.py)
│   ├── static/
│   │   └── index.html        (Vanilla JS frontend)
│   ├── requirements.txt       (Python packages)
│   └── .env                  (Configuration - LOCALLY ONLY)
└── .env                      (Root level on Render)
```

---

## 🚀 Commands Reference

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run backend
cd backend
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Visit
# http://localhost:8000
```

### Production (Render)
- Push to GitHub `main` branch
- Render auto-deploys
- Check logs at: https://dashboard.render.com/{service-name}/logs

### Generate JWT Secret
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

---

## 📝 First-Time Setup Checklist

- [ ] Clone repo or download files
- [ ] Install Python 3.10
- [ ] Create `.env` with all variables
- [ ] Run `pip install -r requirements.txt`
- [ ] Test locally: `python -m uvicorn app.main:app --port 8000`
- [ ] Open `http://localhost:8000` and login
- [ ] Push to GitHub
- [ ] Create Render Web Service
- [ ] Add `.env` variables to Render
- [ ] Deploy and test production URL

---

## ✨ That's It!

No Docker, no build tools, no complicated setup. Just Python + FastAPI + Vanilla JS.

Questions? Check app logs for detailed error messages.
