from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.booking_repository import BookingRepository
from lib.booking import Booking
    

def apply_booking_routes(app):
    @app.route('/create_booking', methods= ["GET"])
    def get_create_booking():
        return render_template('bookings/create_booking.html')
    
    @app.route('/create_booking', methods = ['POST'])
    def post_create_booking():
        connection = get_flask_database_connection(app)
        repo = BookingRepository(connection)
        booking_date = request.form['booking_date']
        space_id = request.form['space_id']
        booking_user_id = request.form['booking_user_id']
        booking = Booking(None, booking_date, space_id, booking_user_id)
        # if not user.is_valid():
        #     errors = user.generate_errors()
        #     return render_template('users/signup.html', errors=errors)
        repo.create(booking)
        return redirect('/booking_confirmation')

    @app.route('/booking_confirmation', methods= ["GET"])
    def get_booking_confirmation():
        return render_template('bookings/booking_confirmation.html')
