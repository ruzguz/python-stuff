from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world. this is another test'

if __name__ == '__main__':
    app.run()
