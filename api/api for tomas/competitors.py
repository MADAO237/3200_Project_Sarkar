from flask import Blueprint, jsonify

competitors_blueprint = Blueprint('competitors', __name__)

@competitors_blueprint.route('/competitors/nearbyLaundry', methods=['GET'])
def get_nearby_competitors():
    mock_competitors_data = [
        {
            "name": "Mock Laundry 1",
            "location": "Boston",
            "rating": 3.5,
            "estimated_customers": 100
        },

        {
            "name": "Mock Laundry 2",
            "location": "Boston",
            "rating": 4.0,
            "estimated_customers": 20
        },

        {
            "name": "Mock Laundry 3",
            "location": "Malden",
            "rating": 4.5,
            "estimated_customers": 120
        }
    ]
    return jsonify(competitors_data)