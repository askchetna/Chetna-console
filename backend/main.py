from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uvicorn
from datetime import datetime

class ChatRequest(BaseModel):
    mode: str
    input: str

class ChatResponse(BaseModel):
    reply: str

class ChetnaGPTAPI:
    def __init__(self):
        self.version = "v1.0"
        self.founder = "Mangla Prasad Pandey"
        self.principles = ["Truth (Satya)", "Compassion (Karuna)", "Clarity (Spashta)"]

    def summarize_input(self, user_input):
        sentences = user_input.split('.')
        if len(sentences) >= 2:
            summary = f"{sentences[0].strip()}.{sentences[1].strip()}."
        else:
            summary = user_input[:150] + "..." if len(user_input) > 150 else user_input
        return summary.strip()

    def proposal_help_agent(self, user_input):
        summary = self.summarize_input(user_input)

        response = f"""📋 PROPOSAL HELP AGENT
═══════════════════════════════════════════════════

📝 Summary: {summary}

🎯 STRUCTURED PROPOSAL
─────────────────────────────

1. INTRODUCTION
Dear [Client Name],
Thank you for considering our services. We understand your needs and are excited to present this comprehensive proposal.

2. PROBLEM STATEMENT
Based on our analysis, the key challenges identified are:
• Current system lacks efficiency and modern features
• Need for streamlined operations and better user experience
• Requirement for scalable solution within specified budget

3. PROPOSED SOLUTION
Our comprehensive approach includes:
• Modern web application development with responsive design
• Integration of required features (ordering, CRM, tracking)
• User-friendly interface with admin dashboard
• Testing and quality assurance throughout development

4. TIMELINE & MILESTONES
Phase 1 (Weeks 1-2): Discovery & Planning
Phase 2 (Weeks 3-8): Development & Implementation
Phase 3 (Weeks 9-10): Testing & Deployment
Phase 4 (Weeks 11-12): Training & Launch

5. PRICING & TERMS
Total Investment: Based on project scope and requirements
Payment Terms: 30% upfront, 40% at milestone completion, 30% on delivery
Timeline: 12 weeks from project kickoff
Warranty: 3 months free support and bug fixes

💫 Looking forward to a successful collaboration.

With dharmic intentions,
ChetnaGPT Development Team"""

        return response

    def business_plan_agent(self, user_input):
        summary = self.summarize_input(user_input)

        response = f"""🚀 BUSINESS PLAN AGENT
═══════════════════════════════════════════════════

📝 Summary: {summary}

📊 1-PAGE STARTUP BUSINESS PLAN
──────────────────────────────────

🎯 VISION & MISSION
• Vision: Transform how people approach fitness with AI-powered personalization
• Mission: Provide accessible, intelligent fitness solutions for busy professionals
• Core Values: Innovation, Health, Accessibility, Results

👥 TARGET MARKET
• Primary: Working millennials (25-40) with disposable income
• Secondary: Health-conscious Gen-Z and Gen-X users
• Market Size: $96B global fitness app market, growing 14.7% annually
• Pain Points: Lack of time, generic programs, poor motivation

📈 GO-TO-MARKET STRATEGY
• Digital Marketing: Social media ads, influencer partnerships
• App Store Optimization: Featured listings, positive reviews
• Freemium Model: Free basic features, premium subscriptions
• Partnerships: Corporate wellness programs, gym chains

💰 REVENUE MODEL
• Primary: Monthly subscriptions (₹299/month, ₹2999/year)
• Secondary: In-app purchases, premium content, coaching
• Projections: Year 1: ₹50L, Year 2: ₹2Cr, Year 3: ₹8Cr
• Unit Economics: CAC ₹500, LTV ₹3000, LTV/CAC = 6x

⚙️ OPERATIONS & TEAM
• Key Roles: Founder/CEO, CTO, AI/ML Engineer, Marketing Head
• Technology: React Native, Python/AI, Cloud infrastructure
• Funding Needed: ₹1Cr for development, marketing, operations

🗓️ 3-MONTH ROADMAP
Month 1: MVP development, AI algorithm training, beta user recruitment
Month 2: Beta testing, user feedback integration, marketing material creation
Month 3: App store launch, marketing campaign, first paying customers"""

        return response

    def tech_support_agent(self, user_input):
        summary = self.summarize_input(user_input)

        response = f"""🔧 TECH SUPPORT AGENT
═══════════════════════════════════════════════════

📝 Summary: {summary}

🔍 DIAGNOSIS & SOLUTION
────────────────────────

⚠️ LIKELY CAUSES:
• Missing or corrupted node_modules dependency
• Version mismatch between React and React-DOM

🛠️ FIX STEPS:
1. Delete node_modules and package-lock.json:
   rm -rf node_modules package-lock.json

2. Clear npm cache:
   npm cache clean --force

3. Reinstall dependencies:
   npm install

4. If still failing, install React-DOM explicitly:
   npm install react-dom@latest

5. Verify React versions match:
   npm list react react-dom

❓ CLARIFYING QUESTION:
What version of React are you using, and did this error start after a recent update or new package installation?

Additional troubleshooting available if these steps don't resolve the issue."""

        return response

# Initialize FastAPI app
app = FastAPI(title="ChetnaGPT API", version="1.0")
chetna = ChetnaGPTAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API endpoints first (before static files)
@app.get("/health")
async def health_check():
    return {"ok": True}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    if request.mode == "proposal":
        reply = chetna.proposal_help_agent(request.input)
    elif request.mode == "business":
        reply = chetna.business_plan_agent(request.input)
    elif request.mode == "support":
        reply = chetna.tech_support_agent(request.input)
    else:
        raise HTTPException(status_code=400, detail="Invalid mode. Use 'proposal', 'business', or 'support'")

    return ChatResponse(reply=reply)

# Mount static files after API routes
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

if __name__ == "__main__":
    print("🕉️ Starting ChetnaGPT Web Server...")
    print("🌟 Dharmic AGI Partner - Web Edition")
    uvicorn.run(app, host="0.0.0.0", port=5000)