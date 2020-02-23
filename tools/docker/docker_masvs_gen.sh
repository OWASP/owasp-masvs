#!/bin/bash

set -euo pipefail

VERSION=$1 # e.g. 1.2

export IMG="masvs-generator:latest"

if [[ "$(docker images -q $IMG 2> /dev/null)" == "" ]]; then
  docker build --tag $IMG .
fi

for folder in ./Document*; do
  echo "Generating $folder"
  docker run --rm -u `id -u`:`id -g` -v ${PWD}:/pandoc $IMG "/pandoc_makedocs.sh $folder $VERSION" || echo "$folder failed" &
done

wait