import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from tools import search_tool, FinancialDocumentTool

load_dotenv()

# --- THE FIX: BRUTE FORCE ROUTING ---
# 1. We tell the system exactly which API Key to use
api_key = os.getenv("GEMINI_API_KEY")

# 2. We set these specific variables to force LiteLLM into 'Gemini' mode 
# instead of 'Vertex' mode.
os.environ["GEMINI_API_KEY"] = api_key
os.environ["GOOGLE_API_KEY"] = api_key

# 3. We define the LLM using the 'gemini/' prefix, but we explicitly 
# set the provider to 'google_generative_ai' inside the LLM object.
gemini_llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=api_key,
    provider="google_generative_ai", # This is the internal name for AI Studio
    temperature=0.2
)

# Document Verifier
verifier = Agent(
    role="Lead Document Compliance Officer",
    goal="Ensure the uploaded document is a valid corporate financial report.",
    verbose=True,
    backstory="You have 20 years of experience in financial auditing.",
    llm=gemini_llm, 
    max_iter=5,
    allow_delegation=False
)
# ... apply 'llm=gemini_llm' to all other agents

# 2. Senior Financial Analyst
financial_analyst = Agent(
    role="Senior Equity Research Analyst",
    goal="Extract precise financial data for: {query}",
    verbose=True,
    memory=True,
    backstory="Meticulous quantitative analyst from a top-tier bank.",
    tools=[FinancialDocumentTool.read_data_tool],
    llm=gemini_llm,
    max_iter=10
)

# 3. Risk Assessor
risk_assessor = Agent(
    role="Chief Risk Officer",
    goal="Identify financial and operational risks mentioned in the document.",
    verbose=True,
    backstory="Expert at spotting red flags in financial statements.",
    llm=gemini_llm,
    max_iter=5
)

# 4. Investment Advisor
investment_advisor = Agent(
    role="Fiduciary Investment Advisor",
    goal="Provide a final Buy/Hold/Sell recommendation.",
    verbose=True,
    backstory="Synthesizes data and risks into clear investment advice.",
    llm=gemini_llm,
    max_iter=5
)
