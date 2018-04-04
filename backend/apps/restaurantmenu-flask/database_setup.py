import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


### class declarations ###

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key = True)
  name = Column(String(250), nullable = False)
  email = Column(String(250), nullable = False)
  picture = Column(String(250))


class Restaurant(Base):
  __tablename__ = 'restaurants'
  id = Column(Integer, primary_key = True)
  name = Column(String(80), nullable = False)
  user_id = Column(Integer, ForeignKey('users.id'))
  user = relationship(User)


class MenuItem(Base):
  __tablename__ = 'menu_items'
  id = Column(Integer, primary_key = True)
  name = Column(String(80), nullable = False)
  course = Column(String(250))
  description = Column(String(250))
  price = Column(String(8))
  restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
  restaurant = relationship(Restaurant)
  user_id = Column(Integer, ForeignKey('users.id'))
  user = relationship(User)

  @property
  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'description': self.description,
      'price': self.price,
      'course': self.course,
    }



### configuration create db ###

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)

def get_session():
    # Create session and connect to DB
    engine = create_engine('sqlite:///restaurantmenu.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    return DBSession()
