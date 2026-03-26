#

## DEMO

https://github.com/user-attachments/assets/1f6c718e-1f8c-433d-82fb-1f353b5b4d63

## Run

```sh
docker run -d --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root mysql:8
docker rm mysql
mysql -u root -p
# root
```
