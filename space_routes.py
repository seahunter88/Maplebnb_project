from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.space import Space
from lib.booking_repository import BookingRepository

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
        space_repo = SpaceRepository(connection)
        space = space_repo.read_one_space(space_id)
        booking_repo = BookingRepository(connection)
        bookings = booking_repo.read_bookings_one_space(space_id)
        return render_template('spaces/show_one_space.html', space = space, bookings = bookings)
    
    @app.route('/spaces/new', methods=['POST'])
    def create_a_space():
        connection = get_flask_database_connection(app)
        repo = SpaceRepository(connection)
        title = request.form['title']
        price = int(request.form['price'])
        description = request.form['description']
        user_id = request.form['user_id']
        space = Space(None, title, price, description, user_id)
        if not space.is_valid():
            errors = space.generate_errors()
            return render_template('spaces/new_space.html', errors=errors)
        repo.create_space(space)
        return redirect('/spaces')
    
    @app.route('/spaces/new')
    def create_space():
        return render_template('spaces/new_space.html')