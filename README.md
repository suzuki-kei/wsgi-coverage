# wsgi-coverage

WSGI アプリケーションに対するマニュアルテストのカバレッジを計測する.

# 各種手順

    # イメージをビルドする.
    docker build -t wsgi-coverage .

    # イメージ内のソースコードでアプリケーションを実行する.
    docker run -it --rm -p 8080:80 wsgi-coverage

    # 手元にある最新のソースコードでアプリケーションを実行する.
    docker run -it --rm -v $(pwd)/src:/opt/wsgi-coverage-app:ro -p 8080:80 wsgi-coverage

    # (for debug) bash を実行する.
    docker run -it --rm -v $(pwd)/src:/opt/wsgi-coverage-app:ro -p 8080:80 wsgi-coverage bash

