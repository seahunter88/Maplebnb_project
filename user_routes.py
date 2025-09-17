from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User

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
    def find_user():
        connection = get_flask_database_connection(app)
        repo = UserRepository(connection)

        username = request.form['username']
        password = request.form['password']
        user = User(None, username, password)

        if not user.is_valid():
            errors = user.generate_errors()
            return render_template('users/signin.html', errors=errors)

        db_user = repo.find(username, password)

        if db_user is None:
            user_not_found = 'An account with those details is not found.'
            return render_template('users/signin.html', user_not_found=user_not_found)

        return redirect('/welcome')

    @app.route('/signin')
    def signin_user():
        return render_template('users/signin.html')


