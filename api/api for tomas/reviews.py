from flask import Blueprint, jsonify
from db import db_connection

reviews_blueprint = Blueprint('reviews', __name__)

# return the rating
@reviews_blueprint.route('/reviews/summary', methods = ['GET'])
def get_review_summary():
    connection = db_connection()
    cursor = connection.cursor(dictionary = True)

    cursor.execute("SELECT AVG(rating) FROM CustomerReviews")
    avg_rating = cursor.fetchone()

    cursor.close()
    connection.close()

    return jsonify({
        "avg_rating": avg_rating['avg_rating']
    })