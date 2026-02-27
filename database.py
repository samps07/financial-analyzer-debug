import os
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

# Get your connection string from MongoDB Atlas
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGODB_URL)
db = client.financial_analyzer

async def save_analysis(file_name: str, query: str, analysis: str):
    """
    Saves the analysis results to MongoDB.
    This fulfills the 'Database Integration' bonus requirement.
    """
    try:
        collection = db.analysis_history
        document = {
            "file_name": file_name,
            "query": query,
            "analysis": str(analysis),
            "timestamp": datetime.utcnow()
        }
        result = await collection.insert_one(document)
        return str(result.inserted_id)
    except Exception as e:
        print(f"Database error: {e}")
        return "Not saved to DB"
