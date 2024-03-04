from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host="localhost", user="madang", passwd="madang", db="madangdb", charset="utf8"
)
cur = db.cursor()


@app.route("/")
def index():
    sqlstring = "SELECT bookid, bookname, publisher, price FROM Book"
    cur.execute(sqlstring)

    book_list = cur.fetchall()
    return render_template("booklist.html", book_list=book_list)


@app.route("/view")
def getTicket():
    idx = request.args.get("id")
    sqlstring = "SELECT bookid, bookname, publisher, price FROM Book WHERE bookid='" + idx + "'"  # type: ignore
    cur.execute(sqlstring)

    book = cur.fetchall()
    return render_template("bookview.html", book=book)


if __name__ == "__main__":
    app.run("0.0.0.0")
