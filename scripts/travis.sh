#!/usr/bin/env bash
#
# Builds the documentation.
#
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"/../
cd "${DIR}" || exit 1
python setup.py pep8 || exit 1
python setup.py pyflakes || exit 1
./scripts/test.sh || exit 1

