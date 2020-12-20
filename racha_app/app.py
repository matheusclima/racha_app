# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, url_for, request, session
from racha_app.controllers.login import app as login_app
from racha_app.login_required import login_required
from racha_app.models.player import Player
from racha_app.models.goal import Goal  
from flask_migrate import Migrate
from racha_app.db import db
from datetime import date
from racha_app.repositories.player_repository import PlayerRepository
from racha_app.repositories.goal_repository import GoalRepository
from racha_app.models.match import Match
from racha_app.models.team import Team
from racha_app.models.tournament import Tournament
from racha_app.repositories.tournament_repository import TournamentRepository

import numpy as np
import pandas as pd
import psycopg2
import secrets
import datetime

app = Flask(__name__)

app.config.from_pyfile('config/config.py')
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(login_app)

# Add new players to database
@app.route('/s', methods = ["GET"])
def render_new_player_page():
    return render_template("new_player.html")

@app.route('/s', methods = ["POST"])
def create_player():
    player = Player(request.form["player_name"])
    PlayerRepository.add(player)
    return redirect(url_for("new_player"))



# Select players for each team
@app.route('/', methods = ["GET", "POST"])
# @login_required
def new_tournament():
    
    today = date.today().strftime("%Y-%m-%d")

    if request.method == "POST":
        TournamentRepository.add(Tournament(request.form["day"]))
        tournament = db.session.query(Tournament).filter_by(date = today).first()
        return redirect(url_for("select_team", id = tournament.id))

    return render_template("new_tournament.html", today = today)


@app.route('/tournament/<id>', methods = ["GET", "POST"])
# @login_required
def select_team(id):
    
    players = [player.name for player in PlayerRepository.select_all(Player)]
    day = TournamentRepository.get_date(Tournament, id)
    print(day)
    if request.method == "POST":
        a = request.form.getlist("A")
        print(a)
        team_A = Team(0, "A")
        
        team_A.players.append(PlayerRepository.select(Player, a[0]))
        team_A.players.append(PlayerRepository.select(Player, a[1]))
        
        db.session.add(team_A)
        db.session.commit()


        return render_template("select_team.html", is_true = True, players = players)
        

        
    return render_template("select_team.html", is_true = True, players = players)


@app.route('/test', methods = ["GET", "POST"])
def matches():
    # a = request.args.get('a', None)
    # b = request.args.get('b', None)
    

    return render_template("matches.html", is_true = True)
 
if __name__ == "__main__":
    app.run(debug=True)
