import sys
from config import Config
import plugin_helpers as Plugins
import importlib
from action_predicate_base import action_predicate_base

class run_python_function(action_predicate_base):

    def run(self, command_item, buffer_name=''):
        function_file = command_item["function_file"]
        function_name = command_item["function_name"]
        input_args = command_item.get("input_args", {})
        set_on_return = command_item.get("set_on_return", None)
        functions_path = Plugins.resolve_plugin_path('functions')
        if functions_path not in sys.path:
            sys.path.insert(0, functions_path)
        function_module_name = function_file.replace(".py", "")
        function_module = importlib.import_module(function_module_name)
        function = getattr(sys.modules[function_module_name], function_name)
        interpolated_input_args = {}
        for key, value in input_args.items():
            interpolated_input_args[key] = Config().get()["variables"][value]
        function_result = function(**interpolated_input_args)
        if set_on_return:
            Config().get()["variables"][set_on_return] = function_result