import tide.utils.config_source_config as CSC
import tide.utils.python_files as Pf

CONFIG_OBJECT = CSC.get_all_configs()
FUNCTIONS_LOCATION_ARRAY = Pf.get_valid_files_from_paths_for_plugin_and_add_to_sys_path("functions", False, True)
