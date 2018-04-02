from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from restaurantmenu import RestaurantCRUD
from html import \
    HTML_LAYOUT, \
    HTML_RESTAURANT_INDEX, \
    HTML_RESTAURANT_CREATE, \
    HTML_RESTAURANT_EDIT, \
    HTML_RESTAURANT_DELETE, \
    HTML_COMP_RESTAURANT_ITEM

import cgi

crud = RestaurantCRUD()

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        parts = self.path.split('/')

        # /
        if len(parts) == 1 and parts[0] == '/':
            self.send_response(302)
            self.send_header('Location', '/restaurants')
            self.end_headers()
            self.wfile.write("Redirecting...".encode())
            return

        # /restaurants
        if len(parts) == 2 and parts[1] == 'restaurants':

            items = ""
            restaurants = crud.all()
            for r in restaurants:
                items += HTML_COMP_RESTAURANT_ITEM.format(name=r.name, id=r.id)

            content = HTML_RESTAURANT_INDEX.format(items=items)
            body = HTML_LAYOUT.format(title="Restaurants", content=content)

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(body.encode())
            return

        # /restaurants/new
        if len(parts) == 3 and parts[1] == 'restaurants' and parts[2] == 'new':

            content = HTML_RESTAURANT_CREATE.format(name='')
            body = HTML_LAYOUT.format(title="Add Restaurant", content=content)

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(body.encode())
            return

        # /restaurants/{id}/edit
        if len(parts) == 4 and parts[1] == 'restaurants' and parts[3] == 'edit':

            r = crud.find(parts[2])

            if(r == None):
                self.send_error(404, 'Restaurant not found: %s' % parts[2])
                return

            content = HTML_RESTAURANT_EDIT.format(name=r.name, id=r.id)
            body = HTML_LAYOUT.format(title="Edit Restaurant", content=content)

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(body.encode())
            return

        # /restaurants/{id}/delete
        if len(parts) == 4 and parts[1] == 'restaurants' and parts[3] == 'delete':

            r = crud.find(parts[2])

            if(r == None):
                self.send_error(404, 'Restaurant not found: %s' % parts[2])
                return

            content = HTML_RESTAURANT_DELETE.format(name=r.name, id=r.id)
            body = HTML_LAYOUT.format(title="Edit Restaurant", content=content)

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(body.encode())
            return

        self.send_error(404, 'File Not Found: %s' % self.path)


    def do_POST(self):
        parts = self.path.split('/')
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        postvars = cgi.parse_multipart(self.rfile, pdict)

        # /restaurants/new
        if len(parts) == 3 and parts[1] == 'restaurants' and parts[2] == 'new':
            try:
                name = postvars.get('name')[0]
                r = crud.new()
                r.name = name
                crud.create(r)

                self.send_response(302)
                self.send_header('Location', '/restaurants')
                self.end_headers()
                self.wfile.write("Created!".encode())
            except (AttributeError, IndexError) as e:
                self.send_error(400, 'Invalid form data: %s' % str(e))
            return

        # /restaurants/{id}/edit
        if len(parts) == 4 and parts[1] == 'restaurants' and parts[3] == 'edit':
            try:
                id = parts[2]
                name = postvars.get('name')[0]

                r = crud.find(id)

                if(r == None):
                    self.send_error(404, 'Restaurant not found: %s' % parts[2])
                    return

                r.name = name
                crud.update(r)

                self.send_response(302)
                self.send_header('Location', '/restaurants')
                self.end_headers()
                self.wfile.write("Updated!".encode())
            except (AttributeError, IndexError) as e:
                self.send_error(400, 'Invalid form data: %s' % str(e))
            return

        # /restaurants/{id}/delete
        if len(parts) == 4 and parts[1] == 'restaurants' and parts[3] == 'delete':
            try:
                id = parts[2]
                r = crud.find(id)

                if(r == None):
                    self.send_error(404, 'Restaurant not found: %s' % parts[2])
                    return

                crud.delete(r)

                self.send_response(302)
                self.send_header('Location', '/restaurants')
                self.end_headers()
                self.wfile.write("Deleted!".encode())
            except (AttributeError, IndexError) as e:
                self.send_error(400, 'Invalid form data: %s' % str(e))
            return



        self.send_error(404, 'File Not Found: %s' % self.path)


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print("Webserver running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt as e:
        print("^C interrupt, stopping server...")
        server.socket.close()


if __name__ == '__main__':
    main()