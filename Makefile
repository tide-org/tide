# see here for setting up brew links: https://blog.seso.io/posts/gdb-on-macos/
# and ./tests/scripts/gdb_tim.rb for the brew formula

.PHONY: tests clean git-install build upload local-dev docker-dev pylint

UNAME_S := $(shell uname -s)

define DOCKER_COMPOSE
docker-compose -f ./tests/docker/docker-compose.yml build > /dev/null
docker-compose -f ./tests/docker/docker-compose.yml run --rm --service-ports
endef

tests:
	$(MAKE) git-install
	$(DOCKER_COMPOSE) test ./run-python-tests

clean:
	rm -rf dist
	rm -rf tide.egg-info
	rm -rf build
	rm -rf ./lib

git-install:
	git submodule init
	git submodule update

build:
	$(DOCKER_COMPOSE) test ./run-build-package

upload:
	$(DOCKER_COMPOSE) test ./run-upload-package

local-dev:
	pip3 install -e . --user

docker-dev:
	$(DOCKER_COMPOSE) test sh

pylint:
	$(DOCKER_COMPOSE) pylint pylint *


vim_assembly: export TIDE_CONFIG_LOCATION=$(shell pwd)/../tide-plugins/plugins/atom/assembly_filter/config/
vim_assembly:
ifeq ($(UNAME_S),Darwin)
	brew unlink gdb_tim && brew link gdb
endif
	vim

vim_c: export TIDE_CONFIG_LOCATION=$(shell pwd)/../tide-plugins/plugins/atom/test_c_filter/
vim_c:
ifeq ($(UNAME_S),Darwin)
	brew unlink gdb && brew link gdb_tim
endif
	vim

vim_python: export TIDE_CONFIG_LOCATION=$(shell pwd)/../tide-plugins/plugins/atom/python/
vim_python:
	vim
