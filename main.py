from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route("/")
def home():
    return render_template("index.html", library=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = {
            "name": request.form.get("bName"),
            "author": request.form.get("bAuthor"),
            "rating": request.form.get("rating"),
        }
        all_books.append(new_book)
        return redirect(url_for("home"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
