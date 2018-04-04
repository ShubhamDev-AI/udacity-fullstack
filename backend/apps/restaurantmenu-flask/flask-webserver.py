from flask import Flask, render_template, redirect, request, url_for, flash, jsonify, make_response
from flask import session as login_session
from restaurantmenu import RestaurantCRUD, MenuItemCRUD, UserCRUD

from oauth2client.client import flow_from_clientsecrets, FlowExchangeError

import random, string, httplib2, json, requests

restCrud = RestaurantCRUD()
menuCrud = MenuItemCRUD()
userCrud = UserCRUD()

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('google_client_secrets.json', 'r').read())['web']['client_id']

# show login
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('auth_login.html', state=state, google_client_id=CLIENT_ID)

# submit oauth callback
@app.route('/google-oauth-callback', methods=['POST'])
def googleOAuthCallback():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('google_client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    # get or create the user
    user = userCrud.findByEmail(data['email'])
    if user == None:
        user = userCrud.new()
        user.email = data['email']
        user.name = data['name']
        user.picture = data['picture']
        userCrud.create(user)

    login_session['username'] = user.name
    login_session['picture'] = user.picture
    login_session['email'] = user.email
    login_session['user_id'] = user.id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print("done!")
    return output

# submit oauth logout
@app.route('/google-oauth-logout')
def googleOAuthLogout():
    access_token = login_session.get('access_token')
    if access_token is None:
        print('Access Token is None')
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print('In gdisconnect access token is %s', access_token)
    print('User name is: ')
    print(login_session['username'])
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print('result is ')
    print(result)
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response


# show restaurant index
@app.route('/')
@app.route('/restaurants')
def restaurantIndex():
    restaurants = restCrud.all()
    return render_template('restaurant_index.html', rests=restaurants)

# show|submit restaurant create form
@app.route('/')
@app.route('/restaurants/new', methods=['GET', 'POST'])
def createRestaurant():

    if 'username' not in login_session:
        return redirect(url_for('showLogin'))

    rest = restCrud.new()
    rest.name = ''

    if request.method == 'POST':
        rest.name = request.form['name']
        restCrud.create(rest)
        flash("Restaurant '%s' created" % rest.name)
        return redirect(url_for('restaurantDetail', r_id=rest.id))

    return render_template('restaurant_form.html', rest=rest, action='create')

# show|submit restaurant edit form
@app.route('/')
@app.route('/restaurants/<int:r_id>/edit', methods=['GET', 'POST'])
def editRestaurant(r_id):

    if 'username' not in login_session:
        return redirect(url_for('showLogin'))

    rest = restCrud.find(r_id)

    if request.method == 'POST':
        rest.name = request.form['name']
        restCrud.update(rest)
        flash("Restaurant '%s' updated" % rest.name)
        return redirect(url_for('restaurantDetail', r_id=rest.id))

    return render_template('restaurant_form.html', rest=rest, action='update')

# show|submit restaurant delete form
@app.route('/')
@app.route('/restaurants/<int:r_id>/delete', methods=['GET', 'POST'])
def deleteRestaurant(r_id):

    if 'username' not in login_session:
        return redirect(url_for('showLogin'))

    rest = restCrud.find(r_id)

    if request.method == 'POST':
        restCrud.delete(rest)
        flash("Restaurant '%s' delete" % rest.name)
        return redirect(url_for('restaurantIndex'))

    return render_template('restaurant_delete.html', rest=rest)

# show restaurant detail
@app.route('/restaurants/<int:r_id>')
def restaurantDetail(r_id):
    rest = restCrud.find(r_id)
    menuItems = menuCrud.forRestaurant(rest)
    return render_template('restaurant_detail.html', rest=rest, items=menuItems)

# create menu item form
@app.route('/restaurants/<int:r_id>/menu-items/new', methods=['GET', 'POST'])
def createMenuItem(r_id):

    if 'username' not in login_session:
        return redirect(url_for('showLogin'))

    rest = restCrud.find(r_id)
    item = menuCrud.new(r_id)

    if request.method == 'POST':
        item.name = request.form['name']
        item.price = request.form['price']
        item.description = request.form['description']
        item.course = request.form['course']
        menuCrud.create(item)
        flash("Menu Item '%s' created" % item.name)
        return redirect(url_for('restaurantDetail', r_id=r_id))

    return render_template('menuitem_form.html', rest=rest, item=item, action='create')

# edit menu item form
@app.route('/restaurants/<int:r_id>/menu-items/<int:m_id>/edit', methods=['GET', 'POST'])
def editMenuItem(r_id, m_id):

    if 'username' not in login_session:
        return redirect(url_for('showLogin'))

    rest = restCrud.find(r_id)
    item = menuCrud.find(m_id)

    if request.method == 'POST':
        item.name = request.form['name']
        item.price = request.form['price']
        item.description = request.form['description']
        item.course = request.form['course']
        menuCrud.update(item)
        flash("Menu Item '%s' updated" % item.name)
        return redirect(url_for('restaurantDetail', r_id=r_id))

    return render_template('menuitem_form.html', rest=rest, item=item, action='update')

# delete menu item form
@app.route('/restaurants/<int:r_id>/menu-items/<int:m_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(r_id, m_id):

    if 'username' not in login_session:
        return redirect(url_for('showLogin'))

    rest = restCrud.find(r_id)
    item = menuCrud.find(m_id)

    if request.method == 'POST':
        menuCrud.delete(item)
        flash("Menu Item '%s' deleted" % item.name)
        return redirect(url_for('restaurantDetail', r_id=r_id))

    return render_template('menuitem_delete.html', rest=rest, item=item)

# api - restaurant detail
@app.route('/api/restaurants/<int:r_id>')
def apiGetRestaurant(r_id):
    rest = restCrud.find(r_id)
    menuItems = menuCrud.forRestaurant(rest)
    return jsonify(MenuItems=[i.serialize for i in menuItems])


# api - menu item detail
@app.route('/api/restaurants/<int:r_id>/menu-items/<int:m_id>')
def apiGetMenuItem(r_id, m_id):
    rest = restCrud.find(r_id)
    menuItem = menuCrud.find(m_id)
    return jsonify(MenuItem=menuItem.serialize)


# User Helper Functions


def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


##### RUN APP #####
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)