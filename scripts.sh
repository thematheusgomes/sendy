# set -e
ENVPATH=".venv"
VLOCK="0"
PROJECT="sendy"
OLDPYTHONPATH=''

function py-env() {
    echo "py-env..."
    if [ ! -d "$ENVPATH" ]; then
        echo "creating virtualenv..."
        virtualenv -p python3 $ENVPATH
    fi
    if [ "$VLOCK" = "1"  ]; then
        echo "VLOCK is set! ignoring export PYTHONPATH and source $ENVPATH/bin/activate"
    fi
    if [ "$VLOCK" = "0" ]; then
        VLOCK="1"
        OLDPYTHONPATH=$PYTHONPATH
        echo "activate environment..."
        export PYTHONPATH=$PYTHONPATH:${PWD}/.venv/bin/python:${PWD}/src:${PWD}
        source $ENVPATH/bin/activate
    fi
}

function py-d-env() {
    if [ "$VLOCK" = "1"  ]; then
        export PYTHONPATH=$OLDPYTHONPATH
        VLOCK="0"
        deactivate
    fi
}
