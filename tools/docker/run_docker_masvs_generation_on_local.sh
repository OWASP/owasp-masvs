#!/bin/bash

# NOTE: You can run this script on your local machine e.g. macOS where Docker is installed.

set -euo pipefail

if [ -z ${1+x} ]
then
      VERSION="SNAPSHOT"
else
      VERSION=$1
fi

echo "Version = ${VERSION}"

export IMG="owasp/masvs-docgenerator:0.1"

docker pull $IMG

for folder in ./Document*; do
  echo "Generating $folder"
  [ -f $folder-temp ] && rm -rf $folder-temp
  cp -r $folder $folder-temp
  docker run --rm -u `id -u`:`id -g` -v ${PWD}:/pandoc $IMG "/pandoc_makedocs.sh $folder-temp ${VERSION}" || echo "$folder failed" &

done

wait

echo "Cleaning up"
for folder in Document*; do
    if [ -d "$folder-temp" ]; then 
        rm -Rf $folder-temp
    fi
done