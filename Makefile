.PHONY:test
.PHONY:clean
.PHONY:git-install
.PHONY:build
.PHONY:upload
.PHONY:local-dev
.PHONY:docker-dev

test:
	docker-compose -f ./tests/docker/docker-compose.yml build
	docker-compose -f ./tests/docker/docker-compose.yml run --rm --service-ports test-python-tide /work/tests/scripts/run-python-tests

clean:
	rm -rf dist
	rm -rf tide.egg-info
	rm -rf build

git-install:
	git submodule init
	git submodule update

build:
	docker-compose -f ./tests/docker/docker-compose.yml build
	docker-compose -f ./tests/docker/docker-compose.yml run --rm --service-ports test-python-tide /work/tests/scripts/run-build-package

upload:
	docker-compose -f ./tests/docker/docker-compose.yml build
	docker-compose -f ./tests/docker/docker-compose.yml run --rm --service-ports test-python-tide /work/tests/scripts/run-upload-package

local-dev:
	DIR=$(realpath .)
	pip install $DIR

docker-dev:
	docker-compose -f ./tests/docker/docker-compose.yml build
	docker-compose -f ./tests/docker/docker-compose.yml run --rm --service-ports test-python-tide sh
