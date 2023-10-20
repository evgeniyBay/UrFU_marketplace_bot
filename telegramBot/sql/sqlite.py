import sqlite3 as sq

db = sq.connect('product.db')
cur = db.cursor()


async def db_start():
    global db, cur
    db = sq.connect('product.db')
    cur = db.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS product(product_id TEXT PRIMARY KEY, seller_id TEXT, title TEXT, cost TEXT, description TEXT, photo TEXT)")

    db.commit()


async def create_product(product_id):
    product = cur.execute("SELECT 1 FROM product WHERE product_id == '{key}'".format(key=product_id)).fetchone()
    if not product:
        cur.execute(
            "INSERT INTO product VALUES(?, ?, ?, ?, ?, ?)",
            (product_id, '', '', '', '', ''))
        db.commit()


async def edit_profile(state, product_id, seller_id):
    data = await state.get_data()
    print(data)
    cur.execute(
        f"UPDATE product SET seller_id = ?, title = ?, cost = ?, description = ?, photo = ? WHERE product_id = ?",
        (seller_id, data['title'], data['cost'], data['description'], data['photo'], product_id))
    db.commit()
