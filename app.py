import json
import random

from flask import Flask, redirect, url_for, request, jsonify, make_response

app = Flask(__name__)

data = json.load(open('services.json'))
imeiservicelist = data["IMEISERVICELIST"]
accountinfo = data["ACCOUNTINFO"]


@app.route('/api/index.php', methods=['POST', 'GET'])
def imeiservices():  # put application's code here
    if request.method == 'POST' and request.form['action'] == 'imeiservicelist':
        return imeiservicelist
    elif request.method == 'POST' and request.form['action'] == 'accountinfo':
        return accountinfo
    else:
        return make_response(jsonify({"status": "read documentation"}), 400)


if __name__ == '__main__':
    app.run()
