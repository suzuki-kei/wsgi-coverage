
def application(environ, start_response):
    status = "200 OK"
    response_body = b"Hello"
    response_headers = [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(response_body))),
    ]

    start_response(status, response_headers)
    yield response_body

