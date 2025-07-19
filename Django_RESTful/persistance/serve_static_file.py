import pathlib
from typing import NamedTuple

class FileResult(NamedTuple):
    code : int
    content : bytes
    content_type: str

from config import APPLICATION_WEB_DIRECTORY

def get_file_content(file: str):
    path = (pathlib.Path(APPLICATION_WEB_DIRECTORY) /
            file.lstrip('/')
                .rstrip('/')
                .replace('../', ''))

    if not path.exists() :
        return FileResult(code=404, content="file not found".encode('utf-8'), content_type="plain/text")

    with path.open(mode="rb") as file_stream :
        data = file_stream.read()

    return FileResult(code=200, content=data, content_type=getContentType(path.suffix))


def is_static_file(self: str):
    return pathlib.Path(self).suffix != ''

def getContentType(suffix : str) :
    if suffix == '.js':
        return "text/javascript"

    elif suffix == '.html':
        return "text/html"

    elif suffix == ".ico":
        return "image/x-icon"

    return "text/plain"
