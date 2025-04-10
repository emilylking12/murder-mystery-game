from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    name = request.form.get("name")
    trait1 = request.form.get("trait1")
    trait2 = request.form.get("trait2")
    return render_template("scene1.html", name=name, trait1=trait1, trait2=trait2)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
