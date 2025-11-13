from utils import summarize_text


def test_summarize_empty():
    assert summarize_text("") == ""


def test_summarize_short():
    text = "First short. Second short."
    s = summarize_text(text, min_len=10)
    # fallback returns the first sentences if none are "long"
    assert "First" in s or "Second" in s


def test_summarize_long_sentence():
    text = (
        "This is a sufficiently long sentence that should be picked out by the summarizer "
        "because it has many words. Short."
    )
    s = summarize_text(text, min_len=20)
    assert "sufficiently long" in s
