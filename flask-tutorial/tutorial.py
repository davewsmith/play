from app import (
    app,
    db,
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
        # 'app' ia automatic
        'db': db,
        'User': User,
        'Note': Note,
    }
