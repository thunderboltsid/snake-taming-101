#!/usr/bin/env python
from flask import Flask, request

app = Flask(__name__)

# Shared storage for our list of tasks
tasks = ["GenCS 1"]

@app.route("/")
def home():
    task_list = ["<li>" + task + "</li>" for task in tasks]

    return "<ul>" + "".join(task_list) + "</ul>"


app.run()
