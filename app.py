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

# Modules
from connection import *

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
load_dotenv(verbose=True)
app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET')
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

class User(object):
    def __init__(self, id, username, password, namae):
        self.id = id
        self.username = username
        self.password = password
        self.namae = namae

    def __str__(self):
        return ["%s","%s","%s"] % (self.id, self.username, self.namae)
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
    useremail = request.json['useremail']
    password = request.json['userpw']
    namae = request.json['namae']
    password_hash = generate_password_hash(password, method='sha256')
    with conn.cursor() as cur:
        cur.execute("CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY, username varchar UNIQUE, useremail varchar UNIQUE, password_digest varchar, namae varchar);")
        cur.execute("CREATE TABLE IF NOT EXISTS questions (id serial PRIMARY KEY, subject varchar, description varchar, heading varchar, quiz text, answershet text, created_by integer, renew_rules integer, created_at timestamp, changed_at timestamp);")
        cur.execute('INSERT INTO users (username, useremail, password_digest, namae) VALUES (%s, %s, %s, %s)', (username, useremail, password_hash, namae))
    conn.commit()
    return jsonify({"message":"200 OK"}), 200

if __name__ == "__main__":
  if os.environ.get("IS_DEBUG") == "True":
     app.run(debug=True, port=8888)
  else:
     app.run(debug=False, port=8888)