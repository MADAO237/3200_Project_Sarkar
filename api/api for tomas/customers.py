from flask import Blueprint, jsonify
from db import db_connection

customers_blueprint = Blueprint('customers2', __name__)

# return high freq
@customers_blueprint.route('/customers/highFrequency', methods = ['GET'])
def get_loyal_customers():
    connection = db_connection()
    cursor = connection.cursor(dictionary = True)
    cursor.execute("""
        SELECT user_id, COUNT(*) FROM Orders GROUP BY user_id
        HAVING total_orders >= 3 ORDER BY total_orders DESC
    """)
    results = cursor.fetchall()

    cursor.close()
    connection.close()
    return jsonify(results)