from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# make a database session

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# add new restaurant entry

restaurant = Restaurant(name = "Pizza Palace")
session.add(restaurant)
session.commit()

# query all restaurants

restaurants = session.query(Restaurant).all()