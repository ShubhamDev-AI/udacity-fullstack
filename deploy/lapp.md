# Deploy LAPP

Linux Apache2 PostgreSQL Python

```sh
sudo mkdir /var/www/catalog
sudo mkdir /var/www/catalog/catalog
sudo mkdir /var/www/catalog/catalog/static
sudo mkdir /var/www/catalog/catalog/templates
```


```sh
sudo vim /var/www/catalog/catalog/__init__.py
```

```py
from flask import Flask
from db_setup import get_session

app = Flask(__name__)
session = get_session()

@app.route("/")
def hello():
    return "Hello, I love Digital Ocean!"

@app.route("/error")
def throw_error():
    raise Exception("Error thrown!")

@app.errorhandler(Exception)
def catch_errors(error):
    return error.description

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
```

```
sudo vim /etc/apache2/sites-available/000-default.conf
```

```apache
<VirtualHost *:80>
		# ServerName mywebsite.com
		ServerAdmin admin@mywebsite.com
		WSGIScriptAlias / /var/www/catalog/catalog.wsgi
		<Directory /var/www/catalog/catalog/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/catalog/catalog/static
		<Directory /var/www/catalog/catalog/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel info
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

```sh
sudo vim /var/www/catalog/catalog.wsgi
```

```py
#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/catalog/")

from catalog import app as application

application.secret_key = 'Add your secret key'
application.debug = True
```


```sh
sudo su postgres
psql
```

```sql
CREATE USER catalog WITH PASSWORD 'secret';
CREATE DATABASE catalog WITH OWNER catalog;
```

```sh
exit
```

```py
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key = True)
  name = Column(String(250), nullable = False)
  email = Column(String(250), nullable = False)
  picture = Column(String(250))

engine = create_engine('postgresql://catalog:secret@localhost:5432/catalog')
Base.metadata.create_all(engine)

def get_session():
    # Create session and connect to DB
    engine = create_engine('postgresql://catalog:secret@localhost:5432/catalog')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    return DBSession()

```