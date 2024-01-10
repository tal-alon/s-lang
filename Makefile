server/requirements.txt:
	poetry export --without-hashes --format=requirements.txt > server/requirements.txt

build_server: server/requirements.txt
	docker build server/. -t s_lang_api:latest

push:
	docker tag s_lang_api:latest talalon/s_lang_api:latest
	docker push talalon/s_lang_api:latest