from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask!"

@app.route('/greet')
def greet():
    name = request.args.get('name', 'World')
    return f"Hello, {name}!"

@app.route('/data', methods=['POST'])
def data():
    return jsonify(request.get_json() or {"error": "No data received"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
