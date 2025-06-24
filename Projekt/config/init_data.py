from models.models import db, Ship

def init_data(app):
    with app.app_context():
        db.create_all()

        # if Ship.query.first() is None:
        #     new_ship = Ship(length=1)
        #     db.session.add(new_ship)
        #     db.session.commit()