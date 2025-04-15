from flask import Blueprint, jsonify, make_response, current_app
from backend.db_connection.db import db_connection

analytics_blueprint = Blueprint('analytics', __name__)

@analytics_blueprint.route('/analytics', methods = ['GET'])
def get_analytics():
        connection = db_connection()
        cursor = connection.cursor(dictionary = True)
        cursor.execute("SELECT * FROM AppAnalytics")
        results = cursor.fetchall()

        cursor.close()
        connection.close()
        return make_response(jsonify(results), 200)


'''

from flask import Blueprint, jsonify
from db import db_connection

# blueprint instance
analytics_blueprint = Blueprint('analytics', __name__)

@analytics_blueprint.route('/analytics', methods = ['GET'])
def get_analytics():
    connection = db_connection()
    cursor = connection.cursor(dictionary = True)
    cursor.execute("SELECT * FROM AppAnalytics")
    results = cursor.fetchall()

    cursor.close()
    connection.close()
    return jsonify(results)
'''