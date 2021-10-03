import os
from concurrent import futures
import logging

import grpc

from db import get_connection
from blog_post_pb2_grpc import BlogPosterServicer, add_BlogPosterServicer_to_server
from blog_post_pb2 import BlogPost, GetAllPostResponse


class Greeter(BlogPosterServicer):

    def CreatePost(self, request, context):
        connection = get_connection()
        cursor = connection.cursor()
        if os.getenv('USE_POSTGRES'):
            cursor.execute(
                "INSERT INTO posts(title, text, published) VALUES (%s, %s, %s)", (
                    request.title,
                    request.text,
                    request.published,
                )
            )
        else:
            cursor.execute(
                "INSERT INTO posts(title, text, published) VALUES (?, ?, ?)", (
                    request.title,
                    request.text,
                    request.published,
                )
            )
        connection.commit()
        cursor.execute(
            f"SELECT id_ FROM posts "
            f"WHERE title = '{request.title}' and text = '{request.text}' and published = {request.published}"
        )
        id_, *_ = cursor.fetchone()
        cursor.close()

        return BlogPost(
            id_=id_,
            title=request.title,
            text=request.text,
            published=request.published,
        )

    def GetPost(self, request, context):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            f"SELECT * FROM posts WHERE id_ = {request.id_}",
        )
        # resp = cursor.fetchone()
        id_, title, text, published = cursor.fetchone()
        cursor.close()

        return BlogPost(
            id_=id_,
            title=title,
            text=text,
            published=published,
        )

    def GetAllPost(self, request, context):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            f"SELECT * FROM posts LIMIT {request.per_page} OFFSET {(request.page - 1) * request.per_page}",
        )
        records = cursor.fetchall()

        cursor.close()

        return GetAllPostResponse(
            page=request.page,
            per_page=request.per_page,
            records=[
                BlogPost(id_=record[0], title=record[1], text=record[2], published=record[3],)
                for record in records
            ]

        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_BlogPosterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
