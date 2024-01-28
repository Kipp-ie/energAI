import http.server
import socketserver
import os

class DirectoryListingHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Check if the request is for the root directory
        if self.path == "/":
            self.path = "/index.html"  # Serve index.html for root directory

        # Call the base class method to serve the file
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Choose the port you want to run the server on
PORT = 8000

# Set the directory from which to serve files
DIRECTORY = "."  # You can change this to your desired directory

# Change the current directory to the one you want to serve files from
os.chdir(DIRECTORY)

# Start the server
with socketserver.TCPServer(("", PORT), DirectoryListingHandler) as httpd:
    print("Server started at port", PORT)
    httpd.serve_forever()