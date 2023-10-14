import mysql.connector
from flask import Flask, jsonify, request

app = Flask(__name__)

# Database connection function
def connect_to_database():
    connection = mysql.connector.connect(
        host="cis3368fall.c6xk1vtqaxor.us-east-1.rds.amazonaws.com",
        user="admin",
        password="Memo1999",
        database="cis3368finalproject"
    )
    return connection

# Route for the home page
@app.route('/')
def index():
    return "<h1>Senior Citizen Facility - Room Occupancy System</h1>"

if __name__ == '__main__':
    app.run(debug=True)
