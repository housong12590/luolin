#!/usr/bin/env bash

git pull

docker rm -f luolin

docker rmi -f luolin

docker build -t luolin .

docker run -d --name luolin -p 8011:5000 luolin