from flask import Flask
from backend.db_connection import db
from backend.laundromat.laundromat_routes import laundromat
from backend.orders.orders_routes import orders


# 000000 test for analysis by MQ
from backend.analytics.analytics_routes import analytics_blueprint

import os
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)

    # Load environment variables
    # This function reads all the values from inside
    # the .env file (in the parent folder) so they
    # are available in this file.  See the MySQL setup 
    # commands below to see how they're being used.
    load_dotenv()

    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    # app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # # these are for the DB object to be able to connect to MySQL. 
    # app.config['MYSQL_DATABASE_USER'] = 'root'
    # app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USER').strip()
    app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_ROOT_PASSWORD').strip()
    app.config['MYSQL_DATABASE_HOST'] = os.getenv('DB_HOST').strip()
    app.config['MYSQL_DATABASE_PORT'] = int(os.getenv('DB_PORT').strip())
    app.config['MYSQL_DATABASE_DB'] = os.getenv('DB_NAME').strip()  # Change this to your DB name

    # Initialize the database object with the settings above. 
    app.logger.info('current_app(): starting the database connection')
    db.init_app(app)


    # Register the routes from each Blueprint with the app object
    # and give a url prefix to each
    app.register_blueprint(laundromat, url_prefix='/l')
    app.register_blueprint(orders, url_prefix='/orders')
    
    @app.route('/test', methods=['GET'])
    def test():
        return "API is running!"


    # 000000 test for analysis by MQ
    app.register_blueprint(analytics_blueprint, url_prefix='/analytics')

    # TEST 4000 by MQ delete later
    @app.route("/")
    def index():
        return {"message": "test message for flask port 4000"}

    # Don't forget to return the app object
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port = 4000)
