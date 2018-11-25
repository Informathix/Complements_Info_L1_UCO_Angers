#!/bin/bash
ARG=$1
mypy $ARG;
RESULT=$?
if [ $RESULT -eq 0 ]; then
    python $ARG
fi
