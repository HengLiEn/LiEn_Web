from flask import Flask, render_template
import os

# Point Flask to the folders relative to api/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
)

PHOTOS = {
    "hero": "photo_2026-04-12-19-09-57.jpg",
    "about": "photo_2026-04-12-19-51-34.jpg"
}

@app.route("/")
def index():
    return render_template("index.html", photos=PHOTOS)

# No handler() function — Vercel uses the `app` object directly