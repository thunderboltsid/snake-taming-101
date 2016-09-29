#!/usr/bin/env python
from flask import Flask, request

app = Flask(__name__)

# Shared storage for our list of tasks
tasks = ["GenCS 1"]

form = ("<form action='/' method='POST'>"
        "<input autofocus type='text' name='task' />"
        "<input type='submit' />"
        "</form>")

@app.route("/",  methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        new_task = request.form['task']
        tasks.append(new_task)

    task_list = ["<li>" + task + "</li>" for task in tasks]

    return form + "<ul>" + "".join(task_list) + "</ul>"


app.run()
