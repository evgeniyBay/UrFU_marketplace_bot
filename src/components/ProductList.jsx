import React from 'react';
import Product from './Product';
import './ProductList.css';
import { Link } from 'react-router-dom';

function ProductList({ products }) {
    return (
        <div className="product-list">
            {products.map((product) => (
                <div key={product.id} className="product-container">
                    <Link to={`/products/${product.id}`}>
                        <Product {...product} />
                    </Link>
                </div>
            ))}
        </div>
    );
}

export default ProductList;
