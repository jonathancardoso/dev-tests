from flask import Flask, render_template, request, url_for, flash, redirect, session, abort
import os
import controller

#env variables
UPLOAD_FOLDER = './uploads'

app = Flask('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect('/uploader')
        #return 'Hello Boss!  <a href="/logout">Logout</a>'

@app.route('/login', methods=['POST'])
def do_admin_login():
    user = request.form['username']
    password = request.form['password']
    if controller.auth(user,password):
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return redirect('/')

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if not session.get('logged_in'):
        return home()

    if request.method == 'GET':
        return redirect('/uploader')

    else:
        return controller.upload(request)


@app.route('/uploader', methods=['GET'])
def upload_file():
    if not session.get('logged_in'):
        return home()

    return render_template('uploader.html')

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run()
