from flask_script import Manager
from tcas import create_tcas
from tcas.db import initialize_model
from tcas.db import reset_model

application = create_tcas()
manager = Manager(application)


@manager.command
def run():
    """Run application.

    """
    application.run(debug=True)


@manager.command
def test():
    """Run application.

    """
    application.run(debug=True)


@manager.command
def reboot():
    """Reset and reboot application."""
    reset()
    initialize()


@manager.command
def initialize():
    """Initialize database."""
    initialize_model()


@manager.command
def reset():
    """Reset database."""
    reset_model()


if __name__ == '__main__':
    manager.run()
