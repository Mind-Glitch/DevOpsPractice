import uvicorn

from persistance.serve_static_file import get_file_content


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
