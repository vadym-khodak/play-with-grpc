import os

if os.environ.get('https_proxy'):
    del os.environ['https_proxy']
if os.environ.get('http_proxy'):
    del os.environ['http_proxy']

ORIGINS = [
    "http://localhost:3000",
    "http://localhost:80",
    "http://localhost:8000",
    os.getenv("ADDITIONAL_ORIGIN", "http://localhost")
]
SERVER_HOST = os.getenv("SERVER_HOST", "localhost")
SERVER_PORT = os.getenv("SERVER_PORT", "50051")
