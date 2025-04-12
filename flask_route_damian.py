from flask import request, jsonify
from app import app, db
from models import Orders, OrderDetails

@app.route('/orders/<int:order_id>/pickup_time', methods=['POST'])
def update_pickup_time(order_id):
    new_time = request.json.get('pickup_time')
    order = Orders.query.get(order_id)
    order.pickup_time = new_time
    db.session.commit()
    return jsonify({'message': 'Pickup time updated'})

@app.route('/orders/<int:order_id>/delivery_time', methods=['POST'])
def update_delivery_time(order_id):
    new_time = request.json.get('delivery_time')
    order = Orders.query.get(order_id)
    order.delivery_time = new_time
    db.session.commit()
    return jsonify({'message': 'Delivery time updated'})

@app.route('/orders/<int:order_id>/delivery_location', methods=['POST'])
def update_delivery_location(order_id):
    new_location = request.json.get('delivery_location')
    order = Orders.query.get(order_id)
    order.delivery_location = new_location
    db.session.commit()
    return jsonify({'message': 'Deliery location updated'})

@app.route('/OrderDetails/<int:order_id>', methods=['GET'])
def get_order_details(order_id):
    details = OrderDetails.query.filter_by(order_id=order_id).all()
    return jsonify([d.serialize() for d in details])

@app.route('/Orders/<int:order_id>/cost', methods=['PUT'])
def update_total_cost(order_id):
    new_cost = request.json.get('total_cost')
    order = Orders.query.get(order_id)
    order.total_cost = new_cost
    db.session.commit()
    return jsonify({'message': 'Order cost updated'})

@app.route('/Orders/<int:order_id>/<int:status>', methods=['GET'])
def get_order_status(order_id, status):
    order = Orders.query.get(order_id)
    if order.status == status:
        return jsonify({'order_id': order_id, 'status': 'Completed' if status else 'Pending'})
    return jsonify({'message': 'Status mismatch'}), 404

def serialize(self):
    return {column.name: getattr(self, column.name) for column in self.__table__.columns}



