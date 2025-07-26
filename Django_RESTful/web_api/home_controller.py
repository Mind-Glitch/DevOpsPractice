from typing import Awaitable, Callable
from persistance.serve_static_file import get_file_content
import json

async def index(receive, send):
    code, content, content_type = get_file_content("index.html")

    await send({
        "type": "http.response.start",
        "status": code,
        "headers": [
            (b"content-type", content_type.encode('utf-8'))
        ],
    })

    await send({
        "type": "http.response.body",
        "body": content
    })

async def get_data(receive, send):
    await send({
        "type": "http.response.start",
        "status": 200,
        "headers": [
            (b"content-type", b"text/plain")
        ]
    })

    await send({
        "type": "http.response.body",
        "body": b"Oh, nigga, you gay!"
    })

async def process_number(receive, send) :
    await send({
        "type" : "http.response.start",
        "status": 200,
        "headers": [
            [b"content-type", b"application/json"]
        ] 
    })

    data = await receive()
    body = data.get("body").decode('utf-8')
    if not body:
        body = '{"my_number": 1487}'
        
    encoded_content = json.loads(body)

    my_number = int(encoded_content["my_number"])

    response_body = json.dumps({"new_number": my_number + 1}).encode("utf-8")
    
    await send({
        "type": "http.response.body",
        "body": response_body,
        "more_body": False
    })