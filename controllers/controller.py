from app import app
from flask import render_template, url_for
from models.orders import orders


@app.route('/')
def index():
    return render_template('index.jinja', title = 'Orders List', orders = orders)

@app.route('/<page>')
def order_details(page):
    return render_template(f'{[page]}')