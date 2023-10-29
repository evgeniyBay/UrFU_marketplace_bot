import sqlite3 as sq

db = sq.connect('products.db')
cur = db.cursor()


async def db_start():
    global db, cur
    db = sq.connect('products.db')
    cur = db.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS products(product_id TEXT PRIMARY KEY, seller_id TEXT, title TEXT, cost TEXT, description TEXT, photo TEXT, photo_id TEXT)")

    db.commit()


async def create_product(product_id):
    product = cur.execute("SELECT 1 FROM products WHERE product_id == '{key}'".format(key=product_id)).fetchone()
    if not product:
        cur.execute(
            "INSERT INTO products VALUES(?, ?, ?, ?, ?, ?, ?)",
            (product_id, '', '', '', '', '', ''))
        db.commit()


async def edit_profile(state, product_id, seller_id, photo):
    data = await state.get_data()
    cur.execute(
        f"UPDATE products SET seller_id = ?, title = ?, cost = ?, description = ?, photo = ?, photo_id = ? WHERE product_id = ?",
        (seller_id, data['title'], data['cost'], data['description'], photo, data['photo'], product_id))
    db.commit()
