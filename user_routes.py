import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User
from lib.space_repository import SpaceRepository
from lib.space import Space\

def apply_user_routes(app):
    @app.route('/signup', methods = ['POST'])
    def create_user():
        connection = get_flask_database_connection(app)
        repo = UserRepository(connection)
        username = request.form['username']
        password = request.form['password']
        user = User(None, username, password)
        if not user.is_valid():
            errors = user.generate_errors()
            return render_template('users/signup.html', errors=errors)
        repo.create(user)
        return redirect('/welcome')

    @app.route('/welcome')
    def welcome_user():
        return render_template('users/welcome.html')

    @app.route('/signup')
    def signup_user():
        return render_template('users/signup.html')
    
    
    @app.route('/signin', methods = ['POST'])
    def signin_user():
        connection = get_flask_database_connection(app)
        repo = UserRepository(connection)
        username = request.form['username']
        password = request.form['password']
        user = User(None, username, password)
        if not user.is_valid():
            errors = user.generate_errors()
            return render_template('users/signup.html', errors=errors)
        repo.find(user)
        return redirect('/welcome')
    