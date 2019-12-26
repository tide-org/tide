import os
import sys
from os.path import abspath, isdir, realpath, join
import tide.utils.path_helpers as Ph
from yamlreader import yaml_load
import tide.utils.sys_path_container as SPC

__CONFIG_ENVIRONMENT_VARIABLE = "TIDE_CONFIG_LOCATION"

def __get_config_location_from_environment_variable():
    tide_config_location = os.environ.get(__CONFIG_ENVIRONMENT_VARIABLE)
    if tide_config_location:
        real_config_location = realpath(tide_config_location)
        if isdir(real_config_location):
            return abspath(real_config_location)
        base_path = Ph.get_python_scripts_base_path()
        path_from_scripts = join(base_path, real_config_location)
        if path_from_scripts and isdir(path_from_scripts):
            return abspath(path_from_scripts)

def get_base_config_location():
    environment_config_path = __get_config_location_from_environment_variable()
    if environment_config_path:
        return environment_config_path
    raise RuntimeError("error: unable to find a matching path for the config.\r\nplease either set the environment variable TIDE_CONFIG_LOCATION \r\nor specify in the file config_location.yaml")
