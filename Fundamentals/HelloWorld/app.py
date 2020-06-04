from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    message ="Hello World from Flask"
    return message

if __name__ == '__main__':
    app.run(debug=False)