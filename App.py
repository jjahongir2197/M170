from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/letters", methods=["GET", "POST"])
def letters():
    if request.method == "POST":
        text = request.form["text"]

        count = len(text.replace(" ", ""))

        return render_template("result33.html", count=count)

    return render_template("index33.html")

if __name__ == "__main__":
    app.run(debug=True)
