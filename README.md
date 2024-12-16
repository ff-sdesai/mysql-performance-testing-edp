# mysql-performance-testing-edp
mysql-performance-testing-edp



# local setup

### Repo setup
* clone repo && cd mysql-performance-testing-edp
* poetry install
* poetry shell
* cd myapi
* python manage.py migrate -- run migration to update DB
* python manage.py runserver



### Docker Setup: 
* docker run --name mysql-db -e MYSQL_ROOT_PASSWORD=rootpassword -e MYSQL_DATABASE=exampledb -p 4040:3306 -d mysql:8

* docker exec -it mysql-db mysql -u root -p


### Migration command
* python manage.py makemigrations -- make new migration
* python manage.py migrate -- run migration to update DB

### Run local server
* python manage.py runserver


### errors:
* Exception: Can not find valid pkg-config name.Specify MYSQLCLIENT_CFLAGS and MYSQLCLIENT_LDFLAGS env vars manually <br>
 Solution: `brew install mysql pkg-config`


### API avilable:
- GET: http://127.0.0.1:8000/api/devices/ 
- POST: http://127.0.0.1:8000/api/devices/ 
```
sample request body:
{
  "tenant_id": 101,
  "device_type": "Sensor",
  "column_1": "Value1",
  "column_2": "Value2",
  "column_3": "Value3",
  "column_4": "Value4",
  "column_5": "Value5",
  "column_6": "Value6",
  "column_7": "Value7",
  "column_8": "Value8",
  "column_9": "Value9",
  "column_10": "Value10"
}

```
