
pwd := $(shell pwd)

.PHONY: clean
clean: # 生成したファイルを削除する.
	rm -rf target

.PHONY: build
build: # イメージをビルドする.
	docker build -t wsgi-coverage .

.PHONY: start
start: # バックグラウンドでサーバを実行する.
	docker run -d --rm -p 8080:80 --name wsgi-coverage \
		-v $(pwd)/src:/opt/wsgi-coverage-app/src:ro \
		-v $(pwd)/config:/opt/wsgi-coverage-app/config:ro \
		-v $(pwd)/scripts:/opt/wsgi-coverage-app/scripts:ro \
		-v $(pwd)/target:/opt/wsgi-coverage-app/target \
		wsgi-coverage

.PHONY: logs
logs: # バックグラウンドで実行中のサーバのログを閲覧する.
	docker logs -f wsgi-coverage

.PHONY: stop
stop: # バックグラウンドで実行中のサーバを停止する.
	docker kill wsgi-coverage

.PHONY: run
run: # フォアグラウンドでサーバを実行する.
	docker run -it --rm -p 8080:80 --name wsgi-coverage \
		-v $(pwd)/src:/opt/wsgi-coverage-app/src:ro \
		-v $(pwd)/config:/opt/wsgi-coverage-app/config:ro \
		-v $(pwd)/scripts:/opt/wsgi-coverage-app/scripts:ro \
		-v $(pwd)/target:/opt/wsgi-coverage-app/target \
		wsgi-coverage

.PHONY: report
report: # カバレッジレポートを生成する.
	docker run -it --rm \
		-v $(pwd)/src:/opt/wsgi-coverage-app/src:ro \
		-v $(pwd)/config:/opt/wsgi-coverage-app/config:ro \
		-v $(pwd)/scripts:/opt/wsgi-coverage-app/scripts:ro \
		-v $(pwd)/target:/opt/wsgi-coverage-app/target \
		wsgi-coverage coverage html --rcfile="/opt/wsgi-coverage-app/config/coveragerc"

.PHONY: bash
bash: # (for debug) bash を実行する.
	docker run -it --rm \
		-v $(pwd)/src:/opt/wsgi-coverage-app/src:ro \
		-v $(pwd)/config:/opt/wsgi-coverage-app/config:ro \
		-v $(pwd)/scripts:/opt/wsgi-coverage-app/scripts:ro \
		-v $(pwd)/target:/opt/wsgi-coverage-app/target \
		wsgi-coverage bash

.PHONY: random-requests
random-requests: # (for debug) ランダムなリクエストを送信する.
	shuf -n 3 -e / /hoge /piyo /fuga /gofu /not-found \
		| xargs -I{} bash -c 'echo -n "{} => " && curl localhost:8080{} && echo'

