import sys
import tide.utils.path_helpers as Ph
import tide.utils.config_source_location as CSL
import tide.utils.config_source_locations as CSLS
import tide.utils.config_source_configs as CSC
import tide.utils.sys_path_container as SPC

def __get_function_paths_and_add_to_sys_path():
    function_paths = Ph.get_paths_for_plugin("functions")
    for function_path in function_paths:
        if function_path not in sys.path:
            SPC.insert(function_path)
    return function_paths

FULL_CONFIG_LOCATION = CSL.get_base_config_location()
CONFIG_LOCATION_ARRAY = CSLS.get_all_config_locations()
CONFIG_OBJECT = CSC.get_all_configs(CONFIG_LOCATION_ARRAY)
FUNCTIONS_LOCATION_ARRAY = __get_function_paths_and_add_to_sys_path()
