# langchain-chatbot
This project implements a custom chatbot utilizing the Langchain framework and Flask web framework. The chatbot is designed to provide information about technical courses extracted from the Brainlox website.

# Custom Chatbot using Langchain and Flask

This project implements a custom chatbot utilizing the Langchain framework and Flask web framework. The chatbot is designed to provide information about technical courses extracted from the [Brainlox website](https://brainlox.com/courses/category/technical).

## Features

- **Data Extraction**: Automatically fetches course information from the specified URL using a web scraping loader.
- **Embeddings**: Creates vector embeddings of the extracted documents using OpenAI’s embeddings model, enabling efficient similarity search.
- **RESTful API**: Exposes a simple RESTful API using Flask to handle user queries and provide relevant course information.

## Technologies Used

- **Python**: The programming language for the entire application.
- **Langchain**: A framework for building language model applications.
- **Flask**: A lightweight web framework for creating the API.
- **FAISS**: A library for efficient similarity search and clustering of dense vectors.

## Getting Started

### Prerequisites

- Python 3.x
- OpenAI API key (required for embedding generation)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AyaanShaher/langchain-chatbot.git

2. Navigate to the project directory:

 ```bash
cd custom-chatbot
```


3. Install the required dependencies:
```bash
 pip install -r requirements.txt
```

Configuration
->  Set your OpenAI API key in the chatbot.py file where indicated.

Run the application:
```bash
python chatbot.py
```
The application will start running on http://127.0.0.1:5000.

API Usage:
Send a POST request to the /chat endpoint with a JSON payload containing your query.
```bash
curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d "{\"message\":\"Tell me about technical courses.\"}"
```





