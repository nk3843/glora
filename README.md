# GLORA: Global Events Analysis with LangChain

GLORA is a powerful tool for analyzing and querying global events using natural language. It combines the capabilities of LangChain with vector embeddings to provide semantic search and conversational analysis of event data.

## Features

- 🔍 Semantic search for global events
- 💬 Natural language querying
- 📊 Event metadata analysis
- 🤖 Conversational interface
- 📅 Temporal analysis with date filtering
- 🌍 Actor-based event filtering

## Prerequisites

- Python 3.8+
- FastAPI
- LangChain
- ChromaDB
- HuggingFace Transformers

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd glora
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
glora/
├── app/
│   ├── api_routes.py    # FastAPI route handlers
│   ├── main.py         # FastAPI application setup
│   └── schemas.py      # Pydantic models
├── core/
│   ├── agent.py        # LangChain agent setup
│   ├── embedder.py     # Text embedding configuration
│   └── vectorstore.py  # Vector store operations
├── embeddings/         # Vector store persistence (gitignored)
└── requirements.txt    # Project dependencies
```

## Usage

1. Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

2. The API will be available at `http://localhost:8000`

### API Endpoints

#### Query Events
```http
POST /query
Content-Type: application/json

{
    "query": "Find events related to trade agreements",
    "k": 5,
    "page": 1,
    "page_size": 10
}
```

#### Chat Interface
```http
POST /chat
Content-Type: application/json

{
    "messages": [
        {"role": "user", "content": "What were the major trade events in 2022?"}
    ]
}
```

## Development

### Adding New Features

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Running Tests

```bash
pytest
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain)
- [ChromaDB](https://github.com/chroma-core/chroma)
- [FastAPI](https://github.com/tiangolo/fastapi)
- [HuggingFace](https://huggingface.co/) 