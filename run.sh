#!/bin/bash

echo "Starting Bot"

docker-compose stop bot
docker rm bot
docker build --tag bot:1.0 .
docker-compose up -d bot
docker logs -f bot

echo "Done"
