[ ] fix python plugin not setting breakpoint and continue not running
[ ] fix vg_template updating after step for test_c - showing old line numbers e.g. 6 instead of 7
[ ] implement environment variables as tide variables
[ ] create a dev environment setup section to the Makefile - install all other repos, dependencies, etc.
[ ] allow interpolation in settings - e.g file location for source
[ ] add internal variables that can be used for things - e.g. path locations
[ ] allow run_command_with_match to match on multiple groups in line for array - e.g in python break lists breakpoints and line and filename need to be caught together
[ ] allow Tide() to close on .stop() and not keep state
[ ] change run_command to use interpolation and convert run_command_string to use run_command
[ ] abstract all top-level config fields into a processor to allow user-defined top-level fields with custom logic.
[ ] abstract the command_handler into an interface called handler_interface
[ ] fix regex_match feeezing test_c_filters when no match after run for vg_locals
[ ] fix buffer jitter in atide on vg_code
[ ] use __init__.py files for imports
[ ] implement plugin for go
[ ] have option to send partial updates to editor to prevent large payloads across the wire
[ ] get working on windows (maybe)
[ ] only run buffer commands for open buffers - check editor what buffers are open
[ ] look into using async await instead of Thread while loops - https://gist.github.com/debugtalk/3d26581686b63c28227777569c02cf2c
[ ] implement correct python logging subsystem - similar to Airflow
[ ] add templates to config
[ ] add source to config
