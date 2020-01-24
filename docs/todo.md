[ ] implement environment variables as tide variables
[ ] get/test python plugin working in atide
[ ] put all atide functions in relevant plugins and pass to editor in config_dictionary
[ ] python - function_args vs event_input_args - use function_args.  (also understand and document)
[ ] allow interpolation in settings - e.g file location for source
[ ] add internal variables that can be used for things - e.g. path locations
[ ] allow Tide() to close on .stop() and not keep state
[ ] change run_command to use interpolation and convert run_command_string to use run_command
[ ] abstract all top-level config fields into a processor to allow user-defined top-level fields with custom logic. (e.g. buffers, commands, filters, etc.)
[ ] abstract the command_handler into an interface called handler_interface
[ ] fix regex_match feeezing test_c_filters when no match after run for vg_locals
[ ] use __init__.py files for imports
[ ] implement plugin for go
[ ] have option to send partial updates to editor to prevent large payloads across the wire
[ ] get working on windows (maybe)
[ ] only run buffer commands for open buffers - check editor what buffers are open
[ ] look into using async await instead of Thread while loops - https://gist.github.com/debugtalk/3d26581686b63c28227777569c02cf2c
[ ] implement correct python logging subsystem - similar to Airflow
[ ] add templates to config
[ ] add source to config - as base64 maybe?
