flask:
  build: ./app
  container_name: flask_container
  ports:
    - "5001:5001"
  depends_on:
    - mysql
