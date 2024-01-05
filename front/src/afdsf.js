import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import './index.css';

let url = 'http://127.0.0.1:5000/products';

const App = () => {
  const [products, setProducts] = useState([]);
  const [selectedProduct, setSelectedProduct] = useState(null);

  const getProductDetails = (productId) => {
    // Fetch product details from the server based on the selected productId
    // You can use a separate API endpoint to retrieve the detailed information of the product or use the existing API endpoint with query parameters
    // For simplicity, let's assume you have an API endpoint called `http://127.0.0.1:5000/products/{productId}` to retrieve the product details

    fetch(`http://127.0.0.1:5000/product/${productId}`)
      .then(response => response.json())
      .then(data => {
        setSelectedProduct(data);
      })
      .catch(error => {
        console.error('Error retrieving product details:', error);
      });
  }

  useEffect(() => {
    // Fetch the list of products from the server
    fetch(url)
      .then(response => response.json())
      .then(data => {
        setProducts(data);
      })
      .catch(error => {
        console.error('Error retrieving products:', error);
      });
  }, []);

  return (
    <div className="screen">
      <div className="titlediv">
        <h2 className="title">URFU MARKETPLACE</h2>
      </div>
      <div className="search">
        {/* Search functionality */}
      </div>
      <div className="buttons">
        {/* Buttons */}
      </div>
      <div className="products">
        {products.map((product) => (
          <Product
            key={product.id}
            photo={product.id}
            name={product.name}
            price={product.price}
            onClick={() => getProductDetails(product.id)}
          />
        ))}
      </div>
      {selectedProduct && (
        <ProductDetails
          product={selectedProduct}
          onClose={() => setSelectedProduct(null)}
        />
      )}
    </div>
  );
};

const Product = ({ photo, name, price, onClick }) => (
  <div className="product" onClick={onClick}>
    <img className="photo" src={process.env.PUBLIC_URL + `/images/products/${photo}.png`} alt={name} />
    <div className="name">{name}</div>
    <div className="price">{price} р.</div>
  </div>
);

const ProductDetails = ({ product, onClose }) => (
  <div className="product-details">
    <h2 className="product-name">{product.name}</h2>
    <img className="product-photo" src={process.env.PUBLIC_URL + `/images/products/${product.id}.png`} alt={product.name} />
    <p className="product-description">{product.description}</p>
    <button className="close-button" onClick={onClose}>Close</button>
  </div>
);

ReactDOM.render(<App />, document.getElementById('root'));
