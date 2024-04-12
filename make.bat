@echo off

rem Define the commands for each action
set COMMAND_RUN=python manage.py runserver
set COMMAND_TEST=python manage.py test
set COMMAND_LINT=black . & pep8 .

rem Check the first argument (the action to perform)
if "%1" == "run" (
    %COMMAND_RUN%
) elseif "%1" == "test" (
    %COMMAND_TEST%
) elseif "%1" == "lint" (
    %COMMAND_LINT%
) else (
    echo Invalid command. Use 'run', 'test' or 'lint'.
)
