from flask import Blueprint, jsonify, request


# 创建 Blueprint 实例
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

# GET /customers 获取所有用户
@customers_blueprint.route('/customers', methods = ['GET'])
def get_all_customers():
    connection = db_connection()
    cursor = connection.cursor(dictionary = True)
    cursor.execute("SELECT * FROM Customers")
    results = cursor.fetchall()

    cursor.close()
    connection.close()
    return jsonify(results)

# GET /customers/search?name=xxx&email=xxx 搜索用户
@customers_blueprint.route('/customers/search', methods = ['GET'])
def search_customers():
    name = request.args.get('name')
    email = request.args.get('email')
    connection = get_db_connection()
    cursor = connection.cursor(dictionary = True)
    SQLuery = "SELECT * FROM Customers WHERE firstname LIKE %s OR email LIKE %s"
    cursor.execute(SQLuery, (f"%{name}%", f"%{email}%"))
    results = cursor.fetchall()

    cursor.close()
    connection.close()
    return jsonify(results)

# POST /customers 添加新用户
@customers_blueprint.route('/customers', methods = ['POST'])
def add_customer():
    data = request.get_json()
    connection = get_db_connection()
    cursor = connection.cursor()

    SQLquery = "INSERT INTO Customers (firstname, lastname, email, address) VALUES (%s, %s, %s, %s)"
    cursor.execute(SQLquery, (data['firstname'], data['lastname'], data['email'], data['address']))
    connection.commit()

    cursor.close()
    connection.close()
    return jsonify({'message': 'Customer added successfully'}), 201

# DELETE /customers/<id> → 删除用户
@customers_bp.route('/customers/<int:user_id>', methods = ['DELETE'])
def delete_customer(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Customers WHERE user_id = %s", (user_id,))
    connection.commit()

    cursor.close()
    connection.close()
    return jsonify({'message': f'Customer {user_id} deleted'}), 200

# PUT /customers/<id> → 更新用户信息（自定义字段）
@customers_bp.route('/customers/<int:user_id>', methods = ['PUT'])
def update_customer(user_id):
    data = request.get_json()
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "UPDATE Customers SET firstname = %s, lastname = %s, email = %s, address = %s WHERE user_id = %s"
    cursor.execute(query, (data['firstname'], data['lastname'], data['email'], data['address'], user_id))
    connection.commit()
    
    cursor.close()
    connection.close()
    return jsonify({'message': f'Customer {user_id} updated'}), 200
