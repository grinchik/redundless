#!/bin/bash

set -o nounset;
set -o errexit;
set -o pipefail;

readonly STARTING_POINT="$1";
readonly THREAD_NUMBER="$2";

find \
    "${STARTING_POINT}" \
    -type f \
    -print0 \
| \
xargs \
    -0 \
    --max-procs "${THREAD_NUMBER}" \
    sha256sum \
;
