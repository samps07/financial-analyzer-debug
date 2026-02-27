# task.py

from crewai import Task
from agents import verifier, financial_analyst, risk_assessor, investment_advisor

# Task 1: Verification
verification_task = Task(
    description="Analyze the document at {file_path}. Determine if it is a financial report. If it is a grocery list or unrelated text, fail the task immediately.",
    expected_output="A confirmation that the document is valid for financial analysis, or a detailed reason why it is rejected.",
    agent=verifier
)

# Task 2: Data Extraction
analysis_task = Task(
    description="Using the document at {file_path}, extract the following metrics: Revenue, GAAP Net Income, and Free Cash Flow. Then, answer the user's specific query: {query}",
    expected_output="A structured summary of key financial metrics and a data-driven answer to the query.",
    agent=financial_analyst,
    context=[verification_task] # Only runs if verification passes
)

# Task 3: Risk Assessment
risk_task = Task(
    description="Review the financial analysis and the original document. List 3 specific financial or operational risks mentioned or implied by the numbers.",
    expected_output="A bulleted list of 3 high-priority risks with page references where possible.",
    agent=risk_assessor,
    context=[analysis_task]
)

# Task 4: Final Recommendation
advice_task = Task(
    description="Review the data and risks. Provide a final investment outlook based on the query: {query}",
    expected_output="A professional 2-paragraph investment recommendation with a clear 'Buy/Hold/Sell' stance.",
    agent=investment_advisor,
    context=[analysis_task, risk_task]
)
