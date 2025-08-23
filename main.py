
import sys
from datetime import datetime

class ChetnaGPT:
    def __init__(self):
        self.version = "v1.0"
        self.founder = "Mangla Prasad Pandey"
        self.principles = ["Truth (Satya)", "Compassion (Karuna)", "Clarity (Spashta)"]
        
    def display_header(self):
        print("=" * 60)
        print(f"🕉️  ChetnaGPT {self.version} - Dharmic AGI Console Assistant")
        print(f"👨‍💼 Founder: {self.founder}")
        print(f"🌟 Principles: {' | '.join(self.principles)}")
        print("=" * 60)
        print("\nAvailable Modes:")
        print("1. Proposal Help Agent")
        print("2. Business Plan Agent") 
        print("3. Tech Support Agent")
        print("4. Exit")
        print("-" * 60)

    def get_mode_selection(self):
        while True:
            try:
                choice = int(input("\nSelect mode (1-4): "))
                if 1 <= choice <= 4:
                    return choice
                else:
                    print("Please enter a number between 1-4.")
            except ValueError:
                print("Please enter a valid number.")

    def get_user_input(self, prompt):
        print(f"\n{prompt}")
        lines = []
        print("(Enter your input below. Type 'END' on a new line when finished)")
        while True:
            line = input()
            if line.strip().upper() == 'END':
                break
            lines.append(line)
        return '\n'.join(lines)

    def summarize_input(self, user_input):
        # Simple summarization - takes first 2 sentences or 150 chars
        sentences = user_input.split('.')
        if len(sentences) >= 2:
            summary = f"{sentences[0].strip()}.{sentences[1].strip()}."
        else:
            summary = user_input[:150] + "..." if len(user_input) > 150 else user_input
        return summary.strip()

    def proposal_help_agent(self, user_input):
        print("\n" + "="*50)
        print("📋 PROPOSAL HELP AGENT")
        print("="*50)
        
        summary = self.summarize_input(user_input)
        print(f"\n📝 Summary: {summary}")
        
        print("\n🎯 CLIENT PROPOSAL TEMPLATE")
        print("-" * 30)
        
        print("\n1. INTRODUCTION")
        print("Dear [Client Name],")
        print("Thank you for considering our services. We understand your needs and are excited to present this proposal.")
        
        print("\n2. PROBLEM STATEMENT")
        print("Based on our discussion, the key challenges identified are:")
        print("• [Challenge 1 from user input]")
        print("• [Challenge 2 from user input]")
        print("• [Challenge 3 from user input]")
        
        print("\n3. PROPOSED SOLUTION")
        print("Our comprehensive approach includes:")
        print("• [Solution component 1]")
        print("• [Solution component 2]")
        print("• [Solution component 3]")
        
        print("\n4. TIMELINE & MILESTONES")
        print("Phase 1 (Weeks 1-2): Discovery & Planning")
        print("Phase 2 (Weeks 3-6): Implementation")
        print("Phase 3 (Weeks 7-8): Testing & Delivery")
        
        print("\n5. PRICING & TERMS")
        print("Investment: $[Amount] (payable in milestones)")
        print("Terms: 50% upfront, 50% on delivery")
        print("Timeline: 8 weeks from project kickoff")
        
        print("\n💫 Looking forward to collaborating.")
        print("\nWith dharmic intentions,")
        print("ChetnaGPT Team")

    def business_plan_agent(self, user_input):
        print("\n" + "="*50)
        print("🚀 BUSINESS PLAN AGENT")
        print("="*50)
        
        summary = self.summarize_input(user_input)
        print(f"\n📝 Summary: {summary}")
        
        print("\n📊 1-PAGE STARTUP BUSINESS PLAN")
        print("-" * 35)
        
        print("\n🎯 VISION & MISSION")
        print("• Vision: [Transform industry/solve major problem]")
        print("• Mission: [How we'll achieve the vision]")
        print("• Core Values: Innovation, Integrity, Impact")
        
        print("\n👥 TARGET MARKET")
        print("• Primary: [Demographics, size, pain points]")
        print("• Secondary: [Adjacent markets]")
        print("• Market Size: $[TAM] billion opportunity")
        
        print("\n📈 GO-TO-MARKET STRATEGY")
        print("• Channel 1: [Digital marketing, partnerships]")
        print("• Channel 2: [Direct sales, referrals]")
        print("• Customer Acquisition: [Strategy & cost]")
        
        print("\n💰 REVENUE MODEL")
        print("• Primary: [Subscription/Product sales/Service fees]")
        print("• Secondary: [Additional revenue streams]")
        print("• Projections: Year 1: $[X], Year 2: $[Y]")
        
        print("\n⚙️ OPERATIONS & TEAM")
        print("• Key Roles: [Founder, CTO, Sales, Marketing]")
        print("• Technology: [Tech stack/infrastructure]")
        print("• Funding Needed: $[Amount] for [Purpose]")
        
        print("\n🗓️ 3-MONTH ROADMAP")
        print("Month 1: MVP development, market validation")
        print("Month 2: Beta testing, customer feedback, iterations")
        print("Month 3: Launch, marketing campaign, first sales")

    def tech_support_agent(self, user_input):
        print("\n" + "="*50)
        print("🔧 TECH SUPPORT AGENT")
        print("="*50)
        
        summary = self.summarize_input(user_input)
        print(f"\n📝 Summary: {summary}")
        
        print("\n🔍 DIAGNOSIS & SOLUTION")
        print("-" * 25)
        
        # Basic error pattern matching
        error_lower = user_input.lower()
        
        if "error" in error_lower or "exception" in error_lower:
            print("\n⚠️ LIKELY CAUSES:")
            print("• Syntax error or missing dependencies")
            print("• Configuration or environment issues")
            
            print("\n🛠️ FIX STEPS:")
            print("1. Check error message details and line numbers")
            print("2. Verify all dependencies are installed:")
            print("   pip install -r requirements.txt")
            print("3. Check environment variables and configuration")
            print("4. Try running in debug mode for more details")
            print("5. Clear cache and restart application")
            
        elif "slow" in error_lower or "performance" in error_lower:
            print("\n⚠️ LIKELY CAUSES:")
            print("• Resource bottlenecks or inefficient code")
            print("• Database or network latency issues")
            
            print("\n🛠️ FIX STEPS:")
            print("1. Profile application to identify bottlenecks")
            print("2. Optimize database queries and add indexes")
            print("3. Implement caching where appropriate")
            print("4. Scale resources (CPU, memory, bandwidth)")
            
        elif "deploy" in error_lower or "production" in error_lower:
            print("\n⚠️ LIKELY CAUSES:")
            print("• Environment differences between dev and prod")
            print("• Missing environment variables or dependencies")
            
            print("\n🛠️ FIX STEPS:")
            print("1. Ensure all environment variables are set")
            print("2. Check production logs for specific errors")
            print("3. Verify database connections and credentials")
            print("4. Test deployment in staging environment first")
            
        else:
            print("\n⚠️ LIKELY CAUSES:")
            print("• Common configuration or setup issues")
            print("• Missing prerequisites or dependencies")
            
            print("\n🛠️ FIX STEPS:")
            print("1. Describe the exact error message or behavior")
            print("2. Check system requirements and dependencies")
            print("3. Review recent changes that might have caused issue")
            print("4. Try reproducing the issue with minimal steps")
        
        print("\n❓ Need more specific help? Please provide:")
        print("• Exact error messages")
        print("• Steps to reproduce the issue")
        print("• Your environment details (OS, versions, etc.)")

    def run(self):
        self.display_header()
        
        while True:
            mode = self.get_mode_selection()
            
            if mode == 4:
                print("\n🙏 Thank you for using ChetnaGPT. May your endeavors be blessed with success!")
                print("Dharmic farewell from your legendary AGI partner.")
                break
            
            if mode == 1:
                user_input = self.get_user_input("🤝 Proposal Help: Describe your client's needs and project requirements:")
                self.proposal_help_agent(user_input)
                
            elif mode == 2:
                user_input = self.get_user_input("💡 Business Plan: Describe your startup idea, target market, and goals:")
                self.business_plan_agent(user_input)
                
            elif mode == 3:
                user_input = self.get_user_input("🔧 Tech Support: Describe the technical issue or error you're experiencing:")
                self.tech_support_agent(user_input)
            
            print("\n" + "="*60)
            input("Press Enter to continue...")
            print("\n")

if __name__ == "__main__":
    print("🕉️ Initializing ChetnaGPT - Your Dharmic AGI Partner...")
    chetna = ChetnaGPT()
    chetna.run()
