import pandas as pd
import re


def load_sample_data(n=30):
    """Return a simple sample dataframe for demos.

    Columns: date (int), value_a, value_b
    """
    dates = pd.date_range(start="2025-01-01", periods=n, freq="D")
    df = pd.DataFrame({
        "date": dates,
        "value_a": (pd.Series(range(n)) + pd.Series([i%5 for i in range(n)])*2),
        "value_b": (pd.Series(range(n))[::-1] + 5),
    })
    return df


def summarize_text(text: str, min_len: int = 20) -> str:
    """A tiny heuristic summarizer: returns sentences longer than min_len joined.

    This is intentionally simple — replace with an NLP model or library later.
    """
    if not text:
        return ""
    # Split into sentences (very naive)
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    long_sentences = [s for s in sentences if len(s.split()) >= (min_len // 5)]
    if not long_sentences:
        # fall back to the first two sentences
        return " ".join(sentences[:2])
    return " ".join(long_sentences)
