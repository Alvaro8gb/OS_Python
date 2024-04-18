1. Create the docker File
 ```Dockerfile 
FROM python:3.10

WORKDIR /my-project
ADD . /my-project

EXPOSE 8000
ENTRYPOINT ["python", "/my-project/server.py"]  
```

2. Build the image

**Ensure you are in this directory**

```bash
docker build -t my-image .     
```

3. Run the image
```bash
 docker run -it --name container1 -p 9000:8000 my-image
 ```
For running in the background

```bash
 docker run -d -it --name container1 -p 9000:8000/udp my-image
 ```

4. Check conection 

```bash
nc -u  localhost 9000 

```

 ## Other tools

 - check if a port is free
 ```
 netstat -tuln | grep 9000
 ```
