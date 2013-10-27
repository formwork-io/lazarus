#!/usr/bin/env bash
#
# Executes nosetests.
#
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"/../
cd "${DIR}" || exit 1

NOSE_OPTS+="--nocapture "
NOSE_OPTS+="--with-doctest "
NOSE_OPTS+="--doctest-options=+ELLIPSIS "

PYTHONPATH=. nosetests $NOSE_OPTS -v
