from database_setup import Base, Restaurant, MenuItem
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class RestaurantCRUD:

    def __init__(self):
        # Create session and connect to DB
        engine = create_engine('sqlite:///restaurantmenu.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def query(self):
        return self.session.query(Restaurant)

    def all(self):
        res = self.query() \
                .order_by(Restaurant.name) \
                .all()
        return res

    def find(self, id):
        res = self.query() \
                .filter(Restaurant.id == id) \
                .first()
        return res

    def update(self, model):
        self.session.add(model)
        self.session.commit()
        return

    def delete(self, model):
        self.session.delete(model)
        self.session.commit()
        return
