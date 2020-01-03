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

vim_assembly: export TIDE_CONFIG_LOCATION=/Users/willvk/source/wilvk/vgdb/plugins/atom/assembly_filter/config/
vim_assembly:
	brew unlink gdb_tim && brew link gdb
	vim

vim_c: export TIDE_CONFIG_LOCATION=/Users/willvk/source/wilvk/vgdb/plugins/atom/test_c_filter/
vim_c:
	brew unlink gdb && brew link gdb_tim
	vim

vim_python: export TIDE_CONFIG_LOCATION=/Users/willvk/source/wilvk/vgdb/plugins/atom/python/
vim_python:
	vim
