#!/usr/bin/env python
"""Create a new admin user able to view the /reports endpoint."""
from getpass import getpass
import sys

from flask import current_app
from app import create_app
from app.models import User, db
from werkzeug.security import generate_password_hash

from func import cfg

# app = create_app(os.getenv("FLASK_ENV") or "config.DevelopementConfig")
app = create_app(cfg.get("FLASK_ENV", "config.DevelopementConfig"))


def main():
    """Main entry point for script."""
    with app.app_context():
        db.metadata.create_all(db.engine)
        if User.query.all():
            print("A user already exists! Create another? (y/n):")
            create = input()
            if create == "n":
                return

        print("Enter username: ")
        username = input()
        print("Enter email address: ")
        email = input()
        password = getpass()
        assert password == getpass("Password (again):")

        user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password),
        )
        db.session.add(user)
        db.session.commit()
        print("User added.")


if __name__ == "__main__":
    sys.exit(main())
