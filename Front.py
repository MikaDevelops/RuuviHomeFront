from flask import Flask, render_template, request
from access_controller.AccessController import AccessController
import sys

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('index.html')

@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def tryLogin():
    message = request.get_json()
    if accController.checkMainUserPassword(message['passwordings']):
        token = accController.giveNewToken()
        jsonString = '{"token":"'+token +'"}'
        return jsonString
    return '{"token":"failed"}'

@app.route("/data")
def dataFetch():
    if accController.checkToken(request.args.get('token')):
        return "success"
    else:
        return "please login"

if __name__ == "__main__":
    arg = sys.argv[1]
    accController = AccessController(arg)
    accOk = accController.pwOk()
    if accOk != True:
        print("pw not ok")
        sys.exit()
    app.run(ssl_context = 'adhoc')