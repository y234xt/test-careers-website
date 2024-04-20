from flask import Flask  # Import Flask Class

app = Flask(__name__)  # Create an Instance


@app.route("/")
def hello_world():
  return "Hello, World!"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
