import os
import sys
from os.path import abspath, join, isdir, dirname
from yamlreader import yaml_load
import tide.utils.config_source as Cs

VALID_PLUGIN_NAMES = [
    'actions',
    'config',
    'editor_wrappers',
    'filters',
    'functions',
    'templates'
]

def resolve_plugin_path(plugin_name, config_path):
    validate_plugin_name(plugin_name)
    start_path = get_start_path(plugin_name, config_path)
    if isdir(start_path):
        return abspath(start_path)
    if start_path:
        plugin_path = get_plugin_path(start_path, config_path)
        if isdir(plugin_path):
            return abspath(plugin_path)

def validate_plugin_name(plugin_name):
    if plugin_name not in VALID_PLUGIN_NAMES:
        raise RuntimeError(f"error: plugin name: {plugin_name} is invalid")

def get_start_path(plugin_name, config_path):
    config_object = yaml_load(config_path)
    return config_object.get("settings", {}).get("plugins", {}).get(plugin_name + "_path", '')

def get_plugin_path(start_path, config_path):
    default_path = join(config_path, start_path)
    if isdir(default_path):
        return default_path
    trimmed_path = join(dirname(config_path), start_path)
    if isdir(trimmed_path):
        return trimmed_path
    raise RuntimeError(f"error: unable to get plugin path for: {str(config_path)} and: {str(start_path)}")

def get_tide_base_path():
    join_paths = get_python_scripts_base_path(), ".."
    return join(*join_paths)

def get_python_scripts_base_path():
    return abspath(join(dirname(os.path.realpath(__file__)), ".."))

def get_paths_for_plugin(plugin_name):
    validate_plugin_name(plugin_name)
    plugin_paths = []
    for config_path in Cs.CONFIG_LOCATION_ARRAY:
        resolved_path = resolve_plugin_path(plugin_name, config_path)
        if resolved_path:
            plugin_paths.append(resolved_path)
    return plugin_paths
