# Kafka Streamin #
Follow the steps below to build a Kafka pipeline through Docker 

## Expectations ##
Markup : 1. Docker is installed and setup
         2. MySQL is installed

## Steps: ##

### Start MySQL ###


### Create Database and table ###

### Start Zookeeper ###
docker run --name myzookeeper --restart always zookeeper

### Start Kafka ###
docker run --name mykafkaserver --link myzookeeper:zookeeper apache/kafka

### Create a topic ###
docker exec -it mykafkaserver /opt/kafka/bin/kafka-topics.sh --create --topic atm_transaction --bootstrap-server localhost:9092

### Create the producer ###
producer_atm_data.py

### Create the Consumer ###