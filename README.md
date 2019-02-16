# librebot

A Libre Virtual Assistant to help brokers work. This is a
**free/libre open source software FLOSS**. 

## Instalation

All configuration is made using [docker](https://www.docker.com/)
 and [docker-compose](https://docs.docker.com/compose/).

Build all necessary containers:

```sh
sudo docker-compose build
```

Run all containers

```sh
sudo docker-compose up
```

## Tests

* If you want to make a console test just run this commands:

```sh
sudo docker-compose run --rm bot make train                                     
sudo docker-compose run --rm bot make run-console
```

## Contribute with us

Please check our others modules [here](https://github.com/brokerlibre).
If you have any feature suggestion or bug, please report us with an 
[Issue](https://github.com/brokerlibre/librebot/issues)

## Acknowledgments

We'd like to thank [LAPPIS](http://lappis-unb.gitlab.io/) and 
[tais](http://github.com/lappis-unb/tais) project other **FLOSS** project
with many documentations and tips about chatbot context.
