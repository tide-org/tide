from yamlreader import yaml_load

def get_all_configs(config_location_array):
    full_config = {}
    for config_path in config_location_array:
        if not full_config:
            full_config = yaml_load(config_path)
        else:
            full_config = yaml_load(config_path, full_config)
    return full_config
