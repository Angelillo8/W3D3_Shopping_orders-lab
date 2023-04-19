from app import app
from flask import render_template, url_for
from models.orders import orders


@app.route('/')
def index():
    return render_template('index.jinja', title = 'Orders List', orders = orders)

@app.route('/order/<order_index>')
def order(order_index):
    order = orders[int(order_index)-1]
    return render_template('order.jinja', order=order)