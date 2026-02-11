version: '3.8'

services:

  mysql:
    image: mysql:8.0
    container_name: mysql_container
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: flaskdb
    ports:
      - "3307:3306"

  flask:
    build: ./app
    container_name: flask_container
    ports:
      - "5001:5001"
    depends_on:
      - mysql
