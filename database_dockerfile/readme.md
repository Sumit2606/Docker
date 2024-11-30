1.create directory then create the files inside it <br>
2.docker build -t custom_mysql_img . <br>
3.docker run -d --name mysql_cont -e MYSQL_ROOT_PASSWORD=sumit2606 custom_mysql_img <br>
4.docker exec -it mysql_cont /bin/bash <br>
5.check the database and content in it. <br>
