Chat Application Project

Overview

Our objective is to create a versatile WebSocket Chat Application that enables users to communicate in real-time. The system should facilitate a seamless user experience by supporting a wide array of operations, including joining chat rooms, sending messages, and handling users. To achieve this goal, we will implement a diverse set of functionalities using WebSocket technology and JavaScript programming techniques.

Project Requirements

WebSocket Setup and Configuration
Implement WebSocket connections in the chat application.
Understand the concept of bi-directional, full-duplex communication.
Configure WebSocket server and client to establish communication channels.
Implement CORS (Cross-Origin Resource Sharing) to allow communication with front-end applications.
Implementing WebSocket Events and Handlers
Implement connection, message, and disconnection events.
Understand WebSocket event handling and how it differs from traditional HTTP request-response cycles.
Handle WebSocket events to manage user interactions in the chat application.
Creating a Chat Room
Design and implement a chat room feature where users can join and participate in conversations.
Broadcast a message to everyone in the room when a user joins the chat room.
Create join_room.html to create a room and join to enter the chat.
Real-Time Messaging and Broadcasting
Implement real-time messaging between users in the chat room.
Implement features like message deletion and editing to enhance user experience.
Broadcast messages to all users in the chat room when a new message is sent.
GitHub Repository
Create a GitHub repository for the project and commit code regularly.
Maintain a clean and interactive README.md file in the GitHub repository, providing clear instructions on how to run the application and explanations of its features.
Include a link to the GitHub repository in the project documentation.
Submission

Upon completing the project, submit your code and video, including all source code files, and the README.md file in your GitHub repository to your instructor or designated platform.

Project Tips

WebSocket Events and Handlers
Use WebSocket events like onopen, onmessage, and onclose to manage user connections and disconnections.
Chat Room Management
Create a data structure to store active chat rooms and their participants.
Real-Time Messaging
Use WebSocket's real-time capabilities to send and receive messages instantly.
GitHub Repository and Version Control
Repository Management: Establish a GitHub repository for your project and commit code regularly. Utilize version control to keep track of changes and collaborate effectively with team members if applicable.
README.md: Maintain a clean and interactive README.md file in your GitHub repository. Provide clear instructions on how to run the application and explanations of its features. Include a link to your GitHub repository in your project documentation.
Running the Application

Prerequisites
Python 3.x
Flask
Flask-SocketIO
Flask-CORS
Installation
Clone the repository:

sh
Copy code
git clone https://github.com/Winter-Krimmert/Chat_Application_Project
cd chat-app
Install the required packages:

sh
Copy code
pip install -r requirements.txt
Running the Server
Start the Flask server:

sh
Copy code
python app.py
Open your web browser and navigate to http://127.0.0.1:5000.

Usage
Join Room: Navigate to http://127.0.0.1:5000 and create or join a chat room.
Chat Room: Once in a chat room, you can send, edit, and delete messages.
Features
Real-time messaging with WebSocket
Join and leave chat rooms
Edit and delete messages
System notifications for user join and leave events
GitHub Repository

Chat Application GitHub Repository