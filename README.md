message-board
# Message Board

| | |
| --- | --- |
| CI/CD | [![CI - Server](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_server.yml/badge.svg)](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_server.yml) [![CD - Frontend](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_frontend.yml/badge.svg)](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_frontend.yml) |
| Package | [![PyPI - Version](https://img.shields.io/pypi/v/message-board.svg?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.org/project/message-board/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/message-board.svg?logo=python&label=Python&logoColor=gold)](https://pypi.org/project/message-board/) |
| Meta | [![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch) [![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![types - Mypy](https://img.shields.io/badge/types-Mypy-blue.svg)](https://github.com/ambv/black) [![License - MIT](https://img.shields.io/badge/license-MIT-9400d3.svg)](https://spdx.org/licenses/) [![GitHub Sponsors](https://img.shields.io/github/sponsors/vanHeemstraSystems?logo=GitHub%20Sponsors&style=social)](https://github.com/sponsors/vanHeemstraSystems) |

-----

> A Message Board that will display submitted messages.

- [Documentation](./DOCUMENTATION.md)
- [Glossary](./GLOSSARY.md)
- [Images](./IMAGES.md)
- [References](./REFERENCES.md)
- [Telemetry](./TELEMETRY.md)

**Executive Summary**

## Server

Getting your code up and running on your own system.

**Note**: Make sure you fulfill the [requirements](./200/README.md).
1.	**Installation process:** 
    ```bash 
    $ cd server
    $ hatch --version # optional, will print the version of our package to the terminal without modifying the source directory (e.g. `0.0.1`).
    # Without hatch: $ python src/message_board/app.py
    $ hatch env create # optional, if the default env already exists you will be told
    $ hatch shell # spawn a shell within an environment
    (server) $ pip show message-board-server # optional, shows the project details, here 'message-board-server', from `pyproject.toml`
    # Name: message-board-server
    # Version: 0.1.0 # it takes this from src/message_board/__about__.py
    # ...
    (server) $ python -c "import sys;print(sys.executable)" # optional, see where your environment's python is located
    (server) $ pip install --upgrade pip # optional, the `run` command allows you to execute commands in an environment as if you had already entered it.
    (server) $ exit # optional, type `exit` to leave the environment
    ```

    **NOTE**: The modern way is to use ```pyproject.toml``` to install dependencies, not ```requirements.txt. Hence there should not be a requirements.txt file.

    === START:  UPDATE THIS SECTION FOR message board ===

    **Package your site with webpack:**
    Once you have a website that is good enough for you to use, you have to package the application with webpack. This package folder is listed in ```.gitignore``` to avoid it to be committed to git.

    All of the setup should be ready by now so all you have to do:
    1) ```$ hatch shell```
    2) ```(threagile-monitoring) $ cd src/threagile_monitoring```
    3) ```(threagile-monitoring) $ npm install```
    4) ```(threagile-monitoring) $ npm run build```

    This will create the ```app.js``` file - which contains all components - in ```/src/threagile_monitoring/static/js/```.

    **Development with webpack:**
    If you are still developing your website, in a **separate terminal session**, after having followed the above installation process, do this:
    1) ```$ hatch shell```
    2) ```(threagile-monitoring) $ cd src/threagile_monitoring```
    3) ```(threagile-monitoring) $ npm install```
    4) ```(threagile-monitoring) $ npm run watch```

    This will - in the separate terminal session (i.e. ```background```) - constantly load the changes you make into the appropriate files, whilst you can can continue make those changes - in the initial terminal session (i.e. ```foreground```). So you do not have to build your sources after each edit, it is taken care of automatically!

    To see the changes just save and reload your navigator (usually with F5). 
    
    Make sure, to run your webpage when testing with backend functions, as follows:
    1) ```(threagile-monitoring) $ cd src/threagile_monitoring```
    2) ```(threagile-monitoring) $ python app.py```

    **Test**

    Test the application (frontend) this way:

    1) ```$ hatch shell```
    2) ```(threagile-monitoring) $ cd src/threagile_monitoring```
    3) ```(threagile-monitoring) $ npm install```
    4) ```(threagile-monitoring) $ npm test```
    5) ```(threagile-monitoring) $ npm test -- --coverage```

    **Run:**

    If not developing, run the application (backend and frontend simultaneously) this way: 

    ```
    $ hatch run python src/threagile_monitoring/app.py # starts the app 
    ```

2.	Software dependencies
3.	Latest releases
4.	API references
5.  Build and Test:

    To build your code, use:

    ```bash
    $ cd threagile-monitoring
    $ hatch build
    ```

    To use AI for pull request reviews, use:

    https://app.coderabbit.ai/dashboard (uses ```phpstan.neon```)

    To run the application, use:

    Linux:
    ```bash
    $ export SECRET_KEY="secret"
    ```

    Windows:
    ```bash
    $ setx SECRET_KEY secret
    ```

    Then:

    ```bash
    $ cd threagile-monitoring
    # Without hatch: $ python src/threagile_monitoring/app.py
    $ hatch run python src/threagile_monitoring/app.py
    ```

    Then, navigate to `http://127.0.0.1:5000/` in your web browser.

    To run tests, use:

    ```bash
    $ cd threagile-monitoring
    $ pip install pytest # optional
    $ pytest tests/
    ```

# API Documentation

Navigate to `http://127.0.0.1:5000/docs` in your web browser, or download the openapi.json from `http://127.0.0.1:5000/openapi.json`.

# Metrics

Let a tool like Prometheus scrape `http://127.0.0.1:9464/metrics`.

___ NEW ___

**Table of Contents**

- [Installation](#installation)
- [Version source](#version-source)
- [Environments](#environments)
- [Build](#build)
- [License](#license)

## Installation

```console
pip install threagile-monitoring
```

## Version source

- The [hatch-vcs](https://github.com/ofek/hatch-vcs) version source plugin determines the project version using Git tags

## Environments

- Defined neatly in a standalone [`hatch.toml`](https://hatch.pypa.io/latest/intro/#configuration)
- The `test` matrix uses the [hatch-containers](https://github.com/ofek/hatch-containers) plugin to run each environment inside Docker containers; usage can be seen in the [test](.github/workflows/test.yml) GitHub workflow

## Build

- All build targets use the [hatch-vcs](https://github.com/ofek/hatch-vcs) build hook plugin to ship a `_version.py` file so the version can be used at runtime
- Wheels use the [hatch-mypyc](https://github.com/ofek/hatch-mypyc) build hook plugin to first compile all code with [Mypyc](https://github.com/mypyc/mypyc)
- The [build](.github/workflows/build.yml) GitHub workflow shows how to:
  - use [cibuildwheel](https://github.com/pypa/cibuildwheel) to distribute binary wheels for every platform
  - use the [app](https://hatch.pypa.io/latest/plugins/builder/app/) build target to build standalone distributions for every platform

## License

`threagile-monitoring` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

    === END:  UPDATE THIS SECTION FOR message board ===

## Frontend

1) Create the SvelteKit application:

```
$ cd containers/app
$ npx sv create frontend
Choose "SvelteKit demo"
Choose Yes, using Typescript syntax
Choose prettier, eslint, vitest, tailwindcss
Choose typography, forms, container-queries
Choose pnpm
```

Next steps:

```
│  1: cd frontend                                                          │
|  2: pnpm install @sveltejs/adapter-node --save-dev                       |
|  3: change in svelte.config.js:                                          |
|     FROM: import adapter from '@sveltejs/adapter-auto';                  |
|     TO:   import adapter from '@sveltejs/adapter-node';                  |
|     and:                                                                 |
|     FROM: adapter: adapter()                                             |
|     TO:   adapter: adapter({ out: 'build' })                             |
|  4: Add to package.json:                                                 |
|     "packageManager": "pnpm@9.14.4",                                     |
│  5: git init && git add -A && git commit -m "Initial commit" (optional)  │
│  6: pnpm dev --open                                                      │
│                                                                          │
│  To close the dev server, hit Ctrl-C                                     │
│                                                                          │
│  Stuck? Visit us at https://svelte.dev/chat                              |
|                                                                          |
|  7: pnpm run build # creates a new build folder with production version  |
|  8: pnpm run preview # creates a preview of the production version       |
```

## 100 - Introduction

See [README.md](./100/README.md)

## 200 - Requirements

See [README.md](./200/README.md)

## 300 - Building Our Application

See [README.md](./300/README.md)

## 400 - Conclusion

See [README.md](./400/README.md)
