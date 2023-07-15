PROJECT_NAME:=primesbot
MAIN:=app/main.py

docker_build:
	docker build -t $(PROJECT_NAME) -f docker/Dockerfile .

venv:
	. venv/bin/activate

pip_install:
	pip install -r app/requirements.txt

run: venv pip_install docker_build
	docker run $(PROJECT_NAME)

install_and_run_local: venv pip_install 
	python3 $(MAIN) 

run_local:
	python3 $(MAIN) 

