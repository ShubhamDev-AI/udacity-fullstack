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


### Headers

*An HTTP response can include many headers. Each header is a line that starts with a keyword, such as Location or Content-type, followed by a colon and a value. Headers are a sort of metadata for the response. They aren't displayed by browsers or other clients; instead, they tell the client various information about the response.*


 - `Set Cookie` and `Cookie`: To set a cookie, the server sends the Set-Cookie header. The browser will then send the cookie data back in a Cookie header on subsequent requests.
- `Content-type`: A Content-type header indicates the kind of data that the server is sending. It includes a general category of content as well as the specific format.
- `Content-Length`: Tells the client how long (in bytes) the response body will be.
