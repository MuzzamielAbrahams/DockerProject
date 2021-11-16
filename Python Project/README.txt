
Hi There,

This is just a simple application I have created to explore some topics including:

  [1] Bubblesort O(n^2)
  [2] Micro Web Frameworks (Flask)
  [3] Bash scripts to automate starting up the server (If any testing fails the server won't be started)
  [4] Dockerising the application
  
***********************************************************************************************************************************************
TASK A - Creating Application:
***********************************************************************************************************************************************

[1] pythonmain.py, contains the following:

    - bubbleSort()
    - flatten()
    - removeNone()
    - numOfElements()

[2] testscript.py contains unit tests for the above function using "import unittest" module in python

[3] Used mypy as the static code analyser tool - Mypy is a static type checker for Python 3 and Python 2.7. If you sprinkle your code with type annotations, mypy can type check your code and find common bugs. (Used in the automated testing in TASK C)
   
    -> https://mypy.readthedocs.io/en/stable/introduction.html

***********************************************************************************************************************************************
TASK B: Micro Web Framework (Flask):
***********************************************************************************************************************************************

[1] flask_my_form.py AND /templates/my-form.html:

    - Uses the Flask micro web framework to expose the functionality of task A (Runs on localhost)
    - Takes on an unsorted array in the form [6, 2, [4, 3], [[[5], None], 1]] and outputs [1,2,3,4,5,6]
    - Run python script then add http://127.0.0.1:5000 in the web browser

[2] checks.sh:
    - A bash script to automate unit testing and static code analysis as per task A [1][2]
    - The server will only start up once all checks are successful
    - To execute run "bash checks.sh"

***********************************************************************************************************************************************
TASK C: Dockerise your app
***********************************************************************************************************************************************

[1] Please refer to the dockertest folder which containers all the files require to build the docker image (Dockerfile, requirements.txt, app.py)

***********************************************************************************************************************************************
QUESTIONS:
***********************************************************************************************************************************************

[1] Describe how your application performance is limited/bound by your available compute resources (I/O, CPU, Memory)
    - By default, containers hav no resource constraints and can use as much of a given resource as the host’s kernel scheduler allows (unless limits are set)
    - Now, since we are running the application as a web server which will receive client requests and process request and return a response which will use the above computer resources, It is highly possible that the available computer resources will not be able to handle an increase in client requests. This is also true since our computer resources are finite instead of using something like Autoscaling where were are able to scale as soon as the CPU goes above a certain threshold.
    - Additionally, the application itself uses bubblesort which is an inefficient sorting algorithm O(n^2) which may require more processing power or would take longer to respond to requests
    - 

[2] Describe how you would host the service and what considerations would be important to you.
    - Since our application is running as a docker container, I would run the service in an ECS cluster which is a high-performance container orchestration service that supports Docker containers and allows you to easily run and scale containerized applications on AWS. This gives us the flexibility to scale our containers and the underlying infrastructure I.e. EC2 instances under higher loads to ensure high availability. We can also use Fargate with ECS which allows you to deploy containers without provisioning servers (AWS will manage and scale servers for you.
    - Also more cost effective than using EKS for example since with ECS you only pay for the resources you use.

[3] What would you like to have done differently in your solutions above
    - Given that I had more time I would have liked to create a UI/UX that is customer appealing
    - Additionally, the code is not at its most optimal state in terms of Time and Complexity (O(n^2)) - This can always be improved