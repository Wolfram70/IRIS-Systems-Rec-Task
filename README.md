# IRIS Systems Recruitment Task
This is the repository for the IRIS Systems Recruitment Task. Each task has its own branch and README file explaining the method used and all the steps taken to achieve it in further detail.<br>
The tasks involved are:
## 1. Dockerizing the Rails Application
This task involves writing a dockerfile and a <code>docker-compose.yaml</code> file to build and run a container of the application with docker. More details can be found [here](https://github.com/Wolfram70/IRIS-Systems-Rec-Task/blob/fbba3cd157b6425fbf98c630cf8f4f7b80fccc17/README.md).
## 2. Configuring a Reverse Proxy
This task involves configuring a reverse proxy with <code>nginx</code>. More details can be found [here](https://github.com/Wolfram70/IRIS-Systems-Rec-Task/blob/2820a6579b5198a88ab91ab68078495ef0a95d92/README.md).
## 3. Enabling Data Persistence
This task involves enabling data persistence to ensure data isn't lost between different sessions when the database container is down. More details can be found [here](https://github.com/Wolfram70/IRIS-Systems-Rec-Task/blob/a2083cc6c922f00207623c1e6f0bc0a76e204118/README.md).
## 4. Load Balancing
This task involves creating multiple containers running the application and configuring load balancing with the hekp of <code>nginx</code>. More details can be found [here](https://github.com/Wolfram70/IRIS-Systems-Rec-Task/blob/33626cbb8007e9b3f449141da72f4d4114174552/README.md).
## 5. Rate Limiting
This task involves configuring a request rate limit using <code>nginx</code>. More details can be found [here](https://github.com/Wolfram70/IRIS-Systems-Rec-Task/blob/bc4ecaec3132d74e13fa3ec711c4a7caf84ac024/README.md).
## 6. Backup Daemon
THis task involves creating a new containe running a backup daemon script to take timely backups of data. More details can be found [here](https://github.com/Wolfram70/IRIS-Systems-Rec-Task/blob/6c75f50c3ec8a76ec713274e219089a0c6c760a5/README.md).
## Bonus Task
This task involves setting up a GitHub CI/CD pipeline to automatically build and push the images to dockerhub and then initiate a fake deployment to a private server using [FakeDeployServer](https://github.com/Utkar5hM/FakeDeployServer/blob/main/index.js). More details can be found [here](https://github.com/Wolfram70/IRIS-Systems-Rec-Task/blob/90e3f193a019d0e9460913357a95ce6b74faa3fb/README.md).
