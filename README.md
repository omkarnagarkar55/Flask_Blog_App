# Flask Blog Application

This repository contains a Python-Flask blogging application that is deployed on a Docker container.


## 1. Create a Docker File:-

* To containerize our Flask application, we'll start by creating a Dockerfile.

![image](https://github.com/omkarnagarkar55/Flask_Blog_App/assets/60735358/a0f65ed4-e598-4f5f-a7ad-cec273b12e93)


## 2. Build a Docker Container:-

* Navigate to the directory containing your Dockerfile and execute: docker build -t flask_blog_app .
* This will create a Docker image named flask_blog_app.

![image](https://github.com/omkarnagarkar55/Flask_Blog_App/assets/60735358/9c3c2177-80dd-4cc6-bafb-548f3012048d)


## 3. Check for the Docker Image:-

* To ensure your image has been built: docker images ls

![image](https://github.com/omkarnagarkar55/Flask_Blog_App/assets/60735358/cab22f29-00f7-400e-93e9-d3709d138c93)


## 4. Run the Docker Container:-

* Start a container instance using the image: docker run -p 8080:5000 flask_blog_app
* This maps port 8080 on your host to port 5000 on the container.

![image](https://github.com/omkarnagarkar55/Flask_Blog_App/assets/60735358/ecca9902-186a-4c74-8451-324922c9b39e)


## 5. Access the Application:-

* Open a web browser and navigate to: http://localhost:8080 

![image](https://github.com/omkarnagarkar55/Flask_Blog_App/assets/60735358/9353a767-e228-451b-a442-7b2120fe32a3)


## 6. Execute Test on Docker:-

* If you have tests written for your Flask application, you can execute them within the Docker Container.
  
![image](https://github.com/omkarnagarkar55/Flask_Blog_App/assets/60735358/c3a9a129-5f40-4e8f-a575-3c075e6c0fc9)


## 7. Push Docker image to Docker Hub:-

* First, log in to Docker Hub: docker login
* Then, push your image: docker push [username ]/flask_blog_app

![image](https://github.com/omkarnagarkar55/Flask_Blog_App/assets/60735358/fc00ef3b-dc0f-4acd-b1d2-9308d2911034)

## 8. Docket Hub Results:-

* You can view and manage your Docker image on Docker Hub:

Link to docker hub image - https://hub.docker.com/repository/docker/omkarnagarkar55/flask_blog_app/general 

![image](https://github.com/omkarnagarkar55/Flask_Blog_App/assets/60735358/de751dca-8c1f-4f16-82e1-ba908074aee7)






