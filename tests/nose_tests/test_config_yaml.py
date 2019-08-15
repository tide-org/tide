import setup_tests
from nose import with_setup
import os

os.environ["TIDE_CONFIG_LOCATION"] = "/work/plugins/test_hello"
from tide import Tide

class TestHelloWorldYaml():

    def test_object_is_type_tide(self):
        tide_object = Tide()
        assert type(tide_object) == Tide
