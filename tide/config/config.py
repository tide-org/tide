from tide.utils.singleton import singleton
from tide.logging_decorator import logging
from tide.config.config_base import ConfigBase
from tide.config.config_base_buffers import ConfigBaseBuffers
from tide.config.config_base_commands import ConfigBaseCommands
from tide.config.config_base_events import ConfigBaseEvents
from tide.config.config_base_internal import ConfigBaseInternal
from tide.config.config_base_settings import ConfigBaseSettings
from tide.config.config_base_variables import ConfigBaseVariables

@singleton
@logging
class Config(ConfigBase,
             ConfigBaseSettings,
             ConfigBaseBuffers,
             ConfigBaseEvents,
             ConfigBaseCommands,
             ConfigBaseInternal,
             ConfigBaseVariables):
    pass
