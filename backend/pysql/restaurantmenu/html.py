
HTML_LAYOUT = '''<!DOCTYPE html>
<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        {content}
    </body>
</html>
'''

HTML_RESTAURANT_INDEX = '''
<h1>Restaurants</h1>
<ul>{items}</ul>
<a href="/restaurants/new">Add Restaurant</a>
'''

HTML_RESTAURANT_MENU = '''
<h1>{name}</h1>
<ul>{items}</ul>
<a href="/restaurants/new">Add Menu Item</a>
'''

HTML_RESTAURANT_EDIT = '''
<h1>Edit Restaurant {id}</h1>
<form method="POST" action="/restaurants/{id}/edit" enctype="multipart/form-data">
    <label>Name: <input type="text" name="name" value="{name}"></label>
    <button type="submit">Update</button>
</form>
'''

HTML_RESTAURANT_CREATE = '''
<h1>Add Restaurant</h1>
<form method="POST" action="/restaurants/new" enctype="multipart/form-data">
    <label>Name: <input type="text" name="name" value="{name}"></label>
    <button type="submit">Create</button>
</form>
'''

HTML_RESTAURANT_DELETE = '''
<h1>Delete Restaurant {id}?</h1>
<form method="POST" action="/restaurants/{id}/delete" enctype="multipart/form-data">
    <p>Are you sure you want to delete '{name}'?</p>
    <button type="submit">Delete</button>
</form>
'''

HTML_COMP_RESTAURANT_ITEM = '''
<li>
    {name}
    <a href="/restaurants/{id}">Menu</a>
    <a href="/restaurants/{id}/edit">Edit</a>
    <a href="/restaurants/{id}/delete">Delete</a>
</li>
'''

HTML_COMP_MENU_ITEM = '''
<li>
    <strong>{name}</strong> {price}<br>
    {description}<br>
    <a href="/restaurants/{r_id}/menu-items/{m_id}/edit">Edit</a>
    <a href="/restaurants/{r_id}/menu-items/{m_id}/delete">Delete</a>
</li>
'''