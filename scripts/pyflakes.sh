#!/usr/bin/env bash
#
# Executes pyflakes check.
#
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"/../
cd "${DIR}" || exit 1
echo "Running pyflakes check."

PYFLAKES_OPTS=""

pyflakes $PYFLAKES_OPTS $(find -name *.py)
PYFLAKES_RC=$?

if [ ${PYFLAKES_RC} -eq 1 ]; then
    echo "FAIL"
elif [ ${PYFLAKES_RC} -eq 0 ]; then
    echo "You did a good job."
fi
exit ${PYFLAKES_RC}

