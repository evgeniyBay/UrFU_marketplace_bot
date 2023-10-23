import React from 'react';
import './Product.css';

function Product({ name, price, description }) {
    return (
        <div className="product-container">
            <div className="product">
                <div className="product-info">
                    <h2>{name}</h2>
                    <p>{description}</p>
                    <p>Price: {price}</p>
                </div>
            </div>
        </div>
    );
}

export default Product;

