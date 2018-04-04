from database_setup import Base, Restaurant, MenuItem, User, get_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

session = get_session()

class RestaurantCRUD:

    def query(self):
        return session.query(Restaurant)

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
        session.add(model)
        session.commit()
        return

    def new(self):
        return Restaurant()

    def create(self, model):
        session.add(model)
        session.commit()
        return

    def delete(self, model):
        session.delete(model)
        session.commit()
        return


class MenuItemCRUD:

    def query(self):
        return session.query(MenuItem)

    def all(self):
        res = self.query() \
                .order_by(MenuItem.name) \
                .all()
        return res

    def forRestaurant(self, rest):
        res = self.query() \
                .filter(MenuItem.restaurant_id == rest.id) \
                .order_by(MenuItem.course) \
                .order_by(MenuItem.name) \
                .all()
        return res

    def find(self, id):
        res = self.query() \
                .filter(MenuItem.id == id) \
                .first()
        return res

    def update(self, model):
        session.add(model)
        session.commit()
        return

    def new(self, restaurant_id):
        return MenuItem(name="", price="$1.00", \
            description="", restaurant_id=restaurant_id, course="")

    def create(self, model):
        session.add(model)
        session.commit()
        return

    def delete(self, model):
        session.delete(model)
        session.commit()
        return


class UserCRUD:

    def query(self):
        return session.query(MenuItem)

    def new(self):
        return User(name='', email='')

    def create(self, model):
        session.add(model)
        session.commit()
        return

    def find(self, id):
        res = self.query() \
                .filter(User.id == id) \
                .first()
        return res

    def findByEmail(self, email):
        res = self.query() \
                .filter(User.email == email) \
                .first()
        return res