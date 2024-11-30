create directory then create the files inside it
docker build -t custom_mysql_img .
docker run -d --name mysql_cont -e MYSQL_ROOT_PASSWORD=sumit2606 custom_mysql_img
docker exec -it mysql_cont /bin/bash
check the database and content in it.
