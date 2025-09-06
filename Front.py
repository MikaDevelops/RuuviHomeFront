from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('index.html')
@app.route("/login", methods=["GET"])
def login_page():
    return "login"
@app.route("/login", methods=["POST"])
def tryLogin():
    return "tried login"
@app.route("/data")
def dataFetch():
    return request.args.get('from', 'no args')

if __name__ == "__main__":
    app.run(ssl_context = 'adhoc')