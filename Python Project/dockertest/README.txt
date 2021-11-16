***********************************************************************************************************************************************
TASK C: Dockerise your app
***********************************************************************************************************************************************
Files:

  [1] Dockerfile
  [2] app.py (imports pythonmain.py for functions)
  [3] /templates/my-form.html
  [4] requirements.txt

Steps to build image and run container:

  [1] docker image build -t <dockerimagename> .
      - You can view image by running "docker image ls"
   
  [2] docker run -p 5000:5000 -d <dockerimagename>
      - This should create a docker container, view it by running "docker ps -a"
      - If there are any issues, you can investigate by running "docker inspect <container ID>

  [3] In browser http://0.0.0.0:5000/ -> Add unsorted array in the format "[6, 2, [4, 3], [[[5], None], 1]]" -> Click Submit
