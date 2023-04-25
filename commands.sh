#To generate keys and clone repo
#ssh-keygen -o -t rsa -b 4096
#git clone git@github.com:dill13/udacity-cicd.git

#Create environment and launch app
python3 -m venv ~/.prj2
source ~/.prj2/bin/activate
cd ~/udacity-cicd
make all
az webapp up --name "dill13" --resource-group "Azuredevops" --runtime "PYTHON:3.7"
