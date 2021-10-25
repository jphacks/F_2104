# -*- coding: utf-8 -*-
import os
from os.path import dirname, join

# from pyotp import TOTP
from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask import Flask, abort, jsonify, request, render_template
from flask_jwt import JWT, current_identity, jwt_required
from werkzeug.security import generate_password_hash
import datetime
import re

# Modules
from connection import *

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
load_dotenv(verbose=True)
app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET')
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

class User(object):
    def __init__(self, id, username, password, display_name):
        self.id = id
        self.username = username
        self.password = password
        self.display_name = display_name

    def __str__(self):
        return ["%s","%s","%s"] % (self.id, self.username, self.display_name)
jwt = JWT(app, authenticate, identity)

@app.route("/")
def root():
  return jsonify({"status":"403 Forbidden", "message":"メッセージはでないはずだよ"}), 403

# デバイス関連
# # データの登録
@app.route("/device/new", methods=["post"])
def post_user():
  module_id = request.json["module_id"]
  type = request.json["type"]
  value = request.json["value"]
  with conn.cursor() as cur:
    cur.execute("INSERT INTO users (module_id, type, value) VALUES (%s, %s, %s)", (module_id, type, int(value)))
  conn.commit()
  return jsonify({"message":"200 OK"}), 200

# Account
# # New Account

@app.route("/user/new", methods=["post"])
def new_user():
    username = request.json['username']
    email = request.json['email']
    password = request.json['userpw']
    display_name = request.json['display_name']
    password_hash = generate_password_hash(password, method='sha256')
    with conn.cursor() as cur:
        cur.execute('INSERT INTO users (username, email, password_digest, display_name) VALUES (%s, %s, %s, %s)', (username, email, password_hash, display_name))
    conn.commit()
    return jsonify({"message":"200 OK"}), 200


# # ユーザ更新
@app.route("/alter_user", methods=["put"])
@jwt_required()
def alter_user():
    username = request.json['username']
    email = request.json['email']
    password = request.json['userpw']
    display_name = request.json['display_name']
    password_hash = generate_password_hash(password, method='sha256')
    # 本人情報の取得
    with conn.cursor() as cur:
        cur.execute('SELECT id FROM users WHERE username = %s;', (username,))
        registeredid = cur.fetchall()
    # 本人情報の確認
    if str(current_identity[0]) == str(re.sub("\(|\,|\)", "", str(registeredid[0]))):
        with conn.cursor() as cur:
            cur.execute('UPDATE users SET username=%s, email=%s, password_digest=%s, display_name=%s WHERE username = %s', (username, email, password_hash, display_name, username))
        conn.commit()
        return jsonify({"message":"200 OK"}), 200
    else:
        return jsonify(
            {
                "message": "Forbidden"
            }), 403

if __name__ == "__main__":
  if os.environ.get("IS_DEBUG") == "True":
     app.run(debug=True, port=8888)
  else:
     app.run(debug=False, port=8888)