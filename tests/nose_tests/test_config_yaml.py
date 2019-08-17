import setup_tests
from nose import with_setup
import os
from nose.tools import timed

os.environ["TIDE_CONFIG_LOCATION"] = "/work/plugins/test_hello"
from tide import Tide

class TestHelloWorldYaml():

    def test_object_is_type_tide(self):
        tide_object = Tide()
        assert type(tide_object) == Tide

    @timed(10)
    def test_tide_can_start(self):
        tide_object = Tide()
        tide_object.start()
        assert type(tide_object) == Tide

    @timed(10)
    def test_tide_can_start(self):
        tide_object = Tide()
        tide_object.start()
        tide_object.run_config_command('do_hello')
        assert type(tide_object) == Tide
