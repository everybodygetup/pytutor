from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security

db = SQLAlchemy()
migrate = Migrate()
security = Security()
