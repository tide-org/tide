.PHONY:test
.PHONY:clean
.PHONY:git-install
.PHONY:build
.PHONY:upload
.PHONY:local-dev
.PHONY:docker-dev

define DOCKER_COMPOSE
docker-compose -f ./tests/docker/docker-compose.yml build
docker-compose -f ./tests/docker/docker-compose.yml run --rm --service-ports test-python-tide 
endef

test:
	$(DOCKER_COMPOSE) /work/tests/scripts/run-python-tests

clean:
	rm -rf dist
	rm -rf tide.egg-info
	rm -rf build

git-install:
	git submodule init
	git submodule update

build:
	$(DOCKER_COMPOSE) /work/tests/scripts/run-build-package

upload:
	$(DOCKER_COMPOSE) /work/tests/scripts/run-upload-package

local-dev:
	export DIR=$(realpath .)
	pip install $(DIR)

docker-dev:
	$(DOCKER_COMPOSE) sh
