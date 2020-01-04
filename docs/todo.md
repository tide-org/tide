[ ] add print to stdout logging function using colourised tty [INFO] [module] [message] ..
[ ] add option for logging to output to a buffer_cache instead of stdout
[ ] fix assembly not stepping through to third page of disassembly
[ ] fix regex_match feeezing test_c_filters when no match after run for vg_locals
[ ] have ability for buffer to be able to set filter by name (would override filter for buffer if it exists)
[ ] have the ability to show info at startup for settings, etc.
    and have ability to log actions, filters, functions, etc to a buffer to make debugging easier
[ ] implement plugin for python
[ ] fix buffer jitter in atide on vg_code
[ ] use __init__.py files for imports
[ ] fix up tests for command_handler_2
[ ] implement plugin for go
[ ] have option to send partial updates to editor to prevents large payloads across the wire
[ ] test on linux
[ ] get working on windows (maybe)
[ ] only run buffer commands for open buffers - check editor what buffers are open
[ ] look into using async await instead of Thread while loops - https://gist.github.com/debugtalk/3d26581686b63c28227777569c02cf2c
[ ] implement correct python logging subsystem
[ ] add templates to config
