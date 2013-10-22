#!/usr/bin/env bash
#
# Runs coverage.
#
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"/../
cd "${DIR}" || exit 1
coverage run --source=lazarus setup.py test || exit 1
coverage report -m || exit 1

