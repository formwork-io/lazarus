#!/usr/bin/env bash
#
# Builds the documentation.
#
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"/../
cd "${DIR}" || exit 1
make clean docs || exit 1

