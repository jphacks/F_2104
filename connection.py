# -*- coding: utf-8 -*-
from dotenv import load_dotenv
from os.path import join, dirname
import os
import psycopg2

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Connect to PostgreSQL
def get_connection():
    dsn = os.environ.get('DATABASE_URL')
    return psycopg2.connect(dsn)
conn = get_connection()
cur = conn.cursor()