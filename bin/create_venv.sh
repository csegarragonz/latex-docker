#!/bin/bash

set -e

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]:-${(%):-%x}}" )" >/dev/null 2>&1 && pwd )"
PROJ_ROOT=${THIS_DIR}/..
VENV_PATH="${PROJ_ROOT}/venv"

PIP=${VENV_PATH}/bin/pip3
PYTHON=python3

function pip_cmd {
    source ${VENV_PATH}/bin/activate && ${PIP} "$@"
}

pushd ${PROJ_ROOT} >> /dev/null

if [ ! -d ${VENV_PATH} ]; then
    ${PYTHON} -m venv ${VENV_PATH}
fi

pip_cmd install -U pip
pip_cmd install -U setuptools
pip_cmd install -r requirements.txt

popd >> /dev/null
