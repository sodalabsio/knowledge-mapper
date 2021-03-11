from flask import Flask, request

HOST = '0.0.0.0'
PORT = 5000

app = Flask(__name__, static_url_path='') # path deaults to static/

@app.route("/")
def root():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)