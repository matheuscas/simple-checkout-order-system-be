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

Ps.: if you don't know what's you container's name, run `docker ps` and at the most right collumn the name is there. Pick the one that ends with `api`. 

Now you can access http://0.0.0.0:8000/api/v1/menu check the persisted items. 

## Troubleshoot 

In the case of the `api` don't connect to the database, please try to run `docker-compose up --build` again or manually run the migrations using the following command: `docker exec <container_name> ./manage.py migrate`
