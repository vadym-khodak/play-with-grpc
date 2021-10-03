import grpc
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import config
from blog_post_pb2 import BlogPost, GetAllPostRequest
from blog_post_pb2_grpc import BlogPosterStub


class Post(BaseModel):
    id_: int
    title: str
    text: str
    published: bool


def create_app() -> FastAPI:
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.post("/posts")
    async def create_post(post: Post):
        with grpc.insecure_channel(f'{config.SERVER_HOST}:{config.SERVER_PORT}') as channel:
            stub = BlogPosterStub(channel)
            response = stub.CreatePost(BlogPost(**post.dict()))
        print(response)
        return {
            "id_": response.id_,
            "title": response.title,
            "text": response.text,
            "published": response.published,

       }

    @app.get("/posts/{id_}")
    async def get_post(id_: int):
        with grpc.insecure_channel(f'{config.SERVER_HOST}:{config.SERVER_PORT}') as channel:
            stub = BlogPosterStub(channel)
            response = stub.GetPost(BlogPost(id_=id_))

        print(response)
        return {
            "id_": response.id_,
            "title": response.title,
            "text": response.text,
            "published": response.published,
        }

    @app.get("/posts")
    async def get_all_posts(page: int = 1, per_page: int = 10):
        with grpc.insecure_channel(f'{config.SERVER_HOST}:{config.SERVER_PORT}') as channel:
            stub = BlogPosterStub(channel)
            response = stub.GetAllPost(GetAllPostRequest(page=page, per_page=per_page))

        print(response)
        return {
            "page": page,
            "per_page": per_page,
            "records": [{
                "id_": record.id_,
                "title": record.title,
                "text": record.text,
                "published": record.published,
            }
                for record in response.records
            ]
       }

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
