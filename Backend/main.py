from fastapi import FastAPI,UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from pathlib import Path
from moviepy.editor import *
from fastapi.responses import JSONResponse,FileResponse
from audioSentiment import AudioSentiment
from textSentiment import summary_sentiment
import pandas as pd

from transformers import pipeline,AutoModelForSeq2SeqLM, AutoTokenizer
import re

summary = ""

UPLOAD_DIR = Path() / 'uploads'
UPLOAD_DIR.mkdir(exist_ok=True)  # Create uploads directory if it doesn't exist

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/uploadfile/")
async def create_upload_file(file_upload: UploadFile):
    try:
        data = await file_upload.read()
        save_to = UPLOAD_DIR / file_upload.filename
        with open(save_to, 'wb') as f:
            f.write(data)
        logger.info(f"File {file_upload.filename} saved to {save_to}")
        
        if file_upload.filename.lower().endswith(".mp4"):
            logger.info("Processing video file...")
            video_path = str(UPLOAD_DIR / file_upload.filename)
            video = VideoFileClip(video_path)
            audio_filename = file_upload.filename.replace(".mp4", ".mp3")
            audio_path = str(UPLOAD_DIR / audio_filename)
            video.audio.write_audiofile(audio_path)
            video.close()  # Properly close the video file
            file_upload.filename = audio_filename
    except Exception as e:
        logger.error(f"Error processing file: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"error": f"Error processing file: {str(e)}"}
        )
    
    whisper = pipeline('automatic-speech-recognition', model = 'openai/whisper-medium')

    path = 'uploads/' + file_upload.filename

    text = whisper(path)

    logger.info(text)

    output = text["text"].lower()

    output_parsed = re.sub(r"\s*interrogator[,\?\.]?", "\n\ninterrogator: ", output)
    output_parsed = re.sub(r"\s*witness[,\?\.]?", "\n\nwitness: ", output_parsed)

    logger.info(output_parsed)

    model_ckpt = "foren_summer_bart_large"

    tokenizer = AutoTokenizer.from_pretrained(model_ckpt)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_ckpt)
    tokens = tokenizer.tokenize(output_parsed)
    logger.info(len(tokens))
    inputs = tokenizer(output_parsed, return_tensors="pt", max_length=1024,truncation=True)

    summary_ids = model.generate(**inputs,max_length=3072,min_length=(int(len(tokens)/2)))
    summary = tokenizer.decode(*summary_ids, skip_special_tokens=True)
    
    logger.info(summary)
    sentiment = summary_sentiment(output_parsed)
    audioSenti = AudioSentiment(path)
    
    concatenated_data = f"""File: {file_upload.filename}\n\nText: {text}\n\nOutput: {output}\n\nSummary: {summary}\n\nSentiment: {sentiment}\n\nAudio Sentiment: {audioSenti}"""
    
    with open('output.txt', 'a') as txt_file:
        txt_file.write(concatenated_data)
        
    try:
        df = pd.read_excel('output.xlsx')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['File', 'Text', 'Output', 'Summary', 'Sentiment', 'Audio Sentiment'])

    new_data = pd.DataFrame({'File': [file_upload.filename], 'Text': [text], 'Output': [output], 'Summary': [summary],
                             'Sentiment': [sentiment], 'Audio Sentiment': [audioSenti]})
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_excel('output.xlsx', index=False)

    return {"filename": file_upload.filename, "summary": summary , "dialogue": text["text"] , "audioSenti": audioSenti, "sentiment": sentiment,"video":FileResponse("tedx.mp4")}



    