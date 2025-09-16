import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User
from lib.space_repository import SpaceRepository
from lib.space import Space

"ANYTHING ON LINE 5"

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/spaces', methods=['GET'])
def show_spaces():
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    spaces = repo.read_all_spaces()
    return render_template('show_spaces.html', spaces = spaces)

@app.route('/signup', methods = ['POST'])
def create_user():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    id = request.form['id']
    username = request.form['username']
    password = request.form['password']
    user = User(id, username, password)
    repo.create(user)
    




# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
