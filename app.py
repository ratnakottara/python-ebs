from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    with open('index.html', 'r') as f:
        return f.read()

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']
    output = "You entered: " + user_input
    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
