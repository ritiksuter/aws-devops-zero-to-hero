from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # Returning string from this function (Here we have a simple flask application)
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()



