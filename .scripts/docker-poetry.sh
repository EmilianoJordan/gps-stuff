#!/usr/bin/env bash

# Get the directory of this script.
# Will be relative to pwd if script was called as such
SCRIPT_PATH=${0%/*}

docker compose run shell
_exit_code=$?

# prevents rebuilding the image on error exits.
# you can exit bash `exit 1` to prevent image rebuild.
if [ $_exit_code -eq 0 ]; then
  "$SCRIPT_PATH"/docker-build.sh
else
  echo "\`docker compose run\` exited non 0. Skipping docker build step." 1>&2
fi
