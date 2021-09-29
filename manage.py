import os
from app import db, create_app
from app.models import User, myBudj, myBudj_spr_cat, myBudj_sub_cat

# , Post, Tag, Category, Employee, Feedback
# from flask_script import Manager, Shell

from flask_migrate import Migrate

# from flask.ext.migrate import Migrate,MigrateCommand
from func import cfg

# app = create_app(os.getenv("FLASK_ENV") or "config.DevelopementConfig")
app = create_app(cfg.get("FLASK_ENV", "config.DevelopementConfig"))
# manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(
        app=app,
        db=db,
        User=User,
        myBudj=myBudj,
        myBudj_spr_cat=myBudj_spr_cat,
        myBudj_sub_cat=myBudj_sub_cat
        # Post=Post,
        # Tag=Tag,
        # Category=Category,
        # Employee=Employee,
        # Feedback=Feedback,
    )


# manager.add_command("shell", Shell(make_context=make_shell_context))
# manager.add_command("db")

if __name__ == "__main__":
    app.run()
