from singleton import singleton
from logging_decorator import logging
from config_base import ConfigBase
from config_base_buffers import ConfigBaseBuffers
from config_base_commands import ConfigBaseCommands
from config_base_events import ConfigBaseEvents
from config_base_internal import ConfigBaseInternal
from config_base_settings import ConfigBaseSettings
from config_base_variables import ConfigBaseVariables

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
