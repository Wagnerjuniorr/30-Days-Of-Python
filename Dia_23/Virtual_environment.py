# Setting up Virtual Enviroments
# To start awith project, it would be better to have a virtual envioronment
# Virtual environment can help us create an isolated or separate environment
# this will help us to avoid conflict in dependencies across projects
# if you wirte pip freeze on your terminal you will see all the installed packages on your computer
# if we use virtualenv, we will acess only packages which are specific for that project
# open you terminal and install virtualenv
# pip install virtualenv

# after installing the virtualenv package go to yout project folder and create a virtual env by writting
# C:\Users\User\Documents\30DaysOfPython\Dia_23>python -m venv venv

# Lets check if the venv was created by using ls (or dir for windows command prompt) command
# ls venv/

# Let us activate the virtual enviroment by writing the following command at out project folder
# Activation of the cirtual enviroment in windows may very on windows powershell and git basg
# For Windows Power Shell:
# C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\activate
# For Windows Git bash:
# C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\. activate

# After you write the activation command, you project directory will start with venv
# (venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$

# Now, lets check the avaible packages in this project by writting pip freeze
# pip install Flask

# Now, let us write pip freeze to see a list of installed packages in the project:
# pip freeze

# When you finish you should dactivate active project using deactivate.
# deactivate