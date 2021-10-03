import os


ORIGINS = [
    "http://localhost:3000",
    "http://localhost:80",
    "http://localhost:8000",
    os.getenv("ADDITIONAL_ORIGIN", "http://localhost")
]
SERVER_HOST = os.getenv("SERVER_HOST", "localhost")
SERVER_PORT = os.getenv("SERVER_PORT", "50051")
