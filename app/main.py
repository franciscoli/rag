from flask import Flask, request, jsonify
import os
from embedchain import App
import embedchain
print(embedchain.__version__)
app = Flask(__name__)
#app_rag = App()
app_rag = App.from_config("./configs.yaml")

"""
Este código exemplifica como é posssivel usar a framework com o flask

"""
def generate_response(question):
    # Simple example of generating a respocnse based on the question
    response = app_rag.query(question, citations=True)
    print(response)
    return response

@app.route('/question', methods=['POST'])
def question():
    content = request.json
    question_text = content.get('question')
    if question_text:
        response_text = generate_response(question_text)
        response = {
            "message": "Question received",
            "question": question_text,
            "response": response_text
        }
    else:
        response = {
            "message": "No question received"
        }
    return jsonify(response)


if __name__ == '__main__':
    app_rag.add("./docs/tunelSecagem.pdf")
    app.run(debug=True)
