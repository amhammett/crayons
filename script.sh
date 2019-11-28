#!/usr/bin/env bash

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
script_cwd="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"

color_list_file=${script_cwd}/colors.ini

## if auto color, set color based on terminals (pid) and their color

color_list () {
  match=$1
  match_color="default"

  if [[ -z ${match} ]]; then
    echo "found the following colors:"
  fi

  while IFS="" read -r color || [ -n "$color" ]
  do
    name=$(echo ${color} | cut -d ':' -f1)
    value=$(echo ${color} | cut -d ':' -f2)

    if [[ -z ${match} ]]; then
      # printf '%s\n' "$color"
      echo "[${value}] ${name}"
    fi

    if [[ "${match}" == "${name}" ]]; then
      # echo "found match ${match} and ${name}"
      match_value=$value
    fi
  done < $color_list_file

  return $match_value
}

color_get () {
  osascript -e 'tell application "Terminal" to get background color of window 1'
}

terminal_set_color () {  
  target_color=$1
  color_list "${target_color}"
  target_value=$?

  osascript -e "tell application \"Terminal\"" -e "set current settings of window 1 to settings set ${target_value}" -e "end tell"
}

parse_arguments () {
  while [[ "$#" -gt 0 ]]; do
    case $1 in
      ls|list) local list=1;;
      s|set) local set=1; color="$2"; shift;;
      g|get) local get=1;;
      d|default) local default=1;;
      *) echo "Unknown parameter passed: $1"; exit 1;;
    esac
    shift
  done

  if [[ -n ${list} ]]; then
    color_list
  fi

  if [[ -n ${get} ]]; then
    color_get
  fi

  if [[ -n ${set} ]]; then
    # echo "calling terminal set color ${color}"
    terminal_set_color "${color}"
  fi

  if [[ -n ${default} ]]; then
    terminal_set_color default
  fi
}

parse_arguments "$@"
