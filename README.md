# autodesk-serverapp
#Requiremnets.txt has all the required packages for running this web application
#Install requirements using the below command from the root directory of the project
pip install -r requirements.txt

Note: Installing pip is a prerequisite to the above command, Please install if your system does not detect pip

#After successful installation of packages (resolve other dependencies if required), run application from root direc:
python apiHelloWorld.py

#Execute Unit tests from root directory
python -m pytest Tests/test_apiHelloWorld.py
