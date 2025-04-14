from flask import Blueprint, jsonify
from db import db_connection

orders_blueprint = Blueprint('orders', __name__)

# orders per day
@orders_blueprint.route('/orders/by-day', methods = ['GET'])
def get_orders_by_day():
    connection = db_connection()
    cursor = connection.cursor(dictionary = True)
    cursor.execute("""
        SELECT DATE(order_date) AS day, COUNT(*), SUM(total_cost) FROM OrderDetails
        JOIN Orders ON Orders.order_id = OrderDetails.order_id GROUP BY day ORDER BY day
    """)
    results = cursor.fetchall()

    cursor.close()
    connection.close()
    return jsonify(results)

# orders by location
@orders_blueprint.route('/orders/by-location', methods = ['GET'])
def get_orders_by_location():
    connection = db_connection()
    cursor = connection.cursor(dictionary = True)
    cursor.execute("""
        SELECT delivery_location, COUNT(*), SUM(total_cost) FROM Orders GROUP BY location 
        ORDER BY order_count DESC
    """)
    results = cursor.fetchall()

    cursor.close()
    connection.close()
    return jsonify(results)