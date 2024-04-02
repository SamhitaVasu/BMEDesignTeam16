import os
from langchain_openai import OpenAI

# Ensure your OPENAI_API_KEY is loaded from your environment variables
openai_api_key = os.getenv('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')
if not openai_api_key:
    raise Exception("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

# Initialize LangChain with OpenAI
langchain_openai = OpenAI(api_key=openai_api_key)

print("LangChain configured with OpenAI successfully.")