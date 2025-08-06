from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import nltk
from nltk.tokenize import sent_tokenize
from loguru import logger

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    logger.info("Downloading NLTK punkt tokenizer...")
    nltk.download('punkt')

# Initialize models once
tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

sentiments = ['very calm', 'mildly nervous', 'nervous', 'fearful', 'very fearful']


def sentiment_analysis(review):
    try:
        tokens = tokenizer.encode(review, return_tensors='pt', truncation=True, max_length=512)
        with torch.no_grad():  # No need to calculate gradients for inference
            result = model(tokens)
        ss = int(torch.argmax(result.logits))+1
        return sentiments[ss-1]
    except Exception as e:
        logger.error(f"Error in sentiment analysis: {str(e)}")
        return "very calm"  # Default to neutral sentiment on error

def summary_sentiment(text):
      calm = 0
      m_nervous = 0
      nervous = 0
      fearful = 0
      v_fearful = 0
      sentences = sent_tokenize(text)
      for sentence in sentences:
            sentiment = sentiment_analysis(sentence)
            if sentiment == 'very calm':
                  calm += 1
            elif sentiment == 'mildly nervous':
                  m_nervous += 1
            elif sentiment == 'nervous':
                  nervous += 1
            elif sentiment == 'fearful':
                  fearful += 1
            elif sentiment == 'very fearful':
                  v_fearful += 1
      length = len(sentences)
      return {"very calm":int((calm/length)*100), "midly nervous":int((m_nervous/length)*100), "nervous":int((nervous/length)*100), "fearful":int((fearful/length)*100), "very fearful":int((v_fearful/length)*100)}