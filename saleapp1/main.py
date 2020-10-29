from flask import render_template
from saleapp1 import app,untils

@app.route('/')
def index():
    categories = untils.read_data()
    return render_template('index.html',categories=categories)

@app.route('/products')
def products_list():
    products = untils.read_data(path='data/products.json')
    return  render_template('products.html', products = products)


if __name__ == '__main__':
    app.run(debug=True)

