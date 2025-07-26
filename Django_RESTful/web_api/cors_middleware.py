CORS_ALLOW_ORIGINS = ["http://localhost:5173"]

def create_cors_headers(origin):
    return [
        (b"Access-Control-Allow-Origin", origin),
        (b"Access-Control-Allow-Methods", b"GET, POST, OPTIONS"),
        (b"Access-Control-Allow-Headers", b"Content-Type, Authorization, X-Requested-With")
    ]

async def send_options(send, origin): 
    await send({
        "type": "http.response.start",
        "status": 200,
        "headers": create_cors_headers(origin),
    })

    await send({
        "type": "http.response.body",
        "body": b""
    })

    return

class CorsMiddleware :
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        
        origin = "*"
        for header in scope.get("headers", []):
            if(header[0] == b"origin"):
                origin = header[1]


        if scope["method"] == "OPTIONS":
            send_options(send, origin)

        async def wrapped_message(message):
            if message["type"] == 'http.response.start':
                headers = message.setdefault('headers', [])
                headers.extend(create_cors_headers(origin)) 

            await send(message)


        await self.app(scope, receive, wrapped_message)
