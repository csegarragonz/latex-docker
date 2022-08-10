#!/bin/bash

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
PROJ_ROOT="${THIS_DIR}/.."
VENV_PATH="${PROJ_ROOT}/venv"

pushd ${PROJ_ROOT} >> /dev/null

# ----------------------------
# Virtualenv
# ----------------------------

if [ ! -d ${VENV_PATH} ]; then
    ${PROJ_ROOT}/bin/create_venv.sh
fi

export VIRTUAL_ENV_DISABLE_PROMPT=1
source ${VENV_PATH}/bin/activate

# ----------------------------
# Invoke tab-completion
# (http://docs.pyinvoke.org/en/stable/invoke.html#shell-tab-completion)
# ----------------------------

_complete_invoke() {
    local candidates
    candidates=`invoke --complete -- ${COMP_WORDS[*]}`
    COMPREPLY=( $(compgen -W "${candidates}" -- $2) )
}

complete -F _complete_invoke -o default invoke inv

# ----------------------------
# Environment vars
# ----------------------------

VERSION_FILE=${PROJ_ROOT}/VERSION
export CODE_VERSION=$(cat ${VERSION_FILE})
export PS1="(latex-docker) $PS1"

# -----------------------------
# Splash
# -----------------------------

echo ""
echo "----------------------------------"
echo "LaTeX-Docker Dev. CLI"
echo "Version: ${CODE_VERSION}"
echo "Project root: ${PROJ_ROOT}"
echo "----------------------------------"
echo ""

popd >> /dev/null
