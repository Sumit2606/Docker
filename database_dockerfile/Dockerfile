FROM mysql
MAINTAINER sumit
ENV MYSQL_ROOT_PASSWORD sumit2606
EXPOSE 3306
COPY mysqlfile.sh /docker-entrypoint-initdb.d/mysqlfile.sh
RUN chmod +x docker-entrypoint-initdb.d/mysqlfile.sh
CMD ["mysqld"]
