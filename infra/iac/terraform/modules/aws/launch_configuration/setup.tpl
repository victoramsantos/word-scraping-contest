#!/bin/bash

yum update -y
amazon-linux-extras install docker -y
service docker start

docker run -d -p 7687:7687 -e NEO4J_AUTH=neo4j/root neo4j:4.1
sleep 25
docker run -d -e NEO4J_URI=bolt://localhost:7687 -e NEO4J_USERNAME=neo4j -e NEO4J_PASSWORD=root --net=host --restart=always ${FRONTEND_IMG}
docker run -d -e NEO4J_URI=bolt://localhost:7687 -e NEO4J_USERNAME=neo4j -e NEO4J_PASSWORD=root -e DEPTH_INTERACTIONS=50 -e FIRST_WORD=amor --net=host ${BACKEND_IMG}
