from flask import Flask, request, jsonify, render_template, redirect, url_for
import geopy.distance

app = Flask(__name__)

# In-memory storage for user locations with sample data and messages
users = [
    (40.7128, -74.0060),  # New York
    (34.0522, -118.2437), # Los Angeles
    (41.8781, -87.6298),  # Chicago
    (29.7604, -95.3698),  # Houston
    (33.4484, -112.0740)  # Phoenix
]

# In-memory storage for messages
messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_location', methods=['POST'])
def submit_location():
    location = request.form['location']
    latitude, longitude = map(float, location.split(','))
    users.append((latitude, longitude))
    return redirect(url_for('show_nearby_users', location=location))

@app.route('/nearby_users')
def show_nearby_users():
    location = request.args.get('location')
    if not location:
        return "Location not provided", 400

    latitude, longitude = map(float, location.split(','))
    current_location = (latitude, longitude)

    # Find users within 10km radius
    nearby = [user for user in users if geopy.distance.distance(current_location, user).km <= 10]
    
    return render_template('nearby_users.html', users=nearby, current_location=current_location)

@app.route('/connect/<latitude>/<longitude>')
def connect(latitude, longitude):
    return render_template('connect.html', location=(latitude, longitude))

@app.route('/chat/<latitude>/<longitude>', methods=['GET', 'POST'])
def chat(latitude, longitude):
    if request.method == 'POST':
        message = request.form['message']
        messages.append({'location': (latitude, longitude), 'message': message})
    chat_messages = [msg for msg in messages if msg['location'] == (latitude, longitude)]
    return render_template('chat.html', location=(latitude, longitude), messages=chat_messages)

@app.route('/api/nearby_users', methods=['GET'])
def api_nearby_users():
    if 'location' not in request.args:
        return jsonify(users)  # Return all users if location is not provided

    location = request.args['location']
    latitude, longitude = map(float, location.split(','))
    current_location = (latitude, longitude)

    # Find users within 10km radius
    nearby = [user for user in users if geopy.distance.distance(current_location, user).km <= 10]
    
    return jsonify(nearby)

if __name__ == '__main__':
    app.run(debug=True)
