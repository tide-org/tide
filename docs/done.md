[n] Move startup logic out of `from tide import Tide` and place in `Tide.__init__`
[x] add callbacks from editor
[x] implement receiver: "tide" in stdio stdin for atide
[x] add non-blocking infinite loop to cli
[x] convert tests from nose to pytest
[x] run tests in a docker container
[x] add simple tests based on stdio and to build an understanding of how config items should work
[x] implement startup complete callback
[x] fix startup_complete showing in atide - library issue
[x] fix stdio reading to handle doing all buffer startup
[x] implement local server for IDEs that don't have python integrated
[x] abstract all vim-related code:
  - `./defaults/actions/set_buffer.py`
[x] `update internal._buffer_caches` for template buffers
[x] stop stdio read taking up all processor
[x] do tracing on tide package to determine what is holding package open after shutdown
[x] implement a shutdown/stop_tide call
[x] do cleanup in test_config_yaml.py correcly
[x] move stdio functions to under editor_wrappers 
[x] move stdio editor functions into folder under editor_wrappers
[n] use object in stdio request and response objects
[n] move common classes into module paths - action, command, config, editor, filter, logging, helpers
[n] implement shutdown/stop command from editor
[n] move filters into config. convert code to regexes or code in yaml.
[n] ability to define filters in config as well as files - to use a parser - https://en.wikipedia.org/wiki/Compiler-compiler - and - https://en.wikipedia.org/wiki/Yacc
[x] fix tests
[x] write more tests
[x] add tests for callbacks
[x] determine tests to be created for stdio and add config
[x] move to github.com/tide
[x] fix log.py permission denied when file to write to is set without a path
[x] fix function_args in function_args with stdio
[x] allow editor type to be set on startup
[x] move before_command, command and after_command to tide from vgdb (and so it doesn't need to be implemented in atide)
[x] remove function_args showing in input_args with stdio
[?] reconcile missing buffer_name 
