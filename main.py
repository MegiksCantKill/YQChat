from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import os

PATH = "/Users/demid/Desktop/site/"
SERVER = "yq-chat.pp.ua"
PASSWORD = 12823

handler = SimpleHTTPRequestHandler

with TCPServer((SERVER, PASSWORD), handler) as server:
    print(f"Сервер принимает запросы с портом {PASSWORD}")
    server.serve_forever()
