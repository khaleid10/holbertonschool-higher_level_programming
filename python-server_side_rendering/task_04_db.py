#!/usr/bin/python3
"""Display product data from JSON, CSV, or SQLite using Flask."""

import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file(filename):
    """Read products from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def read_csv_file(filename):
    """Read products from a CSV file."""
    products = []

    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)

    return products


def read_sql_file(filename):
    """Read products from a SQLite database."""
    conn = sqlite3.connect(filename)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        'SELECT id, name, category, price FROM Products'
    )

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]


@app.route('/products')
def products():
    """Display products from the selected data source."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    try:
        if source == 'json':
            product_list = read_json_file('products.json')
        elif source == 'csv':
            product_list = read_csv_file('products.csv')
        elif source == 'sql':
            product_list = read_sql_file('products.db')
        else:
            return render_template(
                'product_display.html',
                products=[],
                error='Wrong source'
            )
    except (OSError, json.JSONDecodeError, sqlite3.Error) as error:
        return render_template(
            'product_display.html',
            products=[],
            error=str(error)
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
