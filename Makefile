.PHONY: tests clean git-install build upload local-dev docker-dev pylint

define DOCKER_COMPOSE
docker-compose -f ./tests/docker/docker-compose.yml build
docker-compose -f ./tests/docker/docker-compose.yml run --rm --service-ports 
endef

tests:
	$(DOCKER_COMPOSE) test ./run-python-tests

clean:
	rm -rf dist
	rm -rf tide.egg-info
	rm -rf build

git-install:
	git submodule init
	git submodule update

build:
	$(DOCKER_COMPOSE) test ./run-build-package

upload:
	$(DOCKER_COMPOSE) test ./run-upload-package

local-dev:
	pip install -e .

docker-dev:
	$(DOCKER_COMPOSE) test sh

pylint:
	$(DOCKER_COMPOSE) pylint pylint *
