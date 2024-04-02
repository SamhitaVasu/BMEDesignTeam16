import os
import openai
from openai import OpenAI
from PIL import Image
import requests
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

openai.api_key = "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"
client = OpenAI(api_key='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')

def identify_parts(instruction):
    parts = ['-1', '-1', '-1', '-1', '-1']
    gpt_response = get_chat_response("In the following medication instruction, what is the action word?: " + instruction + " Choose only 1-2 words. Answer in the form 'action: ACTION'")
    parts[0] = str(gpt_response[list(gpt_response)[1]]).lower().split(':')[-1]
    gpt_response = get_chat_response("In the following medication instruction, what is the quantity taken each time?: " + instruction + " Choose a number. Do not give the units. Answer in the form 'quantity: QUANTITY'")
    parts[1] = str(gpt_response[list(gpt_response)[1]]).lower().split(':')[-1]
    gpt_response = get_chat_response("In the following medication instruction, what is the object?: " + instruction + " Choose only 1-2 words. Answer in the form 'object: OBJECT'")
    parts[2] = str(gpt_response[list(gpt_response)[1]]).lower().split(':')[-1]
    gpt_response = get_chat_response("In the following medication instruction, what is the frequency?: " + instruction + " Choose only 1-2 words. Answer in the form 'frequency: FREQUENCY'")
    parts[3] = str(gpt_response[list(gpt_response)[1]]).lower().split(':')[-1]
    gpt_response = get_chat_response("In the following medication instruction, what is the duration?: " + instruction + " Choose only 1-2 words. Answer in the form 'duration: DURATION'")
    parts[4] = str(gpt_response[list(gpt_response)[1]]).lower().split(':')[-1]
    return parts


def image_generating_function_object(object):
    return generate_image(object + " icon")

def image_generating_function_action(action):
    gpt_response = get_chat_response("If I were to make a concrete icon for the action " 
                                     + action + 
                                     ", what would it contain? Give only one example. Be concise and do not give a definition or thought process." +
                                     " Instead of a full sentence, give the answer in the format 'concrete icon: [ANSWER]'")
    prompt = str(gpt_response[list(gpt_response)[1]]).split('Concrete icon: ')[-1]
    return generate_image(prompt + " icon")

def image_generating_function_quantity(quant):
    return generate_image(quant + " number icon")

def generate_image(message):
    image_prompt = (
        "Subject: " + message +
        "Style: black and white pictogram"    
    )
    try:
        response = openai.images.generate(
            model="dall-e-3",
            prompt=image_prompt,
            size="1024x1024",
            quality="standard",
            n=1
        )
    except openai.APIConnectionError as e:
        print("Server connection error: {e.__cause__}")  # from httpx.
        raise
    except openai.RateLimitError as e:
        print(f"OpenAI RATE LIMIT error {e.status_code}: (e.response)")
        raise
    except openai.APIStatusError as e:
        print(f"OpenAI STATUS error {e.status_code}: (e.response)")
        raise
    except openai.BadRequestError as e:
        print(f"OpenAI BAD REQUEST error {e.status_code}: (e.response)")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise
    image_url = response.data[0].url
    return image_url
    
def show_image(url):
    displayed_image = Image.open(requests.get(url, stream=True).raw)
    displayed_image.show()


def get_chat_response(question):
    template = """Question: {question}
    
    Answer: Let's think step by step."""
    
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=client)

    return llm_chain.invoke(question) 


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