from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>demo-task</h1><p>Create a simple test app that shows Hello World</p>'

@app.route('/health')
def health():
    return jsonify(status='ok')
