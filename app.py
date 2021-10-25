# -*- coding: utf-8 -*-
import os
from os.path import dirname, join

# from pyotp import TOTP
from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask import Flask, abort, jsonify, request, render_template
import datetime

# Modules
from connection import *

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

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


if __name__ == "__main__":
  if os.environ.get("IS_DEBUG") == "True":
     app.run(debug=True, port=8888)
  else:
     app.run(debug=False, port=8888)