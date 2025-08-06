import torch
import torchaudio
from transformers import Wav2Vec2ForSpeechEmotionClassification, Wav2Vec2Processor
from loguru import logger

model_name = "audeering/wav2vec2-large-robust-12-ft-emotion-msp-dim"
processor = Wav2Vec2Processor.from_pretrained(model_name)
model = Wav2Vec2ForSpeechEmotionClassification.from_pretrained(model_name)

# Mapping of emotion labels to their meanings
EMOTION_LABELS = {
    0: "anger",
    1: "joy",
    2: "neutral",
    3: "sadness"
}


def recognize_emotion(audio_path):   
    try:
        # Load and resample audio to 16kHz
        waveform, sample_rate = torchaudio.load(audio_path)
        if sample_rate != 16000:
            resampler = torchaudio.transforms.Resample(sample_rate, 16000)
            waveform = resampler(waveform)
        
        # Process audio
        inputs = processor(waveform.squeeze().numpy(), return_tensors="pt", padding=True, sampling_rate=16000)
        
        with torch.no_grad():
            logits = model(inputs.input_values).logits  
        
        predicted_label_id = torch.argmax(logits, dim=-1).item()
        emotion = EMOTION_LABELS.get(predicted_label_id, "unknown")
        
        logger.info(f"Detected emotion: {emotion}")
        return emotion
        
    except Exception as e:
        logger.error(f"Error in emotion recognition: {str(e)}")
        return "unknown"