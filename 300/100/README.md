# 100 - Server

See also [Python Environment Management with Hatch](https://earthly.dev/blog/python-hatch/)

To create a new project, all you have to do is run the hatch new <project name> command. This command creates a project directory containing a source code directory (src), a test directory (tests), and a configuration file for project-related tools (pyproject.toml).

For this tutorial, let’s create a simple Python application named message-board that uses a Flask API. To do so, run hatch new "Message Board". The folder structure that’s created will look like this:

```
$ cd containers/app
$ hatch new "Message Board"
server
|---- src
|     |---- message_board
|           |---- __about__.py
|           |---- __init__.py
|---- tests
|     |---- __init__.py
|---- LICENSE.txt
|---- README.md
|---- pyproject.toml
```

**NOTE**: We manually renamed "message-board" to "server" in above diagram after the project was created.

Go ahead and create a simple Flask API (app.py) in the src/message_board directory and a test script (test_app.py) in the tests directory.

Add the following code to the app.py file:

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
```
src/message_board/app.py

This code imports the Flask dependency and creates an endpoint named hello that prints a simple message.

To test the app, add the following lines of code to the test_app.py file:

```
import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()
```
tests/test_app.py

This code performs [unit testing](https://docs.python.org/3/library/unittest.html) by converting a simple string to uppercase.

Now that the setup is complete, it’s time to explore the environments in Hatch.

Try:

```
$ cd server
$ hatch env create
```

It will tell you that a 'default' environment already exists. That is fine.

Look in ```pyproject.toml```:

```
[tool.hatch.envs.default]
dependencies = [
  "coverage[toml]>=6.5",
  "flask"
]
[tool.hatch.envs.default.scripts]
app = "python src/message_board/app.py"
```
server/pyproject.toml

Yours may differ.

To run a Python script using Hatch, you can use the hatch run command, which supports several arguments, including one for specifying the desired environment. If no environment is specified, the default environment and its dependencies are used to run the script.

Install Python:

```
$ hatch python install 3.13
```

To enter the environment use:

```
$ hatch shell
```

Inside the shell, you can find the project details with:
```
(message-board) $ pip show message-board
```

You will see:

```
Name: message-board
Version: 0.0.1
Summary: 
Home-page: 
Author: 
Author-email: Willem van Heemstra <wvanheemstra@icloud.com>
License: MIT
Location: /home/gitpod/.local/share/hatch/env/virtual/message-board/R24GuwJR/message-board/lib/python3.12/site-packages
Editable project location: /workspace/message-board/containers/app/server
Requires: 
Required-by: 
```

Optionally, see where your envirponment's python is located:

```
(message-board) $ python -c "import sys;print(sys.executable)"
```

You will something like:

```
/home/gitpod/.local/share/hatch/env/virtual/message-board/R24GuwJR/message-board/bin/python
```

Now upgrade pip (optional):

```
(message-board) $ pip install --upgrade pip
```

Install the requirements of the project (kept in requirements.txt):

```
(message-board) $ pip install -r requirements.txt
```

This will install all required python packages.

You can now run the application with:

```
(message-board) $ python src/message_board/app.py
```

Your output should look like this:

```
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:3000
 * Running on http://10.0.5.2:3000
Press CTRL+C to quit
192.168.0.74 - - [09/Dec/2024 13:08:24] "GET / HTTP/1.1" 200 -
192.168.0.74 - - [09/Dec/2024 13:08:25] "GET /favicon.ico HTTP/1.1" 404 -
```

Exit the shell:

```
(message-board) $ exit
```

Test with the following command:

```
$ hatch test --all
```

You will see an output alike:

```

────────────────────────────────────────────── hatch-test.py3.13 ──────────────────────────────────────────────────────────────────────
============================================== test session starts ====================================================================
platform linux -- Python 3.13.0, pytest-8.3.4, pluggy-1.5.0
rootdir: /workspace/message-board/containers/app/server
configfile: pyproject.toml
plugins: rerunfailures-14.0, mock-3.14.0, xdist-3.6.1
collected 1 item                                                                                                                                                                                              

tests/test_app.py .                                                                                                                                                                                     [100%]

=============================================== 1 passed in 0.05s ======================================================================

```

To start your Flask app in the default environment, run the following:

```
$ hatch run app
```

Your output should look like this:

```
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:3000
 * Running on http://10.0.5.2:3000
Press CTRL+C to quit
192.168.0.74 - - [09/Dec/2024 13:08:24] "GET / HTTP/1.1" 200 -
192.168.0.74 - - [09/Dec/2024 13:08:25] "GET /favicon.ico HTTP/1.1" 404 -
```