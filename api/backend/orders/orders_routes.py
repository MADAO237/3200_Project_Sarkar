from flask import Blueprint, jsonify
from backend.db_connection import db_connection

orders_blueprint = Blueprint('orders', __name__)

@orders_blueprint.route('/orders', methods = ['GET'])
def get_orders():
    connection = db_connection()
    cursor = connection.cursor(dictionary = True)
    cursor.execute("SELECT * FROM Orders")
    results = cursor.fetchall()

    cursor.close()
    connection.close()
    return jsonify(results)