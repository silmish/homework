# Homework

Few general notes:

My goal was to use some new framework that had not used before and create the wanted outcome with a simple and light solution. This means that the project structure is very plain and not built in mind of expanding it as it is.

The API has been built with python fastapi framework. No external database has been used, so data do not persist between restarts. The product information has been hardcoded, while orders can be generated and manipulated with the API.

Only one of the homework goals could not be met. This is goal 3. make the app able to listen and configure ports. This is for me a new topic, been researching the topic but unfortunately with this time frame could not solve how it can be implemented into this project. Would like to discuss and hear more how this is meant to be done in this type of APIs. 

Time used for the project was:

* 3 hours for researching and deciding on the tech which to use.
* 8½ hours to get the project done.
* 1 hours to write the documents and setup repo.

## Requirements

Fastapi
`````
pip install fastapi
`````

Uvicorn
`````
pip install uvicorn[standard]
`````
## API functionality

If not familiar with the framework it comes with an interactive documentation. Within this project it can be used with localhost:8000/docs. All the endpoints can be tested within the docs.

### Example uses of the endpoints

`````
GET /api/products

Get list of all the prodcuts.


curl -X 'GET' \
  'http://127.0.0.1:8000/api/products' \
  -H 'accept: application/json'
`````

`````
POST /api/orders

Remark regarding this endpoint. I could not get it to work,
so that a new order is generated with empty body, 
this is why the example has a product id as body.

curl -X 'POST' \
  'http://127.0.0.1:8000/api/orders' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{ 

  "products": [
    {
      "id": 123
    }
]
}'
`````

`````
GET /api/orders/{order_id}

Get all the order details


curl -X 'GET' \
  'http://127.0.0.1:8000/api/orders/aad70c7c-4af9-46a6-92be-5be8b43dd9d3' \
  -H 'accept: application/json'

Replace order id with the one generated earlier.
`````

`````
GET /api/orders/{order_id}/products

Get product information regarding a order.

curl -X 'GET' \
  'http://127.0.0.1:8000/api/orders/aad70c7c-4af9-46a6-92be-5be8b43dd9d3/products' \
  -H 'accept: application/json'

Replace order id with the one generated earlier.
`````

`````
POST /api/orders/{order_id}/products

Add an product to the order using product ID.

curl -X 'POST' \
  'http://127.0.0.1:8000/api/orders/aad70c7c-4af9-46a6-92be-5be8b43dd9d3/products' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 456,
  "quantity": 1
}'

Replace order id with the one generated earlier.
`````

`````
PATCH /api/orders/{order_id}

Change and update order status information.

curl -X 'PATCH' \
  'http://127.0.0.1:8000/api/orders/aad70c7c-4af9-46a6-92be-5be8b43dd9d3' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "status": "PAID"
}'

Replace order id with the one generated earlier.
`````

`````
PATCH /api/orders/{order_id}/products/{product_id}

This end point has 2 functions as stated in the homework assesment. For some reason the docs did not work with this.

http://127.0.0.1:8000/api/orders/3e6de37b-f890-4443-b536-9d1e393963ac/products/123

with body: {
    "id": 999,
    "quantity": 3
}

Changes the product 123 to 999 with quantity 3.

http://127.0.0.1:8000/api/orders/3e6de37b-f890-4443-b536-9d1e393963ac/products/999

with body: {
    "quantity": 1
}

Changes product 999 quantity to 1 from previous 3.

Replace order id with the one generated earlier.
`````