#!/usr/bin/env python 3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route("/")
def home():