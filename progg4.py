from flask import Flask

app = Flask(__name__)

@app.route("/ping_cpe/<string:hostname>")
def hello_world(hostname):
    # hier alle functionaliteit om de ping te doen.
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True)

