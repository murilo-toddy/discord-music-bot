PROJECT_NAME:=primesbot

docker_build:
	docker build -t $(PROJECT_NAME) -f docker/Dockerfile .

venv:
	. venv/bin/activate

pip_install:
	pip install -r app/requirements.txt

run: venv pip_install docker_build
	docker run $(PROJECT_NAME)

