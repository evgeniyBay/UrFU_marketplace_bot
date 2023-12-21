from flask import Flask, request, jsonify
from models import db, Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)


@app.route('/product', methods=['POST'])
def create_product():
    data = request.json
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')
    photo = data.get('photo')
    user_id = data.get('user_id')
    date = data.get('date')

    new_product = Product(name, price, description, photo, user_id, date)
    db.session.add(new_product)
    db.session.commit()

    return 'Товар добавлен', 201


@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404

    product_data = {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'photo': product.photo,
        'user_id': product.user_id,
        'date': product.date
    }

    return jsonify(product_data), 200


@app.route('/products', methods=['GET'])
def get_all_products():
    products = Product.query.all()

    product_list = []
    for product in products:
        product_data = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'photo': product.photo,
            'user_id': product.user_id,
            'date': str(product.date)
        }
        product_list.append(product_data)

    return jsonify(product_list), 200


@app.route('/clear', methods=['DELETE'])
def clear_database():
    db.drop_all()
    db.create_all()

    return 'БД отчищена', 200


@app.route('/clear/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return 'Продукт успешно удален', 200
    else:
        return 'Продукт не найден', 404



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
