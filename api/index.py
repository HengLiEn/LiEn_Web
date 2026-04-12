from flask import Flask, render_template

app = Flask(__name__)

PHOTOS = {
    "hero": "photo_2026-04-12-19-09-57.jpg",
    "about": "photo_2026-04-12-19-51-34.jpg"
}

@app.route("/")
def index():
    return render_template("index.html", photos=PHOTOS)


# Vercel entrypoint
def handler(request, context):
    return app