from flask import Blueprint, jsonify
from backend.db_connection import db

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



from flask import Blueprint, request, jsonify
from backend.db_connection import db

orders = Blueprint('orders', __name__)

@orders.route('/pickup_time', methods=['POST'])
def add_pickup_time():
    data = request.get_json()
    conn = db.connect()
    cursor = conn.cursor()
    try:
        query = """
        INSERT INTO orders (pickup_time)
        VALUES (%s)
        """
        cursor.execute(query, (data['pickup_time'],))
        conn.commit()
        return jsonify({'message': 'Pickup time added'}), 201
    finally:
        cursor.close()
        conn.close()

@orders.route('/delivery_time', methods=['POST'])
def add_delivery_time():
    data = request.get_json()
    conn = db.connect()
    cursor = conn.cursor()
    try:
        query = """
        UPDATE orders
        SET delivery_time = %s
        WHERE order_id = %s
        """
        cursor.execute(query, (data['delivery_time'], data['order_id']))
        conn.commit()
        return jsonify({'message': 'Delivery time updated'}), 200
    finally:
        cursor.close()
        conn.close()
        
@orders.route('/delivery_location', methods=['POST'])
def add_delivery_location():
    data = request.get_json()
    conn = db.connect()
    cursor = conn.cursor()
    try:
        query = """
        UPDATE orders
        SET delivery_location = %s
        WHERE order_id = %s
        """
        cursor.execute(query, (data['delivery_location'], data['order_id']))
        conn.commit()
        return jsonify({'message': 'Delivery location updated'}), 200
    finally:
        cursor.close()
        conn.close()

@orders.route('/orderdetails/<int:order_id>', methods=['GET'])
def get_order_details(order_id):
    conn = db.connect()
    cursor = conn.cursor()
    try:
        query = "SELECT * FROM orders WHERE order_id = %s"
        cursor.execute(query, (order_id,))
        result = cursor.fetchone()
        if result:
            return jsonify(result)
        return jsonify({'error': 'Order not found'}), 404
    finally:
        cursor.close()
        conn.close()

@orders.route('/<int:order_id>/update_cost', methods=['PUT'])
def update_order_cost(order_id):
    data = request.get_json()
    conn = db.connect()
    cursor = conn.cursor()
    try:
        query = """
        UPDATE orders
        SET total_cost = %s
        WHERE order_id = %s
        """
        cursor.execute(query, (data['total_cost'], order_id))
        conn.commit()
        return jsonify({'message': 'Total cost updated'})
    finally:
        cursor.close()
        conn.close()
        
@orders.route('/<int:order_id>/status', methods=['GET'])
def get_order_status(order_id):
    conn = db.connect()
    cursor = conn.cursor()
    try:
        query = "SELECT status FROM orders WHERE order_id = %s"
        cursor.execute(query, (order_id,))
        result = cursor.fetchone()
        if result:
            return jsonify({'order_id': order_id, 'status': result['status']})
        return jsonify({'error': 'Order not found'}), 404
    finally:
        cursor.close()
        conn.close()



