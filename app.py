from flask import Flask, redirect, url_for, render_template, request
import sqlite3
from flask import g
import sys
import os
sys.path.append(os.path.abspath('ML_Model/'))
import ML_Model.predict as pred
app = Flask(__name__)

DATABASE = '/Database/database.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/", methods=["POST", "GET"])
def use():
    sql1 = "SELECT * FROM product ORDER BY RANDOM() LIMIT 9"
    con = sqlite3.connect('Database/database.db')
    con.row_factory = sqlite3.Row
    recomond = []
    if request.method == "POST":
        key = request.form["search"]
        sql1 = "SELECT * FROM product WHERE PRODUCT_NAME LIKE '%" + \
            key + "%' AND PRODUCT_ID  LIKE 'P%' ORDER BY RANDOM() LIMIT 6"
        predict = pred.prediction(key)
        print("Cluster ID ", key, predict)
        sql2 = "SELECT * FROM product WHERE CLUSTER_ID=? AND  PRODUCT_ID  LIKE 'R%' ORDER BY RANDOM() LIMIT 3"
        print(sql2)
        cur2 = con.cursor()
        cur2.execute(sql2, str(predict[0]))
        recomond = cur2.fetchall()
        print(recomond)
    cur = con.cursor()
    cur.execute(sql1)
    product = cur.fetchall()
    print("products : ", product)

    return render_template("index.html", products=product, recomonds=recomond)


if __name__ == "__main__":
    app.run(debug=True)
