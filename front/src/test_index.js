import ReactDOM from 'react-dom';
import React, { useState } from 'react';

const ProductList = ({ products, onItemClick }) => {
  return (
    <div>
      <h2>Список товаров</h2>
      <ul>
        {products.map(product => (
          <li key={product.id} onClick={() => onItemClick(product.id)}>
            {product.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

const ProductPage = ({ product, onBackClick }) => {
  return (
    <div>
      <h2>{product.name}</h2>
      <p>{product.description}</p>
      <button onClick={onBackClick}>Назад к списку товаров</button>
    </div>
  );
};

const App = () => {
  const [products] = useState([
    { id: 1, name: 'Товар 1', description: 'Описание товара 1' },
    { id: 2, name: 'Товар 2', description: 'Описание товара 2' },
    { id: 3, name: 'Товар 3', description: 'Описание товара 3' }
  ]);
  const [selectedProduct, setSelectedProduct] = useState(null);

  const handleItemClick = (productId) => {
    const selected = products.find(product => product.id === productId);
    setSelectedProduct(selected);
  };

  const handleBackClick = () => {
    setSelectedProduct(null);
  };

  return (
    <div>
      {!selectedProduct ? (
        <ProductList products={products} onItemClick={handleItemClick} />
      ) : (
        <ProductPage product={selectedProduct} onBackClick={handleBackClick} />
      )}
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));
