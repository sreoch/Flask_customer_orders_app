from flask import render_template
from app import app
from models import customer_orders
from models.customer_orders import orders


@app.route("/orders")
def index():
    return render_template("index.html", title="home", orders=orders)


@app.route("/orders/<index>")
def find_order(index):
    index_num = int(index)
    return render_template("order.html", title="home", orders=orders, index=index_num)
