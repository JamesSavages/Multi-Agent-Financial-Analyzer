'''
Server entry point
this file wires everything together and starts the application 
FAST API entry point
'''

from fastapi import FastAPI
from src.api.routes import router

# initialize fastAPI object (application instance)
app = FastAPI(
    title="CrewAI Financial Analyst API",
    description="A Production-Grade Agentic API for Stock Analysis.",
    version="1.0.0"
)

# includde our analysis routes
app.include_router(router, prefix="/api/v1")

@app.get("/")
def health_check():
    """Simple health check to verify the server is running."""
    return {"status": "healthy", "service": "Financial Analyst Crew"}