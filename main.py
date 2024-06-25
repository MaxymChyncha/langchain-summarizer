from fastapi import FastAPI, HTTPException

import crud
from schemas import Message

app = FastAPI()


@app.post("/summarize")
async def summarize_text(message: Message) -> dict:
    """
    Summarize the provided text message.

    Args:
    - message (Message): A pydantic model containing the text to be summarized.

    Returns:
    - dict: A dictionary containing the summarized text.

    Raises:
    - HTTPException: If the summarization process fails.
    """
    try:
        summary = await crud.summarize_text(message.text)
        return summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
