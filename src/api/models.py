'''
Acts as a contract for your API
It defines what exactly data your API accepts as input and what it promises to return as Output
'''

from email import message
from pydantic import BaseModel, Field

class AnalysisRequest(BaseModel):
    ticker: str = Field(..., description="The stock ticker symbol (e.g. MSFT, NVDA, AMZN)")


class AnalysisResponse(BaseModel):
    status: str
    ticker: str
    report_content: str
    report_url: str
    message: str

