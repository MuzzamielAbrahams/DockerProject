
Hi There,

This is just a simple application I have created to explore some topics including:

  [1] Bubblesort O(n^2)
  [2] Micro Web Frameworks (Flask)
  [3] Bash scripts to automate starting up the server (If any testing fails the server won't be started)
  [4] Dockerising the application
  
***********************************************************************************************************************************************
TASK A - Creating and Testing (unittest,static code analyzer) Application:
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

[1] Please refer to the dockertest folder which contains all the files required to build the docker image (Dockerfile, requirements.txt, app.py)
