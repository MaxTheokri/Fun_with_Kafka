# Kafka Streamin #
Follow the steps below to build a Kafka pipeline through Docker 

## Expectations ##
Markup : 1. Docker is installed and ready to go
 

## Steps: ##

### Start MySQL ###
Run the following commands
*docker run --name atm-db -p 3306:3306 -e MYSQL_ROOT_PASSWORD=MY_PASSWORD -d mysql:8.4*
*docker exec -it atm-db /bin/bash*
*mysql -p*
Enter the password created with docker run
*CREATE DATABASE atm;*
*CREATE TABLE 

### Create Database and table ###

### Start Zookeeper ###
*docker run --name myzookeeper --restart always zookeeper*

### Start Kafka ###
*docker run --name mykafkaserver --link myzookeeper:zookeeper apache/kafka*

### Create a topic ###
*docker exec -it mykafkaserver /opt/kafka/bin/kafka-topics.sh --create --topic atm_transaction --bootstrap-server localhost:9092*

### Create the producer ###
producer_atm_data.py

### Create the Consumer ###
atm_data_reader.py


## References ##
MySQL Docker: https://hub.docker.com/_/mysql