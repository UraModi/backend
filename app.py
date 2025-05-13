from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

app = Flask(__name__)
api = Api(app)

# Load the stored FAISS index
embeddings = OpenAIEmbeddings()
vector_db = FAISS.load_local("faiss_index", embeddings)

class Chatbot(Resource):
    def post(self):
        user_input = request.json["message"]
        results = vector_db.similarity_search(user_input, k=3)
        response = [doc.page_content for doc in results]
        return jsonify({"response": response})

api.add_resource(Chatbot, "/chat")

if __name__ == "__main__":
    app.run(debug=True)
