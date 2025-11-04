import random
from fuzzywuzzy import fuzz

# --- NEW, COMPREHENSIVE KNOWLEDGE BASE ---
# This is built directly from your 9-section Q&A document.

knowledge_base = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "greeting", "morning", "afternoon"],
        "responses": [
            "Hi there! I'm the FluxAudit bot. How can I help you today?",
            "Hello! I am FluxAudit's AI assistant. What can I do for you?",
            "Hey! Ask me anything about the FluxAudit platform."
        ]
    },
    "goodbye": {
        "keywords": ["bye", "quit", "exit", "goodbye", "see you", "later"],
        "responses": [
            "Goodbye! Have a great day.",
            "See you later! Feel free to ask more questions anytime.",
            "Bye! Take care."
        ]
    },
    "purpose": {
        "keywords": ["what", "is", "fluxaudit", "purpose", "summary", "solution"],
        "responses": [
            "FluxAudit is an AI-powered, web-based platform designed to modernize and automate financial auditing.",
            "It's a solution that provides real-time anomaly detection, automated compliance reporting, and advanced analytics to ensure accuracy and transparency.",
            "The high-level summary is: FluxAudit is an AI platform to automate and modernize financial audits."
        ]
    },
    "problem_solved": {
        "keywords": ["problem", "solve", "why", "manual", "audit"],
        "responses": [
            "FluxAudit addresses the significant operational risks and inefficiencies of traditional, manual financial auditing, which are slow, prone to human error, and can't provide real-time insights.",
            "It solves the problem of manual audits being slow and error-prone, which can lead to financial loss and compliance penalties.",
            "The fundamental business problem is that manual auditing is inefficient and risky. FluxAudit solves this through AI-powered automation."
        ]
    },
    "risks_manual_audit": {
        "keywords": ["risks", "without", "not", "using", "penalties", "loss"],
        "responses": [
            "Businesses face several major risks: Financial loss from undetected fraud, compliance penalties and fines, reputational damage, and making poor decisions based on outdated data.",
            "Without a tool like FluxAudit, you risk significant financial loss from fraud, heavy fines from non-compliance, and damage to your company's reputation.",
            "The main risks are failing to detect fraud, missing regulatory requirements, and wasting employee hours on error-prone manual tasks."
        ]
    },
    "ai_meaning": {
        "keywords": ["ai-powered", "ai", "mean", "artificial", "intelligence", "how", "pattern"],
        "responses": [
            "In this context, 'AI-powered' means the system actively learns from and analyzes your financial data. It looks for unusual patterns and outliers that a human might miss.",
            "It's the difference between a simple calculator and a proactive financial analyst. It actively flags potential fraud, rather than just checking pre-set rules.",
            "It means the system uses AI-driven pattern recognition to identify fraudulent activities as they happen, not just after the fact."
        ]
    },
    "business_value": {
        "keywords": ["value", "roi", "savings", "investment", "economic", "business", "case"],
        "responses": [
            "The economic case is built on a strong Return on Investment (ROI). Value comes from cost reduction (less manual work), loss prevention (catching fraud early), and risk avoidance (avoiding fines).",
            "A positive ROI is expected within 12 to 18 months. The savings from preventing fraud and reducing man-hours far outweigh the initial costs.",
            "Value is generated in three key areas: 1. Reducing manual auditing costs, 2. Preventing financial losses from fraud, and 3. Avoiding multi-million dollar compliance penalties."
        ]
    },
    "cost_model": {
        "keywords": ["cost", "capex", "opex", "capital", "operational", "expenditure"],
        "responses": [
            "The initial development (tools, team time) is a one-time project cost, or Capital Expenditure (CapEx).",
            "The ongoing cloud infrastructure on Azure and maintenance costs are a predictable Operational Expenditure (OpEx)."
        ]
    },
    "target_users": {
        "keywords": ["who", "users", "for", "roles", "cfo", "auditor", "ceo", "admin"],
        "responses": [
            "FluxAudit is for any organization needing to maintain financial integrity. Key users include CFOs, finance departments, internal audit teams, and executive leadership.",
            "The system is designed for multiple roles: Finance Officers, Internal Auditors, Regulators, Admins for system management, and Executives for high-level dashboards.",
            "The target users are finance professionals, auditors, and compliance officers who need to ensure financial integrity."
        ]
    },
    "user_impact": {
        "keywords": ["impact", "daily", "work", "training", "learn", "intuitive", "adoption"],
        "responses": [
            "FluxAudit is designed to be intuitive and streamline daily tasks. It shifts an auditor's job from 'data collector' to 'data analyst', allowing them to focus on high-risk items.",
            "It's designed to be easy to use. Comprehensive training and onboarding will be provided to ensure all users can be confident from day one.",
            "It makes work easier. Instead of spending 80% of their time finding data, auditors will receive pre-analyzed data with anomalies already flagged."
        ]
    },
    "key_features": {
        "keywords": ["features", "capabilities", "what", "can", "it", "do", "nlp"],
        "responses": [
            "Key features include: Role-Based Access Control, Interactive Dashboards, AI-Powered Anomaly Detection, Automated Report Generation (PDF/Excel), and Secure, Unchangeable Audit Trails.",
            "The core features are AI anomaly detection, automated reporting, interactive dashboards, and secure role-based access for different user types. It also includes NLP for adapting to different languages.",
            "It includes NLP for different languages, secure audit trails, automated reporting, and AI-driven fraud detection."
        ]
    },
    "feature_dashboard": {
        "keywords": ["dashboard", "charts", "graphs", "visualization"],
        "responses": [
            "The interactive dashboards translate complex financial data into simple, graphical charts. This allows for a quick, at-a-glance understanding of the company's financial health.",
            "Dashboards are a key feature, allowing executives to see a high-level summary while auditors can drill down into details."
        ]
    },
    "feature_reporting": {
        "keywords": ["report", "pdf", "excel", "export", "data", "reporting", "generation"],
        "responses": [
            "Yes, automated report generation is a key feature. It saves hundreds of hours by allowing users to create and export complex compliance and financial reports (in PDF, Excel, etc.) with a single click.",
            "Absolutely. You can export audit findings, anomaly reports, and summaries as PDF or CSV/Excel files."
        ]
    },
    "feature_security": {
        "keywords": ["secure", "security", "how", "safe", "encryption", "jwt", "audit", "trail"],
        "responses": [
            "Security is a top priority. The system uses robust measures including full data encryption (at rest and in transit), secure JWT tokens for user authentication, and mandatory HTTPS.",
            "It creates a secure, unchangeable (immutable) audit trail of all financial activities, which is a non-negotiable compliance feature providing a single source of truth."
        ]
    },
    "project_plan": {
        "keywords": ["plan", "timeline", "how", "long", "team", "phases", "develop"],
        "responses": [
            "The total project timeline is estimated at 20-22 weeks (around 5 months).",
            "The project is broken down into 6 phases: Requirement Gathering, System Design, Development, Integration, System Testing, and Deployment.",
            "The team is a lean group consisting of a Project Manager, Backend Developer, Frontend Developer, Full-stack Developer, and a QA Tester."
        ]
    },
    "system_quality": {
        "keywords": ["scalability", "reliable", "availability", "uptime", "grow", "enterprise"],
        "responses": [
            "Yes, the system is designed to be highly scalable, meaning it can support enterprise-level data volumes and a growing number of users without slowing down.",
            "Yes, it is built for high availability, targeting a 99.9% uptime. Its cloud-based deployment on Azure makes it reliable and accessible when you need it."
        ]
    },
    "integration": {
        "keywords": ["integration", "connect", "tools", "alerts", "notifications", "email", "sms"],
        "responses": [
            "Yes. FluxAudit is designed to integrate with your existing workflows. It can export all critical data to standard formats like PDF and Excel.",
            "It also uses Email and/or SMS services to send important alerts (like fraud warnings or compliance deadlines) directly to the right people."
        ]
    },
    "strategic_advantage": {
        "keywords": ["advantage", "why", "build", "strategic", "necessary", "need", "nice"],
        "responses": [
            "The strategic advantage is threefold: It creates operational excellence, positions the company as a leader in financial integrity, and provides the tools to make decisions based on real-time, trusted data.",
            "In the modern regulatory environment, a system that ensures compliance and prevents fraud is a 'need to have.' The cost of not having it (fines, fraud losses) is far greater than the cost of implementation."
        ]
    },
    "project_risks": {
        "keywords": ["risks", "mitigation", "scope", "creep", "adoption", "technical"],
        "responses": [
            "The main project risks are: Employee resistance to change (Adoption Risk), AI complexity (Technical Risk), and the project growing beyond its goals (Scope Creep).",
            "These risks are managed with clear mitigation: 1. Comprehensive training and an intuitive UI to manage adoption. 2. Using a proven, modern tech stack (not inventing) to manage technical risk. 3. A clear requirements phase to prevent scope creep."
        ]
    },
    "unknown": {
        "responses": [
            "I'm sorry, I don't have information on that specific topic. I can answer questions about FluxAudit's features, purpose, or security.",
            "My apologies, I don't seem to understand. Could you rephrase your question?",
            "I'm not sure how to respond to that. I can answer questions about FluxAudit's business value, project plan, and key features."
        ]
    }
}


