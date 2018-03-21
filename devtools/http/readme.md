# HTTP


```
__________                 __________
|        | === request ==> |        |
| Client |                 | Server |
|________| <== response == |________|


```



## Server Quickstart

Pyhon demo server:

```
python -m http.server 8000
```

Ncat TCP server:
```
nact -l 127.0.0.1 8080
```


## URI (Uniform Resource Identifier)

Example:

```

https://en.wikipedia.org/wiki/Hydrogen_chloride#Chemistry?key=value

```
 - `https` is the **scheme**. See the [full list](http://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml)
 - `en.wikipedia.org` is the **hostname**
 - `/wiki/Hydrogen_chloride` is the **path**
 - `Chemistry` is the **fragment**
 - `?key=value` **query parameters**


## Hostname

*The Internet tells computers apart by their IP addresses; every piece of network traffic on the Internet is labeled with the IP addresses of the sending and receiving computers. In order to connect to a web server such as www.udacity.com, a client needs to translate the hostname into an IP address. Your operating system's network configuration uses the Domain Name Service (DNS) — a set of servers maintained by Internet Service Providers (ISPs) and other network users — to look up hostnames and get back IP addresses.*

Lookup hostname:
```
host google.com
nslookup google.com
```

### Localhost

*The IPv4 address 127.0.0.1 and the IPv6 address ::1 are special addresses that mean "this computer itself" — for when a client (like your browser) is accessing a server on your own computer. The hostname localhost refers to these special addresses.*


## Ports

*All of the network traffic that computers send and receive — everything from web requests, to login sessions, to file sharing — is split up into messages called packets. Each packet has the IP addresses of the computer that sent it, and the computer that receives it. And (with the exception of some low-level packets, such as ping) it also has the port number for the sender and recipient. IP addresses distinguish computers; port numbers distinguish programs on those computers.*


## HTTP Protocol

### HTTP Request


```
GET / HTTP/1.1
Host: localhost:8000
Connection: keep-alive
...
Cookie: io=mS1bZluod7AY2aJBAAA
```
 - `GET` is the request **method** or **verb**
 - `/` is the request **path**
 - `HTTP/1.1` is the request **protocol**
 - `Connection...Cookie` is the request **headers**

### HTTP Response

```
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.6.4
Date: Mon, 19 Mar 2018 16:55:23 GMT
Content-type: text/html; charset=utf-8
Content-Length: 340

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
...
</html>
```
 - `HTTP/1.0` is the response **protocol**
 - `200 OK` is the response **status**
 - `Server...Content-Lenght` is the response **header**
 - `<!DOCTYPE...` is the response **body**


### Status Codes

 - 1xx — Informational. The request is in progress or there's another step to take.
 - 2xx — Success! The request succeeded. The server is sending the data the client asked for.
 - 3xx — Redirection. The server is telling the client a different URI it should redirect to. The headers will usually contain a Location header with the updated URI. Different codes tell the client whether a redirect is permanent or temporary.
 - 4xx — Client error. The server didn't understand the client's request, or can't or won't fill it. Different codes tell the client whether it was a bad URI, a permissions problem, or another sort of error.
 - 5xx — Server error. Something went wrong on the server side.


### Request Methods

 - `GET` gets a resource
 - `POST` creates or updates a resource
 - `PUT` creates a new resource
 - `PATCH` updates a resource
 - `DELETE` deletes a resource
 - `HEAD` is like `GET` but only return headers
 - `OPTIONS` is used to find features supported by the server
 - `TRACE` echoes back what the server received from the client

[Official Spec](https://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html)


### Headers

*An HTTP response can include many headers. Each header is a line that starts with a keyword, such as Location or Content-type, followed by a colon and a value. Headers are a sort of metadata for the response. They aren't displayed by browsers or other clients; instead, they tell the client various information about the response.*


 - `Set Cookie` and `Cookie`: To set a cookie, the server sends the Set-Cookie header. The browser will then send the cookie data back in a Cookie header on subsequent requests.
- `Content-type`: A Content-type header indicates the kind of data that the server is sending. It includes a general category of content as well as the specific format.
- `Content-Length`: Tells the client how long (in bytes) the response body will be.


### Cookies

*Cookies are a way that a server can ask a browser to retain a piece of information, and send it back to the server when the browser makes subsequent requests. Every cookie has a name and a value, much like a variable in your code; it also has rules that specify when the cookie should be sent back.*

*If the server sends each client a unique cookie value, it can use these to tell clients apart. This can be used to implement higher-level concepts on top of HTTP requests and responses — things like sessions and login. Cookies are used by analytics and advertising systems to track user activity from site to site. Cookies are also sometimes used to store user preferences for a site.*

*The first time the client makes a request to the server, the server sends back the response with a `Set-Cookie` header. This header contains three things: a cookie name, a value, and some attributes. Every subsequent time the browser makes a request to the server, it will send that cookie back to the server. The server can update cookies, or ask the browser to expire them.*

```
Set-Cookie: app_session=eyJpdiI6ImJiNW...wdFV1eVVwTWViYjFoVWc9PSIsIm1hYyI6IjgxOGM2ZGQwZTIwNjBiNDFmZDZmNDllZTEzZDM2YTUwZGRjYmEyOTY3ZWFjODJjYWExZDg3N2Q3ZTkwNmM1MTUifQ%3D%3D; expires=Wed, 28-Mar-2018 09:27:48 GMT; Max-Age=604800; path=/; domain=app.com; secure; HttpOnly
```

 - `app_session` is the cookie `name` or `key`
 - `eyJpdiI6Im...D%3D` is the cookie `content` or `value`
 - `expires=Wed, 28-Mar-2018 09:27:48 GMT` specifies the expiration time is when the server wants the browser to stop saving the cookie
 - `Max-Age=604800` specifies how long the cookie is saved after creation (in seconds)
 - `domain=app.com` specifies the domain(s) to which the cookie is sent
 - `secure` is a flag which specifies that the cookie will only be sent over HTTPS connections
 - `HttpOnly` is a flag which specifies the cookie will not be accessible to JavaScript code running on the page

The browser should then resend the `Cookie` header in subsequent requests:

```
Cookie: app_session=eyJpdiI6IjBOUkwyK1pcL2tP...KzdmTkN2bkZ4VVc2Qm0yNlhcL0R5bGc9PSIsIm1hYyI6ImI4MjAxMTJiMTQxZDM0M2MzOGJjZjk4NWJkNjBmMzNjNGYzYmIyMjUzYTliMGU5YTZjZmY2ZDgzMDQ4Njg0NTcifQ%3D%3D
```

### HTTPS over TLS

*When a browser and a server speak HTTPS, they're just speaking HTTP, but over an encrypted connection. The encryption follows a standard protocol called Transport Layer Security, or TLS for short. TLS provides some important guarantees for web security:*

 - *It keeps the connection **private** by encrypting everything sent over it. Only the server and browser should be able to read what's being sent.*
 - *It lets the browser **authenticate** the server. For instance, when a user accesses https://www.udacity.com/, they can be sure that the response they're seeing is really from Udacity's servers and not from an impostor.*
 - *It helps protect the **integrity** of the data sent over that connection — checking that it has not been (accidentally or deliberately) modified or replaced.*

*Note: TLS is also very often referred to by the older name SSL (Secure Sockets Layer). Technically, SSL is an older version of the encryption protocol. This course will talk about TLS because that's the current standard.*

#### Keys and Certificates

*The server-side configuration for TLS includes two important pieces of data: a private key and a public certificate. The private key is secret; it's held on the server and never leaves there. The certificate is sent to every browser that connects to that server via TLS. These two pieces of data are mathematically related to each other in a way that makes the encryption of TLS possible.*

*The server's certificate is issued by an organization called a certificate authority (CA). The certificate authority's job is to make sure that the server really is who it says it is — for instance, that a certificate issued in the name of Heroku is actually being used by the Heroku organization and not by someone else.*

*The role of a certificate authority is kind of like getting a document notarized. A notary public checks your ID and witnesses you sign a document, and puts their stamp on it to indicate that they did so.*