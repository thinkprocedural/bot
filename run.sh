#!/bin/bash

echo "Starting Bot"

docker-compose stop bot
docker-compose up -d bot
docker logs -f bot

echo "Done"
