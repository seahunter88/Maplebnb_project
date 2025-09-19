from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.booking_repository import BookingRepository
from lib.booking import Booking
from time import sleep
from lib.space_repository import SpaceRepository
from lib.user_repository import UserRepository
    

def apply_booking_routes(app):
    @app.route('/create_booking', methods= ["GET"])
    def get_create_booking():
        return render_template('bookings/create_booking.html')
    
    @app.route('/spaces/<int:space_id>', methods = ['POST'])
    def post_create_booking(space_id):
        connection = get_flask_database_connection(app)
        space_repo = SpaceRepository(connection)
        space = space_repo.read_one_space(space_id)
        booking_repo = BookingRepository(connection)
        bookings = booking_repo.read_bookings_one_space(space_id)
        booking_date = request.form['booking_date']
        booking_user_id = request.form['booking_user_id']
        booking = Booking(None, booking_date, space_id, booking_user_id)
        if not booking_repo.check_booking_is_unique(booking):
            errors = booking_repo.generate_errors(booking)
            return render_template('spaces/show_one_space.html', errors=errors, bookings=bookings, space=space)
        booking_repo.create(booking)
        return redirect('/booking_confirmation')

    @app.route('/booking_confirmation', methods= ["GET"])
    def get_booking_confirmation():
        return render_template('bookings/booking_confirmation.html')

    @app.route('/my_bookings/<int:booking_user_id>', methods= ["GET"])
    def get_my_bookings(booking_user_id):
        connection = get_flask_database_connection(app)
        
        user_repo = UserRepository(connection)
        booking_repo = BookingRepository(connection)
        space_repo = SpaceRepository(connection)
        
        user = user_repo.read_one_user(booking_user_id)
        
        # we get all the bookings associated with one user
        bookings = booking_repo.read_bookings_one_user(booking_user_id)
        
        # we iterate over the bookings list generated
        # the variable space becomes a Space object that is returned based on each booking's space id
        # each booking in the booking list then gets a new attribute called space_title
        # this attribute is the title of the space object created in the first line
        for booking in bookings:
            space = space_repo.read_one_space(booking.space_id)
            booking.space_title = space.title
        
        return render_template('bookings/my_bookings.html', bookings = bookings, user = user)
    
    @app.route('/welcome', methods = ['POST'])
    def post_my_bookings():
        user_id = request.form['user_id']
        return redirect(f'/my_bookings/{user_id}')
