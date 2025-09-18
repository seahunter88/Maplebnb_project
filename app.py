import os
from flask import Flask, request, render_template, redirect
from user_routes import apply_user_routes
from space_routes import apply_space_routes
from booking_routes import apply_booking_routes

app = Flask(__name__)

@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

apply_user_routes(app)
apply_space_routes(app)
apply_booking_routes(app)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))