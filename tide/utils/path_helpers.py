import os
import shutil
from os.path import abspath, join, isdir, dirname
from yamlreader import yaml_load
import tide.utils.config_source_config as CSC

VALID_PLUGIN_NAMES = ['actions', 'config', 'editor_wrappers', 'filters', 'functions', 'templates']

def __resolve_plugin_path(plugin_name, config_path):
    start_path = __get_start_path(plugin_name, config_path)
    if isdir(start_path):
        return abspath(start_path)
    if start_path:
        plugin_path = __get_plugin_path(start_path, config_path)
        if plugin_path and isdir(plugin_path):
            return abspath(plugin_path)
    return None

def __validate_plugin_name(plugin_name):
    if plugin_name not in VALID_PLUGIN_NAMES:
        raise RuntimeError(f"error: plugin name: {plugin_name} is invalid")

def __get_start_path(plugin_name, config_path):
    config_object = yaml_load(config_path)
    return config_object.get("settings", {}).get("plugins", {}).get(plugin_name + "_path", '')

def __get_plugin_path(start_path, config_path):
    default_path = join(config_path, start_path)
    if isdir(default_path):
        return default_path
    trimmed_path = join(dirname(config_path), start_path)
    if isdir(trimmed_path):
        return trimmed_path
    return None

def get_paths_for_plugin(plugin_name):
    __validate_plugin_name(plugin_name)
    plugin_paths = []
    for config_path in CSC.get_all_config_locations():
        resolved_path = __resolve_plugin_path(plugin_name, config_path)
        if resolved_path:
            plugin_paths.append(resolved_path)
    return list(set(plugin_paths))

def find_process_path(find_full_proc_name, main_proc_name):
    if find_full_proc_name:
        return shutil.which(main_proc_name)
    return main_proc_name
