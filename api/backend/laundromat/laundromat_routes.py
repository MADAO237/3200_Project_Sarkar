from flask import Blueprint, request, jsonify
from backend.db_connection import db

laundromat = Blueprint('laundromat', __name__)

@laundromat.route('/laundromat', methods=['GET'])
def get_sorted_laundromats():
    attribute = request.args.get('attribute', 'pricing')
    sort_order = request.args.get('sort', 'asc')
    limit = int(request.args.get('limit', 1))
    
    if attribute not in ['pricing', 'avgtime', 'time_process']:
        return jsonify({'error': 'Invalid attribute'}), 400
 
    sort_order = sort_order.lower()
    if sort_order not in ['asc', 'desc']:
        return jsonify({'error': 'Invalid sort order'}), 400
    
    conn = db.connect()
    cursor = conn.cursor()
    
    try:
        query = f"SELECT * FROM laundromats ORDER BY {attribute} {sort_order.upper()} LIMIT %s"
        cursor.execute(query, (limit,))
        results = cursor.fetchall()
        return jsonify(results)
    finally:
        cursor.close()
        conn.close()
        
