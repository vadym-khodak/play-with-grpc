from __future__ import print_function

import logging
import os

import grpc

from blog_post_pb2 import BlogPost, GetAllPostRequest
from blog_post_pb2_grpc import BlogPosterStub


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel(f'{os.getenv("SERVER_HOST", "localhost")}:{os.getenv("SERVER_PORT", "50051")}') as channel:
        stub = BlogPosterStub(channel)
        response = stub.CreatePost(BlogPost(
            title='Test Title',
            text='Lorem ipsum',
            published=True
        ))
    print(response)

    with grpc.insecure_channel(f'{os.getenv("SERVER_HOST", "localhost")}:{os.getenv("SERVER_PORT", "50051")}') as channel:
        stub = BlogPosterStub(channel)
        response = stub.GetPost(BlogPost(id_=1))

    print(response)

    with grpc.insecure_channel(f'{os.getenv("SERVER_HOST", "localhost")}:{os.getenv("SERVER_PORT", "50051")}') as channel:
        stub = BlogPosterStub(channel)
        response = stub.GetAllPost(GetAllPostRequest(page=2, per_page=2))

    print(response)


if __name__ == '__main__':
    logging.basicConfig()
    run()
