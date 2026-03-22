#!/usr/bin/env python3
"""Simpele HTTP server voor catARACT website."""
import http.server
import socketserver
import os

PORT = 8093
os.chdir(os.path.dirname(os.path.abspath(__file__)))

handler = http.server.SimpleHTTPRequestHandler
handler.extensions_map.update({'.js': 'application/javascript', '.css': 'text/css'})

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"catARACT server op http://localhost:{PORT}")
    httpd.serve_forever()
