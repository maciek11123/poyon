#!/usr/bin/env python3
"""
Run this in the same folder as poyon.html:
    python3 server.py
Then open: http://localhost:8080/poyon.html
"""
import http.server, socketserver, os, sys

PORT = 8080
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()
    def log_message(self, fmt, *args):
        print(f"  {args[0]} {args[1]}")

print(f"Serving on http://localhost:{PORT}/poyon.html")
print("Press Ctrl+C to stop.\n")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
