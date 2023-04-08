# Configuring Reverse Proxy with nginx

A new folder <code>docker/web</code> is created to store the <code>nginx</code> container dockerfile and the configuration file.<br>
However, there are a few changes made in <code>docker-compose.yaml</code> related to the <code>employee-app</code> service. Primarily, the <code>ports</code> section is removed and no ports of the container are exposed to the host machine since all the requests will be handled by the <code>nginx</code> container which will internally forward the connection to the server.

## Reverse Proxy
The dockerfile for the image is stored at <code>docker/web/Dockerfile</code> and the configuration is stored at <code>docker/web/nginx.conf</code>.

### Dockerfile
For the container, the base image is chosen to be <code>nginx:latest</code>. The required utility tools are installed with:
```
RUN apt-get update -qq && apt-get -y install apache2-utils
```
A log directory is created with:
```
RUN mkdir log
```
The required files (mainly the nginx configuration file) is copied to the appropriate directory:
```
COPY public public/
COPY docker/web/nginx.conf /etc/nginx/nginx.conf
```
The following <code>EXPOSE</code> line in the file is stricly not needed since the <code>ports</code> section of <code>docker-compose.yaml</code> handles exposing the required ports to the host machine.<br>
Lastly, the reverse proxy server is started with:
```
CMD ["nginx", "-g", "daemon off;"]
```
### nginx.conf
Since, the protocol used is <code>http</code>, the required configuration details are enclosed in <code>http {...}</code>. The upstream (named <code>web</code>) is defined to be the application service which is <code>employee-app</code> which is listening for requests at port <code>8080</code> (for this task, the Dockerfile for <code>employee-app</code> has been edited and the rails application is launched at port <code>8080</code> of the container). This is done with:
```
upstream web {
    server employee-app:8080;
}
```
The <code>nginx</code> reverse proxy server is configured to listen for requests at port <code>8090</code> and pass all requests to <code>http://web</code> (earlier defined to be our application server). Optionally, additional headers are added to give more information to the application server about the request recieved and error and access logs are also created to view additional information later. This is done with:
```
server {
    listen 8090;

    access_log /app/log/nginx.access.log;
    error_log /app/log/nginx.error.log;

    location / {
        proxy_pass http://web;
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_redirect off;
    }
}
```
### docker-compose.yaml
A new service called <code>web</code> is created. This is similar in configuration to the application service where the context is defined to be the application root directory since the Dockerfile is present in a subfolder.<br>
The <code>depends_on</code> section is added to include the <code>employee-app</code> service to ensure this container starts running only after the other one. The port <code>8090</code> of the container (where it was configured to listen) is exposed to the host at port <code>8080</code>. This is done with:
```
build:
    context: .
    dockerfile: ./docker/web/Dockerfile
depends_on:
    - employee-app
ports:
    - 8080:8090
```
Lastly, the container is set to always restart in the event that it stops at any time with:
```
restart:
    always
```
## Screenshots
### The three containers running:
![Kiku](Screenshots/terminal.png)
### The application accessed at <code>localhost:8080</code>:
![Kiku](Screenshots/running.png)