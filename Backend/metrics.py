from typing import Union
from loguru import logger

def wer(reference: str, hypothesis: str) -> float:
    """
    Calculate Word Error Rate between reference and hypothesis texts.
    
    Args:
        reference (str): The reference text
        hypothesis (str): The hypothesis text to compare against
        
    Returns:
        float: The Word Error Rate score
    """
    reference = reference.split()
    hypothesis = hypothesis.split()
    distance = [[0] * (len(hypothesis) + 1) for _ in range(len(reference) + 1)]

    for i in range(len(reference) + 1):
        for j in range(len(hypothesis) + 1):
            if i == 0:
                distance[i][j] = j
            elif j == 0:
                distance[i][j] = i
            else:
                if reference[i - 1] == hypothesis[j - 1]:
                    distance[i][j] = distance[i - 1][j - 1]
                else:
                    distance[i][j] = 1 + min(distance[i - 1][j], distance[i][j - 1], distance[i - 1][j - 1])

    return distance[len(reference)][len(hypothesis)]

def cer(reference, hypothesis):
    # CER should be calculated at the character level
    reference = list(reference)
    hypothesis = list(hypothesis)
    distance = [[0] * (len(hypothesis) + 1) for _ in range(len(reference) + 1)]

    for i in range(len(reference) + 1):
        for j in range(len(hypothesis) + 1):
            if i == 0:
                distance[i][j] = j
            elif j == 0:
                distance[i][j] = i
            else:
                if reference[i - 1] == hypothesis[j - 1]:
                    distance[i][j] = distance[i - 1][j - 1]
                else:
                    distance[i][j] = 1 + min(distance[i - 1][j], distance[i][j - 1], distance[i - 1][j - 1])

    return distance[len(reference)][len(hypothesis)] / len(reference) if len(reference) > 0 else 0

def calculate_metrics(reference_text: str, hypothesis_text: str) -> dict:
    """
    Calculate WER and CER metrics for given reference and hypothesis texts.
    
    Args:
        reference_text (str): The reference text
        hypothesis_text (str): The hypothesis text to compare against
        
    Returns:
        dict: Dictionary containing WER and CER scores
    """
    try:
        wer_score = wer(reference_text, hypothesis_text)
        cer_score = cer(reference_text, hypothesis_text)
        
        wer_percentage = (wer_score / len(reference_text.split())) * 100 if reference_text else 0
        
        return {
            "wer": round(wer_percentage, 2),
            "cer": round(cer_score * 100, 2)
        }
    except Exception as e:
        logger.error(f"Error calculating metrics: {str(e)}")
        return {
            "error": str(e),
            "wer": 0,
            "cer": 0
        }

if __name__ == "__main__":
    # Example usage
    try:
        with open("reference.txt", "r") as file:
            reference_text = file.read()
        with open("hypothesis.txt", "r") as file:
            hypothesis_text = file.read()
            
        metrics = calculate_metrics(reference_text, hypothesis_text)
        print(f"Word Error Rate (WER): {metrics['wer']}%")
        print(f"Character Error Rate (CER): {metrics['cer']}%")
        
    except FileNotFoundError as e:
        logger.error(f"File not found: {str(e)}")
    except Exception as e:
        logger.error(f"Error: {str(e)}")