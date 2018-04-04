# `flask`

 - [Quickstart](http://flask.pocoo.org/docs/0.12/quickstart/)
 - [Request and Response Objects](http://werkzeug.pocoo.org/docs/0.14/wrappers/)


## Setup App

```py
from flask import Flask
app = Flask(__name__)       # base app instance
```

## Run App

```py
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'     # encrypt key for sessions
    app.debug = True                        # turn on debugging
    app.run(host = '0.0.0.0', port = 5000)  # run webserver
```

## Routes

`@app.route('/some-url')`

### Params

Route paths may specify parameters to pass to the route method:

`@app.route('/some-url/<[converter:]var_name>')`
```py
@app.route('/item/<int:id>')
def getItem(id)
    ...
```

Converters:
 - `string` accepts any text without a slash (the default)
 - `int` accepts integers
 - `float` like int but for floating point values
 - `path` like the default but also accepts slashes
 - `any` matches one of the items provided
 - `uuid` accepts UUID strings

### Methods

Routes by default only respond to `GET` requests. To modify the accepted methods, add a `methods` param:

`@app.route('/item/<int:id>', methods=['GET', 'POST'])`


### Make Urls

Create urls for routes referencing by the route method name:

`url_for(method_name, params)`

```py
url = url_for('getItem', id=some_id)
```

### Request Data

The data in the request body, url query string and headers are accessed with the global `request` object.

```py
from flask import request
```

`request` attributes:
 - `path` (string) - the request path, eg. `/items/12`
 - `method` (string) - the request method, eg. `POST`
 - `form` (dict) - data in the request body. Throws `KeyError`
 - `args` (ImmutableMultiDict) - data in the query string


## Response

### Render Templates

### Redirect

### Static Files


## Auth