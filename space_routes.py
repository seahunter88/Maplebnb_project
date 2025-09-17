from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository

def apply_space_routes(app):
    @app.route('/spaces', methods=['GET'])
    def show_spaces():
        connection = get_flask_database_connection(app)
        repo = SpaceRepository(connection)
        spaces = repo.read_all_spaces()
        return render_template('spaces/show_spaces.html', spaces = spaces)

    @app.route('/spaces/<int:space_id>', methods=['GET'])
    def show_one_space(space_id):
        connection = get_flask_database_connection(app)
        repo = SpaceRepository(connection)
        space = repo.read_one_space(space_id)
        return render_template('spaces/show_one_space.html', space = space)