import React from 'react';
import {BrowserRouter, Router, Route, Routes} from 'react-router-dom';
import ProductList from './components/ProductList';
import ProductDetail from './components/ProductDetail';
import productList from "./components/ProductList";

const products = [
    { id: '1', name: 'Фурсьют', price: "1000000", description: 'не ношеный' },
    { id: '2', name: 'Ответы на матан', price: 2000, description: 'Реально' },
    { id: '1', name: 'Фурсьют', price: "1000000", description: 'не ношеный' },
    { id: '2', name: 'Ответы на матан', price: 2000, description: 'Реально' },
    { id: '1', name: 'Фурсьют', price: "1000000", description: 'не ношеный' },
    { id: '2', name: 'Ответы на матан', price: 2000, description: 'Реально' },
    // Добавьте больше товаров здесь
];

function App() {
    return (
        <BrowserRouter>
        <div className="App">
                <Routes>
                    <Route exact path="/" element={<ProductList products={products}/>}/>
                    <Route path="/products/:id" element={<ProductDetail products={products}/>}/>
                </Routes>
        </div>
        </BrowserRouter>
    );
}

export default App;