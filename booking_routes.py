from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.booking_repository import BookingRepository
from lib.booking import Booking
from time import sleep
from lib.space_repository import SpaceRepository
    

def apply_booking_routes(app):
    @app.route('/create_booking', methods= ["GET"])
    def get_create_booking():
        return render_template('bookings/create_booking.html')
    
    @app.route('/spaces/<int:space_id>', methods = ['POST'])
    def post_create_booking(space_id):
        connection = get_flask_database_connection(app)
        booking_repo = BookingRepository(connection)
        booking_date = request.form['booking_date']
        booking_user_id = request.form['booking_user_id']
        booking = Booking(None, booking_date, space_id, booking_user_id)
        # if not user.is_valid():
        #     errors = user.generate_errors()
        #     return render_template('users/signup.html', errors=errors)
        booking_repo.create(booking)
        # return render_template('/spaces/show_one_space.html', space = space) 
            # and sleep(3) \
        return redirect('/booking_confirmation')

    @app.route('/booking_confirmation', methods= ["GET"])
    def get_booking_confirmation():
        return render_template('bookings/booking_confirmation.html')
