from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World! finally setup is down'  


if __name__ == '__main__':
    app.run(debug=True) # Run the app in debug mode for development