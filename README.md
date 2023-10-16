# Automating Image Stenography using Python

**Note**: This project is for cybersecurity educational purposes only.

**Environment**: I created this project on macOS 14.0 (Sonoma) using Pyton 3.12.0.

**Python libraries installed**: ‘PIL' (Python Imaging Library) library:

In order to install a Python Library in my Pyton project, I first have to install virtualenv at the root of my project folder using the following command:

```shell
pip3 install virtualenv
```

Pip, which is a Python package manager, comes with your Python install from the [official Python site](https://www.python.org/downloads/). And since I have `Python 3.12.0` ***installed***, I need to use the `pip3` command instead of simply the `pip` command on `macOS`.

This command creates a venv folder at the root of your project.

Next, I have to initialize my virtual environment with the following command:

```shell
source ./venv/bin/activate
```

This command triggers a virtual environment for my project so that I can then install packages and use them for my project. The virtual environment needs to be running in order for the packages to work! I just keep it running all the time while I am working on a project. The way that you can tell that your virtual environment is active is if you see (venv) to the left of your command prompt in your Terminal window pointing to your project path.

![Terminal venv screenshot](images/terminal_venv.jpg)

In order to install the ‘PIL' (Python Imaging Library) library needed for this project, I run the following command while my virtual environment:

```shell
pip3 install pillow
```

How to run this Image Stenography automation program:

First run the `hide_text.py` file in the command line from within the project root folder:

```shell
python3 hide_text.py
```

This command hides text inside a newly created image, a copy of the original image, but with a different file name, that contains the hidden text.

Next I run the `extract_text.py` file in the command line from within the project root folder:

```shell
python3 extract_text.py >> output_text.txt
```

This command executes the `extract_text` function inside the extract_text.py file and redirects the output of the print() function inside `extract_text.py` to a (new) file called output_text.txt. So if you intend to run this command, first remove the current `output_text.txt` as well as the `output_geranimo-bKhETeDV1WM-unsplash.png` image so that you can re-create your own from scratch!

By modularizing these functions, I am able to easily re-use them and even separately in other projects.




