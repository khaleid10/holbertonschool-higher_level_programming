# Task 0 - Basics of HTTP/HTTPS

## HTTP vs HTTPS

HTTP is used to send data between the browser and the server. The data is not encrypted, so it is less secure.

HTTPS is the secure version of HTTP. It uses SSL/TLS to encrypt the data, so it is safer to use for websites like banks or online shopping.

Some differences:

- HTTP is not encrypted.
- HTTPS encrypts the data.
- HTTP uses port 80.
- HTTPS uses port 443.
- HTTPS is more secure.

---

## HTTP Request

A request usually has:

- Method
- URL
- Headers
- Body (sometimes)

Example:

```http
GET /index.html HTTP/1.1
Host: example.com
Accept: text/html
```

---

## HTTP Response

A response usually has:

- Status code
- Headers
- Body

Example:

```http
HTTP/1.1 200 OK
Content-Type: text/html

<html>...</html>
```

---

## HTTP Methods

### GET
Gets data from the server.

Example: Opening a website.

### POST
Sends data to the server.

Example: Creating a new account.

### PUT
Updates existing data.

Example: Editing user information.

### DELETE
Deletes data.

Example: Removing a user.

---

## HTTP Status Codes

### 200 OK
The request worked successfully.

### 201 Created
A new resource was created.

### 301 Moved Permanently
The page was moved to another URL.

### 404 Not Found
The page or resource does not exist.

### 500 Internal Server Error
Something went wrong on the server.
