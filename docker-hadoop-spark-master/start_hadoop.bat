#!/bin/bash

docker network inspect disable_ipv6 || docker network create --driver bridge --ipv6=false disable_ipv6
	
docker compose -f docker-compose.yml up -d
