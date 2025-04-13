from flask import Blueprint, jsonify
from db import db_connection

logs_blueprint = Blueprint('logs', __name__)

@logs_blueprint.route('/logs', methods = ['GET'])
def get_logs():
    connection = db_connection()
    cursor = connection.cursor(dictionary = True)
    cursor.execute("SELECT * FROM Logs")
    results = cursor.fetchall()

    cursor.close()
    connection.close()
    return jsonify(results)