import React from 'react';

function ProductDetail({products, ...props}) {
    const { id } = props.match.params;
    const product = products.find((product) => product.id === id);

    if (!product) {
        return <div>Product not found</div>;
    }

    return (
        <div>
            <h2>{product.name}</h2>
            <p>{product.description}</p>
            <p>Price: ${product.price}</p>
        </div>
    );
}

export default ProductDetail;
