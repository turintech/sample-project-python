#!/bin/bash     

# Import variables
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source "$DIR/variables.sh"

# Populate BUILD with the build command
BUILD="poetry install"
echo "Running build command: $BUILD"
eval $BUILD
