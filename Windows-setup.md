# IGX-automation-workshop-foundation

## Windows specific workstation Setup

1. Git and git bash Installation  
   Download the Windows version of git tools from [here](https://git-scm.com/downloads)

   You should be able to start "git bash" and run 'git --version' from the cli.  
   > \# Example output  
    $ git --version
    git version 2.20.0.windows.1


2. Python  
   On windows, Python installs a python launcher you access as 'py' from the cli.  
   Download the latest version of Python 2.x and 3.x from [here](https://www.python.org/downloads/) and install
   * Make sure you choose the option **Add Python to path** when installing each of them.  
   * Once installed, run the launcher from **git-bash** to check both versions work  
   > py -3 -V  
    \# expected output  
    Python 3.7.3  

   > py -2 -V
    \# expected output  
    Python 2.7.16

3. Virtual Environments

   From git-bash, run the following:  
   > py -2 -m pip install virtualenv  
   > $ py -2 -m pip --version  
   > \# example output  
   > pip 18.1 from C:\Python27\lib\site-packages\pip (python 2.7)  

   Now install for Python3:  
   > py -3 -m pip install virtualenv  
   > $ py -3 -m pip --version  
   > \#example output  
   > pip 19.2.1 from C:\Users\WEmbrey\AppData\Local\Programs\Python\Python37\lib\site-packages\pip (python 3.7)

4. Jupyter Lab  
   From the git-bash cli:  
   > py -3 -m pip install jupyter  
   > py -3 -m pip install jupyterlab  


   Create a virtual environment:  
   > py -3 -m venv .workshop-venv  
   > ls -al \# You should see the .workshop-venv folder  

   Start the venv:  
   > source .workshop-venv/Scripts/activate  
   > python -m pip install ipykernel  
   > ipython kernel install  
   > python -m pip install jupyterlab  
   > python -m ipykernel install --user --name=.workshop-venv  

   You should now be able to start the Jupyter lab server locally:  
   > jupyter lab  

   The browser should open up a Jupyter lab page.
   You should have a ".workshop-venv" icon under the *notebook* section.
   Click on that link
