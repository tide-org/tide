[ ] refactor action_name and type in Action and ConfigCommandItem
[ ] consoloidate filter, action and editor_wrapper classes find files functionality into separate class
[ ] implement correct python logging subsystem
[ ] complete SysPathContainer and tests
[ ] create a CommandProcessSettings object for config settings in CommandProcess __init__
[ ] add makefile for all commands
[ ] place logical components into separate folders
[ ] create a filter path helpers class filter_paths
[ ] rework config command stuff into smaller, more manageable classes. add tests
[ ] refactor out dict checks in run_command
[ ] refactor run_config_command to be smaller and testable
[ ] fix recursive info registers when added to do_buffer_diff in assembly config
    and refactor command comfig item to allow any type of config command in event_args
[ ] fix vg_registers not updating for stdio on stepi command
  {"command":{"action":"set_config_dictionary_item","value":""},"sender":"editor","receiver":"tide","has_callback":false,"event_id":"102722b2-c158-497b-ae54-45b4646a7f5e"}
[ ] add more fine-grained unit tests
[ ] clean up having both function_args and event_input_args in function_args (possibly rename) ./defaults/actions/run_editor_function.py
    (see test_c info_source vs set_highlight_line)
[ ] make option for commands to not show for users (user_callable) for atide
[ ] export editor function code to editor.
[ ] move all plugin functions to plugin/functions path
[ ] add linting and docker container for this
[ ] create a build pipeline in shippable.io
[ ] look into using async await instead of Thread while loops - https://gist.github.com/debugtalk/3d26581686b63c28227777569c02cf2c
[?] add tests and config for buffers
[ ] implement tcp/ip as alternative to pexpect (to allow other remote debuggers to integrate into tide)
[ ] write a setup tutorial
[ ] write documentation
[ ] rename editor references to interface
[ ] create a tcpip editor_wrapper
