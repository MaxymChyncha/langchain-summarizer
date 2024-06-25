# LangChainSummarizer 🦜

This FastAPI application provides an endpoint to summarize text using a pre-trained model from Hugging Face.

## Requirements
- Python 3.7+
- FastAPI
- Pydantic
- Transformers (Hugging Face)

## Setup

1. Clone repo from git:
   ```bash
   git clone https://github.com/MaxymChyncha/langchain-summarizer.git
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # For Windows `venv\Scripts\activate`
   ```

3Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

2. Open your browser and go to http://127.0.0.1:8000/docs to access the API documentation and test the endpoint.


### Endpoint

```POST /summarize```

Request Body:

```json
{
  "text": "Text for summarization"
}
```

Response:

```json
{
  "summary": "Summarized text"
}
```
