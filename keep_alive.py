from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "My bot is alive!"
    
def keep_alive():
    server = Thread(target=main)
    server.start()