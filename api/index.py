from flask import Flask, render_template
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print("BASE_DIR:", BASE_DIR)
print("static folder exists:", os.path.exists(os.path.join(BASE_DIR, "static")))
print("photo exists:", os.path.exists(os.path.join(BASE_DIR, "static", "photo_2026-04-12-19-09-57.jpg")))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

print("Files in static:", os.listdir(os.path.join(BASE_DIR, "static")))