import os
from dotenv import load_dotenv
from langsmith import Client
from langsmith import traceable

# Load your .env file
load_dotenv()

# Initialize the LangSmith client
client = Client()

print("Testing LangSmith Connection...")
print(f"Endpoint: {os.getenv('LANGSMITH_ENDPOINT')}")
print(f"Project: {os.getenv('LANGSMITH_PROJECT')}")

# Use the widely supported traceable decorator
@traceable(name="Verification_Test", run_type="chain")
def dummy_work():
    print("Trace created! Doing some 'work'...")
    return {"status": "success", "message": "LangSmith is connected!"}

try:
    # Call the decorated function
    result = dummy_work()
    print("\n✅ Success! The trace was sent. Check your LangSmith dashboard.")
    
except Exception as e:
    print(f"\n❌ Error connecting to LangSmith: {e}")