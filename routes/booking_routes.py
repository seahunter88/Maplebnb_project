from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.bookings.booking_repository import BookingRepository
from lib.bookings.booking import Booking
from time import sleep
from lib.spaces.space_repository import SpaceRepository
from lib.users.user_repository import UserRepository
    

def apply_booking_routes(app):
    @app.route('/create_booking', methods= ["GET"])
    def get_create_booking():
        return render_template('bookings/create_booking.html')
    
    @app.route('/spaces/<int:space_id>', methods = ['POST'])
    def post_create_booking(space_id):
        connection = get_flask_database_connection(app)
        space_repo = SpaceRepository(connection)
        booking_repo = BookingRepository(connection)
        
        space = space_repo.read_one_space(space_id)
        bookings = booking_repo.read_bookings_one_space(space_id)
        
        booking_date = request.form['booking_date']
        booking_user_id = request.form['booking_user_id']
        booking = Booking(None, booking_date, space_id, booking_user_id)
        
        if not booking.is_valid():
            date_errors = booking.generate_errors()
            return render_template('spaces/show_one_space.html', date_errors = date_errors, bookings = bookings, space = space)
        
        if not booking_repo.check_booking_is_unique(booking) or not booking_repo.check_user_id_exists(booking):
            errors = booking_repo.generate_errors(booking)
            return render_template('spaces/show_one_space.html', errors=errors, bookings=bookings, space=space)
        
        booking_repo.create(booking)
        # the redirect uses the URL from @get_booking_confirmation
        # the booking_date parameter is from the form submitted 
        # the space_title parameter is from the Space object returned from read_one_space
        return redirect(url_for('get_booking_confirmation', booking_date = booking_date, space_title = space.title, booking_user_id=booking_user_id))

    @app.route('/booking_confirmation', methods= ["GET"])
    def get_booking_confirmation():
        booking_date = request.args.get('booking_date')
        space_title = request.args.get('space_title')
        booking_user_id = request.args.get('booking_user_id')
        return render_template('bookings/booking_confirmation.html', booking_date = booking_date, space_title = space_title, booking_user_id=booking_user_id)

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
