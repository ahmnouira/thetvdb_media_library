#

## DEMO

<video width="320" height="240" controls>
  <source src="output.mp4" type="video/mp4">
  not supported.
</video>

![](output.mp4)

## Run

```sh
docker run -d --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root mysql:8
docker rm mysql
mysql -u root -p
# root
```
