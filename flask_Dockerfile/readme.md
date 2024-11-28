# Running this files

1) create directory then create the files inside it  
2) docker build -t custom_flask_img .
3) docker run -d --name flask_container -p5000:5000 custom_node_image (The -p 5000:5000 flag maps port 5000 on your machine to port 5000 in the container.)
4) Visit http://localhost:5000/ in your browser. 

   
