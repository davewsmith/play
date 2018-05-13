from app import (
    # cli,
    create_app,
    db,
)
from app.models import (
    User,
    Note,
)

app = create_app()
# cli.register(app)


@app.shell_context_processor
def make_shell_context():
    """
    Exports for `flask shell`
    """
    return {
        # 'app' is exported for free
        'db': db,
        'mail': mail,
        'Note': Note,
    }
