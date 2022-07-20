from flask_babel import Babel
from flask_mailman import Mail
from flask_executor import Executor
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security

mail = Mail()
babel = Babel()
executor = Executor()
db = SQLAlchemy()
migrate = Migrate()
security = Security()
