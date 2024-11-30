1.create directory then create the files inside it
2.docker build -t custom_mysql_img .
3.docker run -d --name mysql_cont -e MYSQL_ROOT_PASSWORD=sumit2606 custom_mysql_img
4.docker exec -it mysql_cont /bin/bash
5.check the database and content in it.
