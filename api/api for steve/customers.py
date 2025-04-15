from flask import Blueprint, jsonify, request


# Blueprint instance
customers_blueprint = Blueprint('customers', __name__)

# 建立数据库连接(connect to MySQL server)
def db_connection():
    return mysql.connector.connect(
    	# name in docker
        host='',         
        user='',
        password='',
        database=''
    )

# get all customers: GET /customers 
@customers_blueprint.route('/customers', methods = ['GET'])
def get_all_customers():
    connection = db_connection()
    cursor = connection.cursor(dictionary = True)
    cursor.execute("SELECT * FROM Customers")
    results = cursor.fetchall()

    cursor.close()
    connection.close()
    return jsonify(results)

# search for customer: GET /customers/search?name=xxx&email=xxx 
@customers_blueprint.route('/customers/search', methods = ['GET'])
def search_customers():
    name = request.args.get('name')
    email = request.args.get('email')
    connection = get_db_connection()
    cursor = connection.cursor(dictionary = True)
    cursor.execute("SELECT * FROM Customers WHERE firstname LIKE %s OR email LIKE %s",
                   (f"%{name}%", f"%{email}%"))
    results = cursor.fetchall()

    cursor.close()
    connection.close()
    return jsonify(results)

# add a new customer: POST /customers 
@customers_blueprint.route('/customers', methods = ['POST'])
def add_customer():
    data = request.get_json()
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Customers (firstname, lastname, email, address) VALUES (%s, %s, %s, %s)",
                   (data['firstname'], data['lastname'], data['email'], data['address']))
    connection.commit()

    cursor.close()
    connection.close()
    return jsonify({'message': 'Customer added successfully'}), 201

# delete a customer: DELETE /customers/<id> → 
@customers_bp.route('/customers/<int:user_id>', methods = ['DELETE'])
def delete_customer(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Customers WHERE user_id = %s", (user_id,))
    connection.commit()

    cursor.close()
    connection.close()
    return jsonify({'message': f'Customer {user_id} deleted'}), 200

# update customer fields: PUT /customers/<id> →
@customers_bp.route('/customers/<int:user_id>', methods = ['PUT'])
def update_customer(user_id):
    data = request.get_json()
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE Customers SET firstname = %s, lastname = %s, email = %s, address = %s WHERE user_id = %s",
                   (data['firstname'], data['lastname'], data['email'], data['address'], user_id))
    connection.commit()
    
    cursor.close()
    connection.close()
    return jsonify({'message': f'Customer {user_id} updated'}), 200
