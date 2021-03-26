# DJANGO GENERATOR
To generate MVT Structure using api definition file

Requirements:  

1. Python 3.6 or higher (Refer to this link to download and install Python: https://www.python.org/downloads/release/python-366/)

2. Pip (Python package manager) usually gets installed along with python. If pip is not installed on your machine then follow the instructions in this link to install pip: https://www.makeuseof.com/tag/install-pip-for-python/

  

## Steps to setup the project:

1. Clone the repository.

2. Run `virtualenv .venv`

3. Run `pip install -r requirements.txt`

4. Run `python manage.py collectstatic`

5.  Run `python manage.py generatefromdef swagger.yaml`


