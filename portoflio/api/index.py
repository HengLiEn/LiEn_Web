# api/index.py

from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates", static_folder="../static")

PHOTOS = {
    "hero": "photo_2026-04-12_19-09-57.jpg",
    "about": "photo_2026-04-12_19-51-34.jpg"
}

@app.route("/")
def index():
    return render_template("index.html", photos=PHOTOS)

def handler(request, context):
    return app(request.environ, lambda *args: None)