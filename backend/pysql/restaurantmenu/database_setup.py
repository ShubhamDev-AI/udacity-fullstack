import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


### class declarations ###

class Restaurant(Base):
  __tablename__ = 'restaurant'
  id = Column(Integer, primary_key = True)
  name = Column(String(80), nullable = False)

class MenuItem(Base):
  __tablename__ = 'menu_items'
  id = Column(Integer, primary_key = True)
  name = Column(String(80), nullable = False)
  course = Column(String(250))
  description = Column(String(250))
  price = Column(String(8))
  restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
  restaurant = relationship(Restaurant)



### configuration create db ###

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
