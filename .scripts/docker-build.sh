#!/usr/bin/env bash

# Get the directory of this script.
# Will be relative to pwd if script was called as such
SCRIPT_PATH=${0%/*}

DOCKER_BUILDKIT=1 docker build \
  -t gps-stuff:latest \
  .
