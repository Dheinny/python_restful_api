# Interview Test

This repository is an interview test solving, where I was challenged to create API restful using Python e its frameworks.
It is expected to build an API to simulate a virtual store and to develop endpoints that allow register clients, products, and order.
It was developed using:
- Language: Python 3.8
- Framework: Flask
- Database: MongoDB

## Prerequisites
To run this project it is necessary to have preinstalled:
Python and Pip 3.8 version
Docker
It is recommended to separate the python environment using a virtualenv package.

## Prepare to execution
Once you have cloned this repository, first you have to install the python packages required for this project:
Let's call the project root directory $HOME_PROJ

To just execute the API install the prod.txt file located in $HOME_PROJ/requirements:
```
$ pip install -r $HOME_PROJ/requiremets/prod.txt
```
It will install all the required packages to run the project.

If you intended to fork the project and continue developing it, you can run the dev requirements, following the command above:
```
$ pip install -r $HOME_PROJ/requiremets/dev.txt
```
It will install the packages to develop, and the tests package as well.

## Starting MongoDB 
We are using MongoDB as the database for this project. To start it, first, you have to pull the MongoDB image from the Docker repository:
```
$ docker run --name mongo-latest -p 27017:27017 -d mongo
```
That command will download a mongo image if it not exists, and create a mongo container called mongo-latest, mapping your localhost's port 27017 to 27017 container's port and run it as a daemon.

## Starting the API
To start up the API, just execute the command below:
```
$ python applications.py
```

### Methods available
The followings methods are available for a while:
#### Clients
##### POST
Create a new client
```
$ curl -X POST localhost:5000/clients -H "Content-Type: application/json" -d '{ 
    "name": "cliente 4", 
    "email": "Cliente4@gmail.com", 
    "address": "rua de teste, da cidade de teste" 
}'
```

##### GET
###### List all clients
```
curl localhost:5000/clients
```
To paginate the result, *page* and *page_size* are available:
```
curl "localhost:5000/clients?page=2&page_size=2"
```

###### Get a specific client by ID
curl localhost:5000/clients/{id}
```
$ curl localhost:5000/clients/5f0d0ff7131bc94677b64308
```

##### DELETE
Delete a client by ID
curl -X DELETE -i localhost:5000/clients/{id}

```
$ curl -X DELETE -i localhost:5000/clients/5f0d0ff7131bc94677b64308
```

#### Products
##### POST
Create a new product
```
$ curl -X POST localhost:5000/products -H "Content-Type: application/json" -d '{
    "name": "product 01",
    "cod_prod": "INF01",
    "desc": "Descricao do produto 01",
    "price":20.40
}'
```

##### GET
###### List all products
```
curl localhost:5000/products
```
To paginate the result, *page* and *page_size* are available:
```
curl "localhost:5000/products?page=2&page_size=2"
```

###### Get a specific product by COD_PROD
curl localhost:5000/products/{cod_prod}, where the cod_prod is the code of the product

```
$ curl localhost:5000/products/INF01
```

##### DELETE{}
Delete a product by cod_prod (code of the product)
curl -X DELETE -i localhost:5000/products/{cod_prod}

```
$ curl -X DELETE -i localhost:5000/products/INF01
```

# Execute tests
To execute tests you must to install the packages required in test.py ou dev.py files, in the #HOME_PROJ/requirements dir

Run the next command to install the API package in editable mode, so you will have a reference of our API path, to execute the tests.
```
$ pip install -e .
```

Then it is possible to execute the tests running the pytest tool:
```
$ pytest
```


