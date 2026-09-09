from flask import Flask, jsonify

app = Flask(__name__)

def add(a, b):
    return a + b

@app.route("/")
def home():
    return jsonify(
        message="CI/CD pipeline is working!",
        result=add(10, 20)
    )
