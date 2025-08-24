from flask import Flask

app = Flask(__name__)

@app.route("/")
def main_page():
    return "hello!"
@app.route("/login", methods=["GET"])
def login_page():
    return "login"
@app.route("/login", methods=["POST"])
def tryLogin():
    return "tried login"

if __name__ == "__main__":
    app.run(ssl_context = 'adhoc')