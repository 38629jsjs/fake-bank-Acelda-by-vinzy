import os
from flask import Flask, send_from_directory

# Directory this file lives in — index.html must sit right next to app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


@app.route("/")
def home():
    # Serves index.html from this same folder
    return send_from_directory(BASE_DIR, "index.html")


# Optional: if you ever add more static files (images, extra pages, etc.)
# next to app.py, this lets them be reached at /filename too.
@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(BASE_DIR, filename)


if __name__ == "__main__":
    # Koyeb (and most PaaS hosts) inject the port to listen on via $PORT.
    # Falls back to 8000 for local testing.
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
