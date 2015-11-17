from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<script>alert("Hello World!")</script>'

if __name__ == "__main__":
    app.run()
