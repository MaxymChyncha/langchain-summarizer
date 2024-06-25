from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline


class Summarizer:
    """
    Handles text summarization using a pre-trained model.
    """

    def __init__(self):
        """
        Initializes the summarizer with the 'facebook/bart-large-cnn' model.
        """
        self._pipeline = pipeline("summarization", model="facebook/bart-large-cnn")
        self._summarizer = HuggingFacePipeline(pipeline=self._pipeline)

    def summarize(self, text: str) -> str:
        """
        Summarizes the given text.

        Args:
        text (str): The text to summarize.

        Returns:
        str: The summarized text.
        """
        return self._summarizer(text)
