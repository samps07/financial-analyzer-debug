# tools.py

import os
from langchain_community.document_loaders import PyPDFLoader
from crewai.tools import tool

class FinancialDocumentTool:
    
    @tool("read_data_tool")
    def read_data_tool(path: str):
        """
        Reads and extracts all text content from a financial PDF document located at the given path.
        Use this tool to get the raw data needed for financial analysis.
        """
        if not os.path.exists(path):
            return f"Error: The file at {path} was not found."
        
        try:
            # Using PyPDFLoader for robust text extraction
            loader = PyPDFLoader(path)
            docs = loader.load()
            
            # Combine all pages into one string
            full_report = "\n".join([doc.page_content for doc in docs])
            
            # Basic cleaning: Remove excessive newlines
            import re
            full_report = re.sub(r'\n{3,}', '\n\n', full_report)
            
            return full_report
            
        except Exception as e:
            return f"Error reading PDF: {str(e)}"

# We can keep the SerperDevTool for external market research if needed
from crewai_tools import SerperDevTool
search_tool = SerperDevTool()
