#!/bin/bash

# NOTE: You can run this script on your local machine e.g. macOS where Docker is installed.

set -euo pipefail

VERSION=$1 # e.g. 1.2

export IMG="masvs-generator:latest"

if [[ "$(docker images -q $IMG 2> /dev/null)" == "" ]]; then
  docker build --tag $IMG tools/docker/
fi

for folder in ./Document*; do
  echo "Generating $folder"
  [ -f $folder-temp ] && rm -rf $folder-temp
  cp -r $folder $folder-temp
  docker run --rm -u `id -u`:`id -g` -v ${PWD}:/pandoc $IMG "/pandoc_makedocs.sh $folder-temp $VERSION" || echo "$folder failed" &

done

wait

echo "Cleaning up"
for folder in Document*; do
    if [ -d "$folder-temp" ]; then 
        rm -Rf $folder-temp
    fi
done