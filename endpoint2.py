from fastapi import FastAPI

app = FastAPI()

products = {
    101: {"name": "Laptop", "price": 85000},
    102: {"name": "Mouse", "price": 1200},
    103: {"name": "Keyboard", "price": 2500}
}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id in products:
        return products[product_id]
    return {"message": "Product not found"}
