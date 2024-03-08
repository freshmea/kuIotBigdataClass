from flask import Flask
import pymysql

app = Flask(__name__)

host = "localhost"
port = 3306
database = "madangdb"
username = "root"
password = "0000"
config = True
conn = pymysql.connect(
    host=host,
    port=port,
    db=database,
    user=username,
    password=password,
    charset="utf8",
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM Book")
books = cursor.fetchall()
cursor.close()
conn.close()


@app.route("/")
def index():
    outputString = str()
    for book in books:
        for c in book:
            outputString += str(c) + "    "
        outputString += "////"
    return outputString


if __name__ == "__main__":
    app.run(debug=True)
