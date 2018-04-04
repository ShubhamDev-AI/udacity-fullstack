from flask import Flask, render_template, redirect, request, url_for, flash, jsonify
from restaurantmenu import RestaurantCRUD, MenuItemCRUD

restCrud = RestaurantCRUD()
menuCrud = MenuItemCRUD()

app = Flask(__name__)

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
    rest = restCrud.find(r_id)

    if request.method == 'POST':
        restCrud.delete(rest)
        flash("Restaurant '%s' delete" % rest.name)
        return redirect(url_for('restaurantIndex'))

    return render_template('restaurant_delete.html', rest=rest)

# showrestaurant detail
@app.route('/restaurants/<int:r_id>')
def restaurantDetail(r_id):
    rest = restCrud.find(r_id)
    menuItems = menuCrud.forRestaurant(rest)
    return render_template('restaurant_detail.html', rest=rest, items=menuItems)

# create menu item form
@app.route('/restaurants/<int:r_id>/menu-items/new', methods=['GET', 'POST'])
def createMenuItem(r_id):
    rest = restCrud.find(r_id)
    item = menuCrud.new(r_id)

    if request.method == 'POST':
        item.name = request.form['name']
        item.price = request.form['price']
        item.description = request.form['description']
        menuCrud.create(item)
        flash("Menu Item '%s' created" % item.name)
        return redirect(url_for('restaurantDetail', r_id=r_id))

    return render_template('menuitem_form.html', rest=rest, item=item, action='create')

# edit menu item form
@app.route('/restaurants/<int:r_id>/menu-items/<int:m_id>/edit', methods=['GET', 'POST'])
def editMenuItem(r_id, m_id):
    rest = restCrud.find(r_id)
    item = menuCrud.find(m_id)

    if request.method == 'POST':
        item.name = request.form['name']
        item.price = request.form['price']
        item.description = request.form['description']
        menuCrud.update(item)
        flash("Menu Item '%s' updated" % item.name)
        return redirect(url_for('restaurantDetail', r_id=r_id))

    return render_template('menuitem_form.html', rest=rest, item=item, action='update')

# delete menu item form
@app.route('/restaurants/<int:r_id>/menu-items/<int:m_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(r_id, m_id):
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



##### RUN APP #####
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)