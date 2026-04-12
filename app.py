from flask import Flask, render_template

app = Flask(__name__)

# ── Photo config ──────────────────────────────────────────────


PHOTOS = {
    "hero":    "photo_2026-04-12_19-09-57.jpg",   # largest — hero right panel
    "travel1": "photo_2026-04-12_19-10-03.jpg",
    "travel2": "photo_2026-04-12_19-10-00.jpg",
    "travel3": "photo_2026-04-12_19-09-52.jpg",
    "travel4": "photo_2026-04-12_19-09-20.jpg",
    "about":   "photo_2026-04-12_19-09-19.jpg",   # about section card
}

@app.route("/")
def index():
    return render_template("index.html", photos=PHOTOS)

if __name__ == "__main__":
    app.run(debug=True)