from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
customers = Blueprint('CustomerReviews', __name__)


#------------------------------------------------------------
# Retrieve all customer reviews for a laundromat
@customers.route('/CustomerReviews/<laundromat_id>', methods=['GET'])
def get_customer_reviews(laundromat_id):
    cursor = db.get_db().cursor()
    query = '''
        SELECT review_id, laundromat_id, user_id, rating, text, title
        FROM CustomerReviews
        WHERE laundromat_id = %s
    '''
    cursor.execute(query, (laundromat_id,))
    reviews = cursor.fetchall()
    the_response = make_response(jsonify(reviews))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Make a user review for a laundromat
@customers.route('/CustomerReviews/<review_id>', methods=['POST'])
def create_review(review_id):
    data = request.json()
    current_app.logger.info(data)


    laundromat_id = data.get('laundromat_id')
    review_id = data.get('review_id')
    user_id = data.get('user_id')
    rating = data.get('rating')
    text = data.get('text')
    title = data.get('title') 

    cursor = db.get_db().cursor()
    new_rev_query = f'''
        INSERT INTO customer_reviews (review_id, laundromat_id, user_id, rating, comment, date)
        VALUES ('{review_id}', '{laundromat_id}', '{user_id}', '{rating}', '{text}', {title}')
    '''
    cursor.execute(new_rev_query, (review_id, laundromat_id, user_id, rating, text, title))
    db.get_db().commit()

    return make_response(jsonify({'message': 'Review created successfully'}), 201)