import myapp.controllers


def application(environ, start_response):
    controller = _get_controller(environ)
    if controller:
        status = "200 OK"
        response_body_str = controller()
    else:
        status = "404 Not Found"
        response_body_str = myapp.controllers.error_404()

    response_body_bytes = response_body_str.encode("utf-8")
    response_headers = _make_response_headers(response_body_bytes)
    start_response(status, response_headers)
    return [response_body_bytes]


def _get_controller(environ):
    routings = {
        "/": myapp.controllers.index,
        "/hoge": myapp.controllers.hoge,
        "/piyo": myapp.controllers.piyo,
        "/fuga": myapp.controllers.fuga,
        "/gofu": myapp.controllers.gofu,
    }
    return routings.get(environ["PATH_INFO"], None)


def _make_response_headers(response_body_bytes: bytes) -> dict[str, str]:
    return [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(response_body_bytes))),
    ]

