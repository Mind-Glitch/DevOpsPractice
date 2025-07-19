import uvicorn

from persistance.serve_static_file import is_static_file, get_file_content
from web_api.home_controller import index, get_data


async def app(scope, receive, send):
    assert scope["type"] == "http"
    web_path = scope["path"]

    # static file
    if is_static_file(web_path) :
        code, content, content_type = get_file_content(web_path)
        await send({
            "type": "http.response.start",
            "status": code,
            "headers":
                [(b"content-type", content_type.encode('utf-8'))]
        })

        await send({
            "type": "http.response.body",
            "body": content
        })
        return

    # action
    if web_path == '/':
        await index(receive, send)
    elif web_path == '/data':
        await get_data(receive, send)
    else :
        await send({
            "type": "http.response.start",
            "status": 404,
            "headers":
                [(b"content-type", b"plain/text")]
        })

        await send({
            "type": "http.response.body",
            "body": "page not found".encode('utf-8')
        })

