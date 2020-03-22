#!/bin/bash
hn=`hostname -I`
unset XDG_RUNTIME_DIR
~/.local/bin/jupyter-lab --no-browser --ip=$hn --port=8080

