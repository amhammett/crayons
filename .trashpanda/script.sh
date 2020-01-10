#!/usr/bin/env bash
# script: change terminal colors

script_cwd="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
project_path="${script_cwd}/../crayon/"
${project_path}/venv/bin/python3 ${project_path}/src/crayon.py $@
