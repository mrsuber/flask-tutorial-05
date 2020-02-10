# Enable Debugging in development
DEBUG = True


# Application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'transaction_service.db')
SQLALCHEMY_DATABASE_URI = 'mysql://flaskfirstprogram:flaskfirstprogram@flask_mysql_server/flaskfirstprogram'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
