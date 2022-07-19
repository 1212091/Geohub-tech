# geohub test project structure
Build Geo's Hub online service by using Python - FastAPI and PostgreSQL. We have 3 services:
product-service, user-service, order-service. We use Docker to containerize these services. In each service:
- service-name.py: controller to receive request.
- db: define database model.
- models: input and output model.
- db_manager: handle CRUD operations to database.
- service: to handle service communication.

## How to run??
 - Make sure you have installed `docker` and `docker-compose`
 - Run `docker-compose up`
 - Head over to:
   http://localhost:8080/api/v1/products/docs for product service docs
   http://localhost:8080/api/v1/users/docs for user service docs
   http://localhost:8080/api/v1/orders/docs for order service docs
 - Sample curl command:
   + View - sort - filter product: `curl --location --request GET 'localhost:8080/api/v1/products?filter_code=SAM&sort_by=code&user_id=1&sort_asc=True'`
   + Create an order: `curl --location --request POST 'localhost:8080/api/v1/orders' \
                   --header 'Content-Type: application/json' \
                   --data-raw '{
                        "order_user_id": 1,
                        "user_id": 1,
                        "order_note": "new service",
                        "order_item_inputs": [
                            {
                                "product_id": 1,
                                "quantity": 2
                            },
                            {
                                "product_id": 2,
                                "quantity": 3
                            }
                        ]
                }'`

## Some assumptions:
- Because authen / author feature still has not been implemented, I have to
pass user_id along with other parameters when send request to view / filter /
sort list of products / services. We use it to track user activity.
- We need to provide some init data for product / service and user so we can
do some other actions:
  + Create user role:
    `
    curl --location --request POST 'localhost:8080/api/v1/users/role' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "role_name": "Call Center"
    }'
    `
  + Create user:
      `
      curl --location --request POST 'localhost:8082/api/v1/users' \
      --header 'Content-Type: application/json' \
      --data-raw '{
          "first_name": "John",
          "last_name": "Snow",
          "phone": "123456",
          "email": "snow@gmail.com",
          "address": "456 Wall Street",
          "role_id": 1
      }'
      `
  + Create product / service:
      `
      curl --location --request POST 'localhost:8080/api/v1/products' \
      --header 'Content-Type: application/json' \
      --data-raw '{
        "code": "XRDP",
        "name": "Remote desktop protocol",
        "description": "To remove desktop",
        "price": 3000,
        "platform": "Ubuntu"
      }'
      `

