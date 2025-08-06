from loguru import logger
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import pandas as pd
from rouge import Rouge


try:
    df = pd.read_excel('test.xlsx')
except FileNotFoundError:
    logger.error("test.xlsx file not found!")
    df = pd.DataFrame(columns=['Dialogue', 'Summary'])

# Initialize the ROUGE scorer
rouge = Rouge()


model_ckpt = "foren_summer_bart_large"
tokenizer = AutoTokenizer.from_pretrained(model_ckpt)
model = AutoModelForSeq2SeqLM.from_pretrained(model_ckpt)


def generate_summary(input_text,target_summary):
    logger.info(f"Target summary word count: {len(target_summary.split())}")
    inputs = tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True)
    # Set max_length to a reasonable value (e.g., 256 tokens)
    # Set min_length to a fraction of the target summary length in tokens
    target_token_count = len(tokenizer.tokenize(target_summary))
    min_length = max(10, int(0.7 * target_token_count))
    max_length = min(256, int(1.5 * target_token_count))
    summary_ids = model.generate(
        **inputs,
        max_length=max_length,
        min_length=min_length,
        num_beams=4,
        early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


all_summaries = []
all_targets = []



# Check for required columns
required_columns = {'Dialogue', 'Summary'}
if not required_columns.issubset(df.columns):
    raise ValueError(f"Input file must contain columns: {required_columns}")

for index, row in df.iterrows():
    input_text = row['Dialogue']
    target_summary = row['Summary']
    generated_summary = generate_summary(input_text, target_summary)
    all_summaries.append(generated_summary)
    all_targets.append(target_summary)


rouge_result = rouge.get_scores(all_summaries, all_targets, avg=True)

logger.info(f"ROUGE scores: {rouge_result}")
