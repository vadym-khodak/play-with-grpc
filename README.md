## Play with Python gRPC
I was inspired to try this by [Alex Borysov](https://github.com/alxbnet), [Mykyta Protsenko](https://github.com/mykyta-protsenko), and [Yevgen Golubenko](https://github.com/HalloGene). They made a bunch of great talks about gRPC at Dexoxx conference.
There are some of them:
- [Break me if you can by Mykyta Protsenko, Alex Borysov](https://www.youtube.com/watch?v=HSVvp7tnKp4&list=PLi7MQHgzNDNcOZwIsMSQw5wIqAYYq7uaX)
- [gRPC vs REST: let the battle begin! by Alex Borysov & Mykyta Protsenko](https://www.youtube.com/watch?v=ZDUA5pD50Ok)
- [gRPC Web: It’s All About Communication by Alex Borysov & Yevgen Golubenko](https://www.youtube.com/watch?v=-dNd8agYGtY&t=1461s)

### Getting started
This is a pet project to play with gRPC server with blog posts API written in Python.

There is a Python FastAPI web server that uses Python gRPC client to create and get blog posts.

### Helpful links

- [What is gRPC](https://grpc.io/)
- [Protocol Buffer](https://developers.google.com/protocol-buffers/docs/overview)
- [Quickstart with gRPC in Python](https://grpc.io/docs/languages/python/quickstart/)
- [My personal Docker Hub repository with these services](https://hub.docker.com/repository/docker/vaddimart/play-with-python-grpc)

### Local development
I use docker and docker compose to run these services locally.
Run `docker-compose up` to run Python gRPC server, Python FastAPI web server, and postgres database.

