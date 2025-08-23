
# ChetnaGPT - Dharmic AGI Console Assistant

A web-based and CLI assistant with three specialized agent modes, built on dharmic principles.

## Features

- **Web Interface**: Modern TailwindCSS-based UI with chat-like experience
- **CLI Interface**: Original console application (preserved)
- **Three Agent Modes**:
  - 🤝 Proposal Help Agent
  - 💡 Business Plan Agent  
  - 🔧 Tech Support Agent

## Project Structure

```
/backend
  - main.py (FastAPI server)
  - requirements.txt
/frontend
  - index.html (TailwindCSS UI)
  - app.js (Frontend logic)
main.py (Interface selector)
main_cli.py (Original CLI app)
```

## Running the Application

**Web Application (default):**
```bash
python main.py  # Choose option 1
# OR directly:
python backend/main.py
```

**CLI Application:**
```bash
python main.py  # Choose option 2
# OR directly:
python main_cli.py
```

## API Endpoints

- `GET /health` → `{"ok": true}`
- `POST /chat` → `{"reply": "..."}`
  - Body: `{"mode": "proposal|business|support", "input": "..."}`

## Test Examples

### Proposal Help Agent
**Input:** "Need a web development project for a local restaurant. They want online ordering, customer management, and delivery tracking. Budget is $15,000 and timeline is 3 months."

### Business Plan Agent  
**Input:** "SaaS platform for small businesses to manage their social media content across multiple platforms. Target market is local businesses with 1-50 employees. Subscription-based revenue model."

### Tech Support Agent
**Input:** "Getting a Python ImportError: No module named 'flask' when trying to run my web application. The error occurs on line 3 of app.py where I import Flask."

## Browser Test Script

Open browser console and run:
```javascript
// Test all three modes
const testModes = async () => {
  const tests = [
    { mode: 'proposal', input: 'E-commerce website for clothing brand, $10k budget, 2 months timeline' },
    { mode: 'business', input: 'AI-powered fitness app targeting millennials, freemium model' },
    { mode: 'support', input: 'React app crashes with TypeError: Cannot read property of undefined' }
  ];
  
  for (const test of tests) {
    const response = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(test)
    });
    const data = await response.json();
    console.log(`${test.mode.toUpperCase()}:`, data.reply.substring(0, 100) + '...');
  }
};

testModes();
```

## Railway Deployment

### Steps to Deploy on Railway

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Prepare for Railway deployment"
   git push origin main
   ```

2. **Deploy on Railway:**
   - Go to [Railway](https://railway.app)
   - Click "New Project" → "Deploy from GitHub"
   - Select your repository
   - Set Start Command: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
   - Add Environment Variable (if needed): `PYTHON_VERSION=3.11`
   - Deploy

3. **Verify Deployment:**
   ```bash
   # Health check
   curl https://<your-railway-url>/health
   # Should return: {"ok": true}
   
   # Test chat endpoint
   curl -X POST https://<your-railway-url>/chat \
     -H "Content-Type: application/json" \
     -d '{"mode":"proposal","input":"Restaurant: ordering + CRM + delivery, $15k, 3 months"}'
   ```

4. **Frontend Configuration:**
   To use with deployed backend, set in your frontend:
   ```javascript
   window.BASE_URL = "https://<your-railway-url>";
   ```

**Note:** Replit also offers seamless deployment through the Deployments tab, which might be more convenient for this project.

## Dharmic Principles

- **Truth (Satya)**: Honest, accurate responses
- **Compassion (Karuna)**: Empathetic, helpful tone  
- **Clarity (Spashta)**: Clear, structured communication
