#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

messages = []


class MessageHandler(BaseHTTPRequestHandler):

    html = """
        <!DOCTYPE html>
        <title>Message Board</title>
        <form method="POST" action="http://localhost:8000/">
            <textarea name="message"></textarea>
            <br>
            <button type="submit">Post it!</button>
        </form>
        <p>Last message: {message}</p>
    """

    def do_POST(self):
        # 1. How long was the message? (Use the Content-Length header.)
        length = int(self.headers.get('Content-length', 0))

        # 2. Read the correct amount of data from the request.
        data = self.rfile.read(length).decode()

        # 3. Extract the "message" field from the request data.
        requestData = parse_qs(data)

        message = requestData['message'][0]
        message = message.replace("<", "&lt;")

        messages.append(message)

        # Send the "message" field back as the response.
        self.send_response(303)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.send_header('Location', '/')
        self.end_headers()
        self.wfile.write("Redirecting...".encode())

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(MessageHandler.html.format(message=', '.join(messages)).encode())



if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
