# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, url_for, request, session
from racha_app.login_required import login_required
from racha_app.models.jogador import Jogador
from passlib.hash import sha256_crypt
from flask_migrate import Migrate
# from dbcon import connect
from datetime import date
from racha_app.db import db

# import pandas as pd
# import numpy as np
import psycopg2
# import secrets
import gc

app = Flask(__name__)

app.config.from_pyfile('config/config.py')
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/login', methods = ['GET', 'POST'])
def login_page():

    error = ''
    try:
        cursor, conn = connect('db_parameters.json')

        if request.method == "POST":
            
            attempted_username = request.form['username']

            select_user = ("SELECT username, password FROM users WHERE username = %s")
            cursor.execute(select_user, (attempted_username,))

            password = cursor.fetchone()[1]
            attempted_password = request.form['password']

            cursor.close()
            conn.close()
            
            if sha256_crypt.verify(attempted_password, password):

                session["logged_in"] = True
                session['username'] = request.form['username']
                return redirect(url_for('artilharia'))
            else:
                error = 'Login Inválido'

        return render_template('login.html', is_true = True, error = error)

    except Exception as e:
        return render_template('login.html', is_true = True, error = error)

@app.route('/logout')
def logout():
    session.clear()
    gc.collect()
    return redirect(url_for('login_page'))           

@app.route('/artilharia')
# @login_required
def artilharia():
    return render_template('index.html', is_true = True)

@app.route('/cu', methods = ["GET", "POST"])
# @login_required
def colocacao():
    
    cursor, conn = connect('db_parameters.json')
    select_players = ("SELECT nome FROM players")

    today = date.today().strftime("%Y-%m-%d")
    cursor.execute(select_players)
    players = list(list(zip(*cursor.fetchall()))[0])
    
    if request.method == "POST":

        day = request.form["date"]
        
        stats = request.form.getlist("stats")
        stats = [stats[x:x+7] for x in range(0,len(stats),7)]

        df = pd.DataFrame(stats, columns = ["Jogador", "Jogo 1", "Jogo 2", "Jogo 3", "Jogo 4", "Jogo 5", "Jogo 6"])
        a, b, c, d = np.array_split(df, 4)
        print(a)
        return render_template("result.html", is_true = True, a = a, b = b, c = c, d = d)
        
    return render_template("team_match.html", is_true = True, today = today, players = players)

@app.route('/', methods = ["GET", "POST"])
def new_player():
    jogador = Jogador('Veras')
    db.session.add(jogador)
    db.session.commit()

    cursor, conn = connect('racha_app/db_parameters.json')
    select_players = ("SELECT nome FROM players")

    cursor.execute(select_players)
    players = list(list(zip(*cursor.fetchall()))[0])
    
    if request.method == "POST":
        
        player_name = request.form["player_name"]
        host_name = request.form["host_name"]

        insert_player = ("INSERT INTO players (nome, host) VALUES (%s, %s)")
        val = (player_name, host_name)

        cursor.execute(insert_player, val)
        conn.commit()        


    return render_template("new_player.html", is_true = True, players = players)

if __name__ == "__main__":
    app.run(debug=True)
