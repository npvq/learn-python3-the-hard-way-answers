# Creating a Virtual Environment. (for Linux)

First, check if `virtualenv` is already installed.

Execute the following command in a command line:

```bash
$ pip3 list | grep 'virtualenv'
```

To install and set up a Virtual Environment, standard procedure is the following commands.

```bash
pip3 install virtualenv
sudo apt install virtualenv  # If the last one didn't work
whereis virtualenv  # Refer to Line 2 if that doesn't work
mkdir ~/.venvs
virtualenv --system-site-packages ~/.venvs/dir_name  # If you don't have a directory with a virtual python installation already
. ~/.venvs/dir_name/bin/activate  # to activate, sources the file 'activate'
```

>Note:
>virtualenv has been discontinued for Python 3, there are two ways to create a virtual environment with python 3.
>Using python3's standard module/lib: `python3 -m venv ~/.venvs/dir_name`
>
>OR Using the legacy format with specified path: `virtualenv -p /path/to/python3 dir_name`

to the virtual environment exit, type `deactivate`.

next, install the testing toolkit `nose` while inside the virtual environment using the command
```bash
pip3 install nose
```

To set up a skeleton for a python project, create the following file structure inside your project folder.

```
.
├── bin
├── doc
├── NAME
│   └── __init__.py
├── setup.py
└── tests
    ├── __init__.py
    └── NAME_tests.py
```

from now on, the Virtual Environment directory that we will be using will be named `lpthw` and will be located in `Exercise 46`. The `skeleton_template` directory will also be located in `Exercise 46`.

All future Virtual Environment usage would be covered in the directory `lpthw`
