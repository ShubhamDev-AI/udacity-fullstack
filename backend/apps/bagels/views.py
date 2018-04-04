from models import Base, User, Bagel
from flask import Flask, jsonify, request, url_for, abort, g
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from flask.ext.httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


engine = create_engine('sqlite:///bagelShop.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    user = session.query(User) \
            .filter(User.username == username) \
            .first()
    if not user or not user.verifyPassword(password):
        return False
    g.user = user
    return True


@app.route('/users', methods = ['GET','POST'])
def usersEndpoint():
    if request.method == 'POST':
        username = request.json.get('username')
        password = request.json.get('password')
        if username is None or password is None:
            abort(400)
        existing = session.query(User) \
                        .filter(User.username == username) \
                        .first()
        if existing is not None:
            abort(400)
        user = User(username=username)
        user.setPassword(password)
        session.add(user)
        session.commit()
        return jsonify(user.serialize), 201




@app.route('/bagels', methods = ['GET','POST'])
@auth.login_required
def showAllBagels():
    if request.method == 'GET':
        bagels = session.query(Bagel).all()
        return jsonify(bagels = [bagel.serialize for bagel in bagels])
    elif request.method == 'POST':
        name = request.json.get('name')
        description = request.json.get('description')
        picture = request.json.get('picture')
        price = request.json.get('price')
        newBagel = Bagel(name = name, description = description, picture = picture, price = price)
        session.add(newBagel)
        session.commit()
        return jsonify(newBagel.serialize)



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)