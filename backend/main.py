
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

🎯 CLIENT PROPOSAL TEMPLATE
─────────────────────────────

1. INTRODUCTION
Dear [Client Name],
Thank you for considering our services. We understand your needs and are excited to present this proposal.

2. PROBLEM STATEMENT
Based on our discussion, the key challenges identified are:
• [Challenge 1 from user input]
• [Challenge 2 from user input]
• [Challenge 3 from user input]

3. PROPOSED SOLUTION
Our comprehensive approach includes:
• [Solution component 1]
• [Solution component 2]
• [Solution component 3]

4. TIMELINE & MILESTONES
Phase 1 (Weeks 1-2): Discovery & Planning
Phase 2 (Weeks 3-6): Implementation
Phase 3 (Weeks 7-8): Testing & Delivery

5. PRICING & TERMS
Investment: $[Amount] (payable in milestones)
Terms: 50% upfront, 50% on delivery
Timeline: 8 weeks from project kickoff

💫 Looking forward to collaborating.

With dharmic intentions,
ChetnaGPT Team"""
        
        return response
    
    def business_plan_agent(self, user_input):
        summary = self.summarize_input(user_input)
        
        response = f"""🚀 BUSINESS PLAN AGENT
═══════════════════════════════════════════════════

📝 Summary: {summary}

📊 1-PAGE STARTUP BUSINESS PLAN
──────────────────────────────────

🎯 VISION & MISSION
• Vision: [Transform industry/solve major problem]
• Mission: [How we'll achieve the vision]
• Core Values: Innovation, Integrity, Impact

👥 TARGET MARKET
• Primary: [Demographics, size, pain points]
• Secondary: [Adjacent markets]
• Market Size: $[TAM] billion opportunity

📈 GO-TO-MARKET STRATEGY
• Channel 1: [Digital marketing, partnerships]
• Channel 2: [Direct sales, referrals]
• Customer Acquisition: [Strategy & cost]

💰 REVENUE MODEL
• Primary: [Subscription/Product sales/Service fees]
• Secondary: [Additional revenue streams]
• Projections: Year 1: $[X], Year 2: $[Y]

⚙️ OPERATIONS & TEAM
• Key Roles: [Founder, CTO, Sales, Marketing]
• Technology: [Tech stack/infrastructure]
• Funding Needed: $[Amount] for [Purpose]

🗓️ 3-MONTH ROADMAP
Month 1: MVP development, market validation
Month 2: Beta testing, customer feedback, iterations
Month 3: Launch, marketing campaign, first sales"""
        
        return response
    
    def tech_support_agent(self, user_input):
        summary = self.summarize_input(user_input)
        error_lower = user_input.lower()
        
        response = f"""🔧 TECH SUPPORT AGENT
═══════════════════════════════════════════════════

📝 Summary: {summary}

🔍 DIAGNOSIS & SOLUTION
────────────────────────"""
        
        if "error" in error_lower or "exception" in error_lower:
            response += """

⚠️ LIKELY CAUSES:
• Syntax error or missing dependencies
• Configuration or environment issues

🛠️ FIX STEPS:
1. Check error message details and line numbers
2. Verify all dependencies are installed:
   pip install -r requirements.txt
3. Check environment variables and configuration
4. Try running in debug mode for more details
5. Clear cache and restart application"""
        
        elif "slow" in error_lower or "performance" in error_lower:
            response += """

⚠️ LIKELY CAUSES:
• Resource bottlenecks or inefficient code
• Database or network latency issues

🛠️ FIX STEPS:
1. Profile application to identify bottlenecks
2. Optimize database queries and add indexes
3. Implement caching where appropriate
4. Scale resources (CPU, memory, bandwidth)"""
        
        elif "deploy" in error_lower or "production" in error_lower:
            response += """

⚠️ LIKELY CAUSES:
• Environment differences between dev and prod
• Missing environment variables or dependencies

🛠️ FIX STEPS:
1. Ensure all environment variables are set
2. Check production logs for specific errors
3. Verify database connections and credentials
4. Test deployment in staging environment first"""
        
        else:
            response += """

⚠️ LIKELY CAUSES:
• Common configuration or setup issues
• Missing prerequisites or dependencies

🛠️ FIX STEPS:
1. Describe the exact error message or behavior
2. Check system requirements and dependencies
3. Review recent changes that might have caused issue
4. Try reproducing the issue with minimal steps"""
        
        response += """

❓ Need more specific help? Please provide:
• Exact error messages
• Steps to reproduce the issue
• Your environment details (OS, versions, etc.)"""
        
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

# Mount static files
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
async def root():
    return FileResponse("frontend/index.html")

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

if __name__ == "__main__":
    print("🕉️ Starting ChetnaGPT Web Server...")
    print("🌟 Dharmic AGI Partner - Web Edition")
    uvicorn.run(app, host="0.0.0.0", port=5000)
