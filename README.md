# IRIS Systems Recruitment Task
This is the repository for the IRIS Systems Recruitment Task. Each task has its own branch and README file explaining the method used and all the steps taken to achieve it in further detail.<br>
The tasks involved are:
## 1. Dockerizing the Rails Application
This task involves writing a dockerfile and a <code>docker-compose.yaml</code> file to build and run a container of the application with docker. More details can be found [here](https://github.com/Wolfram70/IRIS-Systems-Rec-Task/blob/ec4c3c2e3639ff19cdbdc388b7acae830bacc560/README.md).
## 2. Configuring a Reverse Proxy
This task involves configuring a reverse proxy with <code>nginx</code>. More details can be found [here](https://github.com/Wolfram70/IRIS-Systems-Rec-Task/blob/7213f626269e3b745b520c1a3d1f576298532765/README.md).
## 3. Enabling Data Persistence
This task involves enabling data persistence to ensure data isn't lost between different sessions when the database container is down. More details can be found [here](https://github.com/Wolfram70/IRIS-Systems-Rec-Task/blob/7637044bf71f4eec29f4d1de3790990103664498/README.md).
## 4. Load Balancing
This task involves creating multiple containers running the application and configuring load balancing with the hekp of <code>nginx</code>. More details can be found [here](https://github.com/Wolfram70/IRIS-Systems-Rec-Task/blob/9cd0d7a4286a3391a9386aa017db5d7b1349783b/README.md).
## 5. Rate Limiting
This task involves configuring a request rate limit using <code>nginx</code>. More details can be found [here](https://github.com/Wolfram70/IRIS-Systems-Rec-Task/blob/c3009216c3bc0fe5665b57533d3cb4dd5390bb85/README.md).
## 6. Backup Daemon
THis task involves creating a new containe running a backup daemon script to take timely backups of data. More details can be found [here](https://github.com/Wolfram70/IRIS-Systems-Rec-Task/blob/90dc5ee32312df9ea30724033983e72be97d6f13/README.md).
## Bonus Task
This task involves setting up a GitHub CI/CD pipeline to automatically build and push the images to dockerhub and then initiate a fake deployment to a private server using [FakeDeployServer](https://github.com/Utkar5hM/FakeDeployServer/blob/main/index.js). More details can be found [here](https://github.com/Wolfram70/IRIS-Systems-Rec-Task/blob/90e3f193a019d0e9460913357a95ce6b74faa3fb/README.md).
