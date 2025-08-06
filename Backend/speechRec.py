import aiohttp
import asyncio
import os
from loguru import logger

API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
if not API_TOKEN:
    logger.warning("HUGGINGFACE_API_TOKEN not set! Speech recognition will not work.")

API_URL = "https://api-inference.huggingface.co/models/Rajaram1996/Hubert_emotion"
headers = {"Authorization": f"Bearer {API_TOKEN}"} if API_TOKEN else {}

async def recognize_speech(filename):
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Audio file not found: {filename}")

        async with aiohttp.ClientSession() as session:
            with open(filename, "rb") as f:
                data = f.read()
            
            async with session.post(API_URL, headers=headers, data=data) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    error_text = await response.text()
                    logger.error(f"API Error: {response.status} - {error_text}")
                    return {"error": f"API Error: {response.status}"}
                    
    except Exception as e:
        logger.error(f"Error in speech recognition: {str(e)}")
        return {"error": str(e)}