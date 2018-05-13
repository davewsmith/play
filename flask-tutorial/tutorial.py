from app import (
    app,
    db,
    mail,
)
from app.models import (
    User,
    Note,
)


@app.shell_context_processor
def make_shell_context():
    """
    Exports for `flask shell`
    """
    return {
        # 'app' is exported for free
        'db': db,
        'mail': mail,
        'User': User,
        'Note': Note,
    }
