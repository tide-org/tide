[ ] add more fine-grained unit tests
[ ] remove function_args showing in input_args with stdio
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
