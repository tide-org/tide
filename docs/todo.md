[ ] change run_command to use interpolation and convert run_command_string to use run_command
[ ] rename references from commands to instructions
[ ] add templates to config
[ ] fix tide crashing after make vim_python finishes debugging
[ ] have option to send partial updates to editor to prevent large payloads across the wire - to speed up Atide
[ ] implement environment variables as tide variables
[ ] add internal variables that can be used for things - e.g. path locations
[ ] put all atide functions in relevant plugins and pass to editor in config_dictionary
[ ] python - function_args vs event_input_args - use function_args.  (also understand and document)
[ ] allow interpolation in settings - e.g file location for source
[ ] allow Tide() to close on .stop() and not keep state
[ ] abstract all top-level config fields into a processor to allow user-defined top-level fields with custom logic. (e.g. buffers, commands, filters, etc.)
[ ] fix regex_match feeezing test_c_filters when no match after run for vg_locals
[ ] use __init__.py files for imports
[ ] implement plugin for go
[ ] get working on windows (maybe)
[ ] only run buffer commands for open buffers - check editor what buffers are open
[ ] look into using async await instead of Thread while loops - https://gist.github.com/debugtalk/3d26581686b63c28227777569c02cf2c
[ ] implement correct python logging subsystem - similar to Airflow
[ ] add source to config - as base64 maybe?
