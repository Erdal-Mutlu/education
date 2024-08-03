from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Education World! - Version 0001'

@app.route('/about')
def about():
    return 'This is the About page.'

if __name__ == '__main__':
    app.run(port=80)
