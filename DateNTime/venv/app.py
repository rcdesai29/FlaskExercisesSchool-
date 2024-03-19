from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    current_time = datetime.now().strftime("%A, %B %d %Y %H:%M:%S")
    return render_template("layout.html", current_time=current_time)

if __name__ == "__main__":
    app.run(debug=True)
