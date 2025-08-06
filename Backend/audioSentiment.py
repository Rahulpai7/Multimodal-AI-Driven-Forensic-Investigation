import requests
import time

from loguru import logger
import os

API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN", "")  # Get from environment variable
if not API_TOKEN:
    logger.warning("HUGGINGFACE_API_TOKEN not set! Audio sentiment analysis will not work.")

API_URL = "https://api-inference.huggingface.co/models/Rajaram1996/Hubert_emotion"
headers = {"Authorization": f"Bearer {API_TOKEN}"} if API_TOKEN else {}

def query(filename, wait_for_model=True):
    with open(filename, "rb") as f:
        data = f.read()
    options = {"wait_for_model": wait_for_model}
    response = requests.post(API_URL, headers=headers, data=data, params=options)
    return response

def AudioSentiment(audio_file, wait_for_model=True):
    retry_count = 0
    max_retries = 5
    retry_delay = 5  

    while retry_count < max_retries:
        output = query(audio_file, wait_for_model)
        if output.status_code == 200:
            return output.json()
        elif output.status_code == 503 and "loading" in output.text:
            retry_count += 1
            print(f"Model is still loading. Retrying in {retry_delay} seconds... (Retry {retry_count}/{max_retries})")
            time.sleep(retry_delay)
        else:
            return {"error": output.text, "status_code": output.status_code}

    return {"error": "Max retries reached. Model is still loading."}



