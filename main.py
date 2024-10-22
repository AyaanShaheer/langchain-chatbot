from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from langchain.document_loaders import WebBaseLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document

# Step 1: Data Extraction
url = "https://brainlox.com/courses/category/technical"
loader = WebBaseLoader(url)
documents = loader.load()

# Displaying the extracted documents
for doc in documents:
    print(doc.page_content)

# Step 2: Initialize Embeddings
docs = [Document(page_content=doc.page_content) for doc in documents]
embeddings = OpenAIEmbeddings(openai_api_key="sk-TiZbxd_p-rv9mLQjNdOMSwweEuD8n4mpBOHiV-QohjT3BlbkFJo-sXxvb6TgWj2FFwLXBXv-hzhEW2oFi9lEm4nfvMUA")
vector_store = FAISS.from_documents(docs, embeddings)
vector_store.save_local("faiss_index")

# Load vector store for querying
vector_store = FAISS.load_local("faiss_index", embeddings)

# Step 3: Set Up Flask API
app = Flask(__name__)
api = Api(app)

class Chat(Resource):
    def post(self):
        data = request.get_json()
        user_message = data.get('message')

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        response = self.get_response(user_message)
        return jsonify({"response": response})

    def get_response(self, user_message):
        # Query the vector store for similar documents
        docs_with_scores = vector_store.similarity_search_with_score(user_message)
        
        # Formulate a response based on the top document (you can modify this logic)
        if docs_with_scores:
            best_doc, score = docs_with_scores[0]
            return best_doc.page_content  # Returning the content of the best matching document
        return "Sorry, I couldn't find relevant information."

# Add resource to API
api.add_resource(Chat, '/chat')

if __name__ == '__main__':
    app.run(debug=True)

