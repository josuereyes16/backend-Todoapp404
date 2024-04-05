@echo off

rem Define los comandos para cada acción
set COMMAND_RUN=python manage.py runserver
set COMMAND_TEST=python manage.py test
set COMMAND_LINT=black . & pep8 .

rem Verifica el primer argumento (la acción a realizar)
if "%1" == "run" (
    %COMMAND_RUN%
) elseif "%1" == "test" (
    %COMMAND_TEST%
) elseif "%1" == "lint" (
    %COMMAND_LINT%
) else (
    echo Comando no válido. Use 'run', 'test' o 'lint'.
)
