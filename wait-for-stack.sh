#!/bin/bash

set -exu

for i in {1..5}; do
    curl "http://$DOCKER_IP:8000" && curl "http://$DOCKER_IP:4444" && break; sleep 5
done
