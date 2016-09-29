#!/usr/bin/env python
from flask import Flask, request

app = Flask(__name__)

# Shared storage for our list of tasks
tasks = ["GenCS 1"]

form = ("<form action='/' method='POST'>"
        "<input autofocus type='text' name='task' />"
        "<input type='submit' />"
        "</form>")

def delete_form(idx):
    return ("<form action='/delete' method='POST'>"
                "<input type='hidden' name='task' value='" + str(idx) + "' />"
                "<input type='submit' value='Delete'/>"
                "</form>"
                )

def task_list():
    task_list = ["<li>" + task + delete_form(idx) + "</li>" for idx, task in enumerate(tasks)]

    return form + "<ul>" + "".join(task_list) + "</ul>"

@app.route("/",  methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        new_task = request.form['task']
        tasks.append(new_task)

    return task_list()

@app.route("/delete", methods=['POST'])
def delete():
    tasks.pop(int(request.form['task']))

    return task_list()


app.run()
