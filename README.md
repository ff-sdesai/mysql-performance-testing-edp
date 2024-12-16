# mysql-performance-testing-edp
mysql-performance-testing-edp



# local setup

### Repo setup
* clone repo && cd mysql-performance-testing-edp
* poetry install
* poetry shell
* cd myapi


### Docker Setup: 
* docker run --name mysql-db -e MYSQL_ROOT_PASSWORD=rootpassword -e MYSQL_DATABASE=exampledb -p 4040:3306 -d mysql:8

* docker exec -it mysql-db mysql -u root -p



