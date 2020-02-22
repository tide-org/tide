features
[ ] implement environment variables as tide variables - allow to call a file from vim/atom command line
[ ] add internal variables that can be used for things - e.g. path locations
[ ] allow interpolation in settings - e.g file location for source
[ ] only run buffer commands for open buffers - check editor what buffers are open

languages
[ ] implement plugin for dotnet core
[ ] implement plugin for go

nomenclature
[ ] rename references from commands to instructions
[ ] python - function_args vs event_input_args - use function_args.  (also understand and document)

fixes
[ ] allow Tide() to close on .stop() and not keep state
[ ] fix regex_match feeezing test_c_filters when no match after run for vg_locals
[ ] implement correct python logging subsystem - similar to Airflow

[ ] have option to send partial updates to editor to prevent large payloads across the wire - to speed up Atide

refactoring
[ ] use __init__.py files for imports
[ ] put all atide functions in relevant plugins and pass to editor in config_dictionary
[ ] add source to config - as base64 maybe?
[ ] abstract all top-level config fields into a processor to allow user-defined top-level fields with custom logic. (e.g. buffers, commands, filters, etc.)
[ ] look into using async await instead of Thread while loops - https://gist.github.com/debugtalk/3d26581686b63c28227777569c02cf2c

stretch goals
[ ] get working on windows (maybe)

docs
[ ] do a comparison of features between tide and VS Code Debug Adapter Protocol
