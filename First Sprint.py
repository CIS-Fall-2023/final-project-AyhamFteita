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

# Route for getting all floors
@app.route('/api/floors', methods=['GET'])
def get_all_floors():
    connection = connect_to_database()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM floor")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    if result:
        return jsonify({"message": "All floors retrieved successfully.",
                         "floors": result})
    else:
        return jsonify({"message": "No floors found."})

# Route for adding a new floor
@app.route('/api/floors', methods=['POST'])
def add_floor():
    data = request.json
    conn = connect_to_database()
    cursor = conn.cursor()

    insert_query = "INSERT INTO floor (level, name) VALUES (%s, %s)"
    cursor.execute(insert_query, (data["level"], data["name"]))

    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Floor added!"}), 201

# Route for updating a floor
@app.route('/api/floors/<int:floor_id>', methods=['PUT'])
def update_floor(floor_id):
    data = request.json
    conn = connect_to_database()
    cursor = conn.cursor()

    update_query = "UPDATE floor SET level=%s, name=%s WHERE id=%s"
    cursor.execute(update_query, (data["level"], data["name"], floor_id))

    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Floor updated!"})

# Route for deleting a floor
@app.route('/api/floors/<int:floor_id>', methods=['DELETE'])
def delete_floor(floor_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    delete_query = "DELETE FROM floor WHERE id = %s"
    cursor.execute(delete_query, (floor_id,))

    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        return jsonify({"error": "No Floor found"}), 404

    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Floor deleted!"}), 200

# Route for getting all rooms
@app.route('/api/rooms', methods=['GET'])
def get_all_rooms():
    connection = connect_to_database()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM room")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(result)

# Route for adding a new room
@app.route('/api/rooms', methods=['POST'])
def add_room():
    data = request.json
    conn = connect_to_database()
    cursor = conn.cursor()

    insert_query = "INSERT INTO room (capacity, number, floor_id) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (data["capacity"], data["number"], data["floor_id"]))

    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Room added!"}), 201

# Route for updating a room
@app.route('/api/rooms/<int:room_id>', methods=['PUT'])
def update_room(room_id):
    data = request.json
    conn = connect_to_database()
    cursor = conn.cursor()

    update_query = "UPDATE room SET capacity=%s, number=%s, floor_id=%s WHERE id=%s"
    cursor.execute(update_query, (data["capacity"], data["number"], data["floor_id"], room_id))

    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Room updated!"})

# Route for deleting a room
@app.route('/api/rooms/<int:room_id>', methods=['DELETE'])
def delete_room(room_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    delete_query = "DELETE FROM room WHERE id = %s"
    cursor.execute(delete_query, (room_id,))

    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        return jsonify({"error": "No Room found"}), 404

    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Room deleted!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
