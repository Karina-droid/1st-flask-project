from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
@app.route('/form', methods=["POST", "GET"])
def render_form():
    if request.method == 'POST':
        return greeting(request.form['fname'])
    else:
        return render_template('form.html')


def greeting(name):
    return render_template('hello.html', name=name)