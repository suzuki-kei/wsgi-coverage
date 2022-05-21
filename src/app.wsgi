

def application(environ, start_response):
    routings = {
        "/": index,
    }
    path_info = environ["PATH_INFO"]
    controller = routings.get(path_info, None)

    if controller:
        status = "200 OK"
        response_body_str = controller()
    else:
        status = "404 Not Found"
        response_body_str = error_404()

    response_body_bytes = response_body_str.encode("utf-8")
    response_headers = make_response_headers(response_body_bytes)
    start_response(status, response_headers)
    yield response_body_bytes


def make_response_headers(response_body_bytes: bytes) -> dict[str, str]:
    return [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(response_body_bytes))),
    ]


def error_404() -> str:
    return "404 Not Found"


def index() -> str:
    return "Hello"

