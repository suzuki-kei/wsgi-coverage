# wsgi-coverage

WSGI アプリケーションに対するマニュアルテストのカバレッジを計測する.

# 各種手順

    # イメージをビルドする
    docker build -t wsgi-coverage .

    # httpd を実行する
    docker run -it --rm -v $(pwd)/src:/opt/wsgi-coverage-app:ro -p 8080:80 wsgi-coverage

    # bash を実行する (for debug)
    docker run -it --rm -v $(pwd)/src:/opt/wsgi-coverage-app:ro -p 8080:80 wsgi-coverage bash

