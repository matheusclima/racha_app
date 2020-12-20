from passlib.hash import sha256_crypt
from racha_app.repositories.user_repository import UserRepository
from flask import Blueprint, render_template, redirect, url_for, request, session

import gc

app = Blueprint('login_blueprint', __name__)

@app.route('/login', methods = ['GET', 'POST'])
def login_page():

    error = ''

    if request.method == "POST":    
        
        attempted_username = request.form['username']
        user = UserRepository().find_by_username(attempted_username)
        
        if user is None:
            error = 'Usuário ou senha inválidas'
        else:    
            password = user.password
            attempted_password = request.form['password']
            if sha256_crypt.verify(attempted_password, password):

                session["logged_in"] = True
                session['username'] = request.form['username']
                return redirect(url_for('artilharia'))
            else:
                error = 'Usuário ou senha inválidas'

    return render_template('login.html', is_true = True, error = error)

@app.route('/logout')
def logout():
    session.clear()
    gc.collect()
    return redirect(url_for('login_blueprint.login_page'))           