# --- FUZZY MATCHING LOGIC (This logic stays the same) ---

def get_bot_response(user_message):
    """
    Parses the user message, finds a matching topic using fuzzy matching,
    and returns a random response.
    """
    user_message = user_message.lower()
    user_words = user_message.split()  # Split user's sentence into words

    # We will store all matches and their scores
    topic_scores = {}

    for topic, data in knowledge_base.items():
        if "keywords" in data:
            topic_scores[topic] = 0  # Initialize score for this topic

            # Compare each word from the user with each keyword for the topic
            for user_word in user_words:
                for keyword in data["keywords"]:
                    # Get a "similarity ratio" (0-100)
                    similarity = fuzz.ratio(user_word, keyword)

                    # If a word is a very close match (e.g., "frad" vs "fraud")
                    if similarity > 85:
                        topic_scores[topic] += similarity  # Add the score

                        # Give a big bonus for very strong keywords
                        if topic == keyword:
                            topic_scores[topic] += 20

    # Find the topic with the highest score
    if topic_scores:
        best_topic = max(topic_scores, key=topic_scores.get)

        # If the best score is above a minimum threshold, we have a match
        if topic_scores[best_topic] > 50:  # Threshold of 50
            return random.choice(knowledge_base[best_topic]["responses"])

    # If no topic scores high enough, return the "unknown" response
    return random.choice(knowledge_base["unknown"]["responses"])