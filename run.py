from app import app, db
from app.models import User

@app.shell_context_processor
def get_context():
    return dict(User = User, app=app, db=db)