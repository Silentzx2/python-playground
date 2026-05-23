from flask import Flask, render_template

app = Flask(__name__)

# Display a simple HTML page with an image
@app.route("/")
def hello_world():
    return render_template("hello_page.html")

app.run()