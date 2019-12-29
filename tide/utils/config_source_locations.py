from os.path import abspath, isdir, join
from yamlreader import yaml_load
import tide.utils.path_helpers as Ph
import tide.utils.config_source_location as CSL

__CONFIG_DEFAULTS_FILE = "defaults/default_config.yaml"

def __get_single_config(path):
    return yaml_load(path)

def __get_config_path_from_settings(config):
    return (config or {}).get("settings", {}).get("plugins", {}).get("config_path", '')

def get_all_config_locations():
    config_locations = []
    config_path = ''
    base_config_path = CSL.get_base_config_location()
    current_config = __get_single_config(base_config_path)
    while True:
        temp_config_path = join(base_config_path, config_path)
        if isdir(config_path):
            temp_config_path = config_path
        if isdir(temp_config_path):
            config_locations.append(abspath(temp_config_path))
            current_config = __get_single_config(temp_config_path)
            config_path = __get_config_path_from_settings(current_config)
            if not config_path:
                break
            base_config_path = temp_config_path
        else:
            break
    config_locations.append(join(Ph.get_python_scripts_base_path(), __CONFIG_DEFAULTS_FILE))
    return config_locations[::-1]
