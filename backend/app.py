from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, Product, init_db

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db.init_app(app)

@app.route("/api/products")
def get_products():
    q = request.args.get("q", "")
    results = Product.query.filter(Product.name.contains(q)).all()
    return jsonify([p.to_dict() for p in results])

if __name__ == "__main__":
    with app.app_context():
        init_db()
    app.run(debug=True)
