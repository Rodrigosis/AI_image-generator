docker build --tag=jupyter-docker:python . 

docker create -t -i --name conteiner-jupyter -p 4000:4000 -v C:\Users\rodri\vs_code\jupyter_docker:/home/user jupyter-docker:python 

docker start conteiner-jupyter 

docker exec -it conteiner-jupyter bash 

jupyter notebook --ip 0.0.0.0 --port 4000 --allow-root 
