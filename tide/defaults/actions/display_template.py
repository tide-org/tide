import os
import jinja2
from tide.plugin.action_base import action_base
from tide.config.config import Config
import tide.utils.path_helpers as Ph
from tide.print_to_stdout import PrintToStdout as PTS

class display_template(action_base):

    def run(self, command_item, buffer_name=''):
        if buffer_name:
            template_paths = Ph.get_paths_for_plugin('templates')
            template_filename = command_item.get("filename", '')
            PTS.info("DISPLAY_TEMPLATE", template_filename, buffer_name, command_item)
            for templates_path in template_paths:
                template_filename_path = os.path.join(templates_path, template_filename)
                if os.path.isfile(template_filename_path):
                    self.__process_template_file(buffer_name, templates_path, template_filename)
                    break

    def __process_template_file(self, buffer_name, templates_path, template_filename):
        template_loader = jinja2.FileSystemLoader(searchpath=templates_path)
        template_env = jinja2.Environment(loader=template_loader)
        template = template_env.get_template(template_filename)
        config_variables = Config().get_variables()
        output_text = template.render(config_variables)
        if output_text:
            output_text_array = output_text.split('\n')
            Config().set_internal_buffer_cache(buffer_name, output_text_array)
