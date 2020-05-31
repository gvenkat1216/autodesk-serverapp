# autodesk-serverapp
Part 1: Using Flask framework,this repo will deploy web server at localhost:5000

Part 2: All Http requests hitting this endpoint will be logged and will responses will be followed based on file <3.1 Take-home Challenge Brief.pdf> in the repo

Part 3: A script in Tests Folder leveraging python's requests library sends multiple requests to App Server and validates responses

#Requiremnets.txt has all the required packages for running this web application.

#Install requirements using the below command from the root directory of the project.
pip install -r requirements.txt

Note: Installing pip is a prerequisite to the above command, Please install if your system does not detect pip

#After successful installation of packages (resolve other dependencies if required), run application from root direc:
python apiHelloWorld.py

#Execute Unit tests from root directory
python -m pytest Tests/test_apiHelloWorld.py
