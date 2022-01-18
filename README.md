# simple-checkout-order-system-be
A simple checkout Order System web app for a restaurant (backend)

## Up and running
Make sure that you have docker installed. After that run:
```shell
docker-compose up --build
```
The server should be running on `http://0.0.0.0:8000/` and you should see the default Django
initial page.

The API is browsable, like `api/v1/menu`, but you can find the documentation behind `api/v1/schema`,
like `api/v1/schema/swagger-ui` or `api/v1/schema/redoc`

### Loading data
To load categories and items into database, you can execute the following commands:
```shell
docker exec <container_name> ./manage.py loaddata categories
```
To load the categories and
```shell
docker exec <container_name> ./manage.py loaddata items
```
To load the items.
