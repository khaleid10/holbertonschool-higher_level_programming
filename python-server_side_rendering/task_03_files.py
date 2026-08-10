#!/usr/bin/python3
"""Display product data from JSON or CSV files using Flask."""

import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file(filename):
    """Read product data from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def read_csv_file(filename):
    """Read product data from a CSV file."""
    products = []

    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)

    return products


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/products')
def products():
    """Display products from JSON or CSV files."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        product_list = read_json_file('products.json')
    elif source == 'csv':
        product_list = read_csv_file('products.csv')
    else:
        return render_template(
            'product_display.html',
            products=[],
            error='Wrong source'
        )

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html',
                products=[],
                error='Product not found'
            )

        product_list = [
            product for product in product_list
            if product['id'] == product_id
        ]

        if not product_list:
            return render_template(
                'product_display.html',
                products=[],
                error='Product not found'
            )

    return render_template(
        'product_display.html',
        products=product_list,
        error=None
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
