from services import Summarizer


async def summarize_text(message: str) -> dict:
    """
    Summarizes the provided text message using a pre-trained summarization model.

    Args:
    -----
    message : str
        The text message to be summarized.

    Returns:
    --------
    dict
        A dictionary containing the summarized text under the key "summary".
    """
    summarizer = Summarizer()
    return {"summary": summarizer.summarize(text=message)}
