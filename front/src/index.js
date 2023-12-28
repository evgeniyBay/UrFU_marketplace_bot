import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';


// const test_product = {
//   photo: process.env.PUBLIC_URL + '/images/Photo.svg',
//   name: 'Название',
//   price: 'Цена',
// }

// const prod = [];

let url = 'http://127.0.0.1:5000/products';


var request = new XMLHttpRequest();
request.open("GET", url);
request.responseType = "json";
request.send();
request.onload = function () {
  var products = request.response;
  
  const App = () => (
    <div class="screen">
      <div class="titlediv">
        <h2 class="title">URFU MARKETPLACE</h2>
      </div>
      <div class='search'>
        <div class='search2'>
          <button class="search_button">
            <img class="img" src='/images/Лупа.svg'></img>
          </button>
          <input class="search_field" placeholder="Найти товар..."></input>
        </div>
        <button class='heart_block'>
          <img src='/images/Сердечко Filled.svg'></img>
        </button>
      </div>
      <div class="buttons">
        <button class="button" id='product-button'>Товары</button>
        <button class="button" id='services-button'>Услуги</button>
      </div>
  
      <div className="products">
        {products.map((product, index) => (
          <Product
            key={index}
            photo={product.id}
            name={product.name}
            price={product.price}
          />
        ))}
      </div>
    </div>
  );
  
  
  ReactDOM.render(<App />, document.getElementById('root'));
};


// const products = responseData;

const Product = ({ photo, name, price}) => (
  <div className="product">
    <img className="photo" src={process.env.PUBLIC_URL + `/images/products/${photo}.png`} alt={name} />
    <div className="name">{name}</div>
    <div className="price">{price} р.</div>
  </div>
);
