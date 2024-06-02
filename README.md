# onecommune

Concept of One Commune
One Commune is envisioned as a platform to connect users within a geographical vicinity, fostering local community interactions. The application allows users to join a community based on their location, discover nearby users, connect with them, and communicate through a simple chat interface.

Features of One Commune
1. User Location Submission
Input Form: Users input their geographical coordinates (latitude and longitude).
Data Handling: The coordinates are captured and sent to the server for processing.
2. Storing and Displaying Nearby Users
User List: The server maintains an in-memory list of user coordinates.
Distance Calculation: Using Geopy, the application calculates the distance between users to determine proximity.
Nearby Users Display: Users within a 10km radius are displayed on the Nearby Users page.
3. Connecting with Nearby Users
Connection Page: Users can select a nearby user to connect with.
User Information: Displays the selected user’s location for context.
4. Chat Functionality
Messaging: Users can send and receive messages with other users.
Message Storage: Messages are temporarily stored in an in-memory list for simplicity.
Chat Interface: The chat interface displays the message history for the conversation.
Detailed Technical Workflow
Home Page (index.html)
Functionality: Collects user location via a form.
Flow: On submission, data is sent to /submit_location.
Submit Location Endpoint (/submit_location)
Data Processing: Receives and processes user-submitted location.
User List Update: Adds the new location to the user list.
Redirection: Redirects to the Nearby Users page with the user's location as a parameter.
Nearby Users Page (/nearby_users)
Location Extraction: Extracts the user's location from the query parameters.
Proximity Calculation: Uses Geopy to find users within a 10km radius.
Display: Renders a list of nearby users with "Connect" buttons.
Connect Page (/connect/<latitude>/<longitude>)
User Connection: Displays selected user's location and offers a "Chat Now" button.
Navigation: Allows navigation back to Nearby Users or the Home page.
Chat Page (/chat/<latitude>/<longitude>)
Message Form: Provides a form for users to send messages.
Message Handling: Stores messages and displays the message history related to the conversation.
Implementation Details
Flask Framework: Handles routing, form submission, and rendering HTML templates.
Geopy Library: Calculates distances between user locations.
HTML Templates: Uses Jinja2 templating engine for dynamic content rendering.
