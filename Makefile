server/requirements.txt:
	poetry export --without-hashes --format=requirements.txt > server/requirements.txt

build_server: server/requirements.txt
	docker build server/. -t s_lang_api:latest

build_web:
	docker build web/. -t s_lang_web:latest

build_all: build_server build_web

push_server:
	docker tag s_lang_api:latest talalon/s_lang_api:latest
	docker push talalon/s_lang_api:latest

push_web:
	docker tag s_lang_web:latest talalon/s_lang_web:latest
	docker push talalon/s_lang_web:latest

push_all: push_server push_web