from flask import Blueprint, jsonify, request
from db import db_connection

analytics_blueprint = Blueprint('analytics', __name__)

# get all kip
@analytics_blueprint.route('/analytics/kpi', methods = ['GET'])
def get_kpi_data():
    connection = db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM AppAnalytics")
    results = cursor.fetchall()

    cursor.close()
    connection.close()
    return jsonify(results)

# promos
@analytics_blueprint.route('/orders/promotions', methods = ['GET'])
def get_promotion_summary():
    promo = request.args.get('code')
    connection = db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT promo_code, COUNT(*), SUM(total_cost) FROM Orders WHERE promo_code = %s
        GROUP BY promo_code
        """, (promo, ))
    results = cursor.fetchall()

    cursor.close()
    connection.close()
    return jsonify(results)