class Tide(object):

    def __init__(self):
        import initialise as Init
        _startup_commands = ''
        _command_handler = None
        Init.initialise_startup_classes()

    def start(self, commands=''):
        try:
            from command_handler import CommandHandler
            self._startup_commands = commands
            self._command_handler = CommandHandler()
            self._command_handler.spawn_process(commands)
        except Exception as ex:
            import traceback
            print("error in Tide.start(): " + str(ex))
            print(traceback.format_exc())

    def stop(self):
        import initialise as Init
        self._command_handler.close_command_handler()
        del self._command_handler
        Init.cleanup()

    def run_config_command(self, command, buffer_name='', event_input_args_name=''):
        from config_command_item import ConfigCommandItem
        from config_command import ConfigCommand
        config_command_item = ConfigCommandItem()
        config_command_item.command = command
        config_command_item.buffer_name = buffer_name
        config_command_item.event_input_args_name = event_input_args_name
        ConfigCommand().run_config_command(config_command_item)
