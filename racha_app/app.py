# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, url_for, request, session, jsonify
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
from racha_app.repositories.team_repository import TeamRepository
from racha_app.repositories.match_repository import MatchRepository

import secrets
import datetime
import uuid


app = Flask(__name__)

app.config.from_pyfile('config/config.py')
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(login_app)

# Add new players to database
@app.route('/s', methods = ['GET'])
def render_new_player_page():
    return render_template('new_player.html')

@app.route('/s', methods = ['POST'])
def create_player():
    player = Player(request.form['player_name'])
    PlayerRepository.save(player)
    return redirect(url_for('render_new_player_page'))


# Create a tournament and add to database
@app.route('/', methods = ['GET'])
# @login_required
def render_tournament_page():
    today = date.today().strftime('%Y-%m-%d')
    return render_template('new_tournament.html', today = today)

@app.route('/', methods = ['POST'])
# @login_required
def create_new_tournament():    
    tournament = Tournament(request.form['day'])
    TournamentRepository.save(tournament)
    return redirect(url_for('render_team_page', tournament_id = tournament.id))


@app.route('/tournament/<tournament_id>', methods = ['GET'])
# @login_required
def render_team_page(tournament_id):
    players = PlayerRepository.select_all()
    return render_template(
            'select_team.html',
            players = players,
            tournament_id = tournament_id
        )

@app.route('/tournament/<tournament_id>/teams', methods = ['POST'])
# @login_required
def create_team(tournament_id):
    teams_letters = ['A', 'B', 'C', 'D']
    players = PlayerRepository.select_all()

    for letter in teams_letters:
        players_id = request.form.getlist(letter)
        
        team = Team(letter = letter, tournament_id = tournament_id)
        
        for id in players_id:
            player = next(x for x in players if str(x.id) == id )
            team.players.append(player)
    
        TeamRepository.save(team)

    return redirect(url_for('render_match_page', tournament_id = tournament_id))

@app.route('/tournament/<tournament_id>/matches', methods = ['GET'])
def render_match_page(tournament_id):
    teams = TeamRepository.select_all(tournament_id)
    teamsObject = {}
    for team in teams:
        teamsObject[team.letter] = {
            'players': [
                    {
                        'name': player.name,
                        'id': player.id
                    } for player in team.players
                ],
            'id': team.id
        }

    return render_template('matches.html', teams = teamsObject, tournament_id = tournament_id)

@app.route('/tournament/<tournament_id>/matches/post', methods = ['POST'])
def create_match(tournament_id):

    matchObject = request.get_json()
    home = matchObject['home']
    away = matchObject['away']
    match = Match(home['id'], away['id'], home['goals'], away['goals'], tournament_id)
    MatchRepository.save(match)
    match.assign_points()
    TeamRepository.save(match.home)
    TeamRepository.save(match.away)
    return redirect(url_for('render_match_page', tournament_id = tournament_id))

@app.route('/tournament/<tournament_id>/results', methods = ['GET'])
def show_tournament(tournament_id):

    tournament = TournamentRepository.select(tournament_id)
    teams = tournament.teams
    teams.sort(key = lambda team: team.points, reverse = True)
    print(teams[0].points)
    print(teams[0])

    
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
