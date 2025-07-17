from transformers import pipeline

# Load HuggingFace summarization pipeline (BART by default)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text: str) -> str:
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']