#!/usr/bin/python3
"""Simple API using http.server."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handle GET requests."""

    def do_GET(self):
        """Return a response depending on the endpoint."""

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            response = json.dumps(data)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(response.encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            response = json.dumps(data)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(response.encode())

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run():
    """Start the server on port 8000."""
    server_address = ("", 8000)
    server = HTTPServer(server_address, SimpleAPIHandler)

    print("Server running on port 8000")
    server.serve_forever()


if __name__ == "__main__":
    run()
