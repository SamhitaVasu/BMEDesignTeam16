import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Load OpenAI API key from environment variables

def image_generating_function(message):
    response = client.images.generate(
        model="dall-e-3",
        prompt=message,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    return image_url
    

def get_chat_response(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )

    return response 


def processing_function(iput_text):
    try:
        # Call the OpenAI API with the input text
        response = client.completions.create(
        model="gpt-4",  # or "gpt-4" based on the availability
        prompt=iput_text,
        temperature=0.7,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
        
        # Extract the text from the response
        processed_text = response.choices[0].text.strip()
        
        return processed_text
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return "Error processing your request."