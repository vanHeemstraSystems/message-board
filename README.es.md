tablero de mensajes

# Tablero de mensajes

|         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CI/CD   | [![CI - Server](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_server.yml/badge.svg)](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_server.yml)[![CD - Frontend](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_frontend.yml/badge.svg)](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_frontend.yml)                                                                                                                                                                                         |
| Paquete | [![PyPI - Version](https://img.shields.io/pypi/v/message-board.svg?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.org/project/message-board/)[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/message-board.svg?logo=python&label=Python&logoColor=gold)](https://pypi.org/project/message-board/)                                                                                                                                                                                                                                                                                 |
| Meta    | [![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)[![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![types - Mypy](https://img.shields.io/badge/types-Mypy-blue.svg)](https://github.com/ambv/black)[![License - MIT](https://img.shields.io/badge/license-MIT-9400d3.svg)](https://spdx.org/licenses/)[![GitHub Sponsors](https://img.shields.io/github/sponsors/vanHeemstraSystems?logo=GitHub%20Sponsors&style=social)](https://github.com/sponsors/vanHeemstraSystems) |

* * *

> Un tablero de mensajes que mostrará los mensajes enviados.

-   [Documentación](./DOCUMENTATION.md)
-   [Glosario](./GLOSSARY.md)
-   [Imágenes](./IMAGES.md)
-   [Referencias](./REFERENCES.md)
-   [Telemetria](./TELEMETRY.md)

**Resumen ejecutivo**

## Servidor

Poner en funcionamiento su código en su propio sistema.

**Nota**: Asegúrese de cumplir con los[requisitos](./200/README.md).

1.  **Proceso de instalación:**

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

    **NOTA**: La forma moderna es utilizar`pyproject.toml`para instalar dependencias, no \`\`\`requirements.txt. Por lo tanto, no debería haber un archivo de requisitos.txt.

    === INICIO: ACTUALIZAR ESTA SECCIÓN PARA el tablero de mensajes ===

    **Empaqueta tu sitio con webpack:**Una vez que tenga un sitio web que sea lo suficientemente bueno para su uso, deberá empaquetar la aplicación con webpack. Esta carpeta de paquete aparece en`.gitignore`para evitar que se comprometa con git.

    Toda la configuración ya debería estar lista, así que todo lo que tienes que hacer:
    1)`$ hatch shell`2)`(threagile-monitoring) $ cd src/threagile_monitoring`3)`(threagile-monitoring) $ npm install`4)`(threagile-monitoring) $ npm run build`

    Esto creará el`app.js`archivo, que contiene todos los componentes, en`/src/threagile_monitoring/static/js/`.

    **Desarrollo con paquete web:**Si todavía estás desarrollando tu sitio web, en un**sesión terminal separada**, después de haber seguido el proceso de instalación anterior, haga esto:
    1)`$ hatch shell`2)`(threagile-monitoring) $ cd src/threagile_monitoring`3)`(threagile-monitoring) $ npm install`4)`(threagile-monitoring) $ npm run watch`

    Esto, en la sesión de terminal separada (es decir,`background`) - cargue constantemente los cambios que realice en los archivos apropiados, mientras puede continuar realizando esos cambios - en la sesión inicial del terminal (es decir,`foreground`). Así que no tienes que crear tus fuentes después de cada edición, ¡se encargan automáticamente!

    Para ver los cambios simplemente guarda y recarga tu navegador (normalmente con F5).

    Asegúrese de ejecutar su página web cuando pruebe con funciones de backend, de la siguiente manera:
    1)`(threagile-monitoring) $ cd src/threagile_monitoring`2)`(threagile-monitoring) $ python app.py`

    **Prueba**

    Pruebe la aplicación (frontend) de esta manera:

    1)`$ hatch shell`2)`(threagile-monitoring) $ cd src/threagile_monitoring`3)`(threagile-monitoring) $ npm install`4)`(threagile-monitoring) $ npm test`5)`(threagile-monitoring) $ npm test -- --coverage`

    **Correr:**

    Si no está en desarrollo, ejecute la aplicación (backend y frontend simultáneamente) de esta manera:

        $ hatch run python src/threagile_monitoring/app.py # starts the app 

2.  Dependencias de software

3.  Últimos lanzamientos

4.  Referencias API

5.  Construir y probar:

    Para construir su código, use:

    ```bash
    $ cd threagile-monitoring
    $ hatch build
    ```

    Para usar IA para revisiones de solicitudes de extracción, use:

    <https://app.coderabbit.ai/dashboard>(usa`phpstan.neon`)

    Para ejecutar la aplicación, utilice:

    Linux:

    ```bash
    $ export SECRET_KEY="secret"
    ```

    Ventanas:

    ```bash
    $ setx SECRET_KEY secret
    ```

    Entonces:

    ```bash
    $ cd threagile-monitoring
    # Without hatch: $ python src/threagile_monitoring/app.py
    $ hatch run python src/threagile_monitoring/app.py
    ```

    Luego, navegue hasta`http://127.0.0.1:5000/`en su navegador web.

    Para ejecutar pruebas, utilice:

    ```bash
    $ cd threagile-monitoring
    $ pip install pytest # optional
    $ pytest tests/
    ```

# Documentación API

Navegar a`http://127.0.0.1:5000/docs`en su navegador web, o descargue openapi.json desde`http://127.0.0.1:5000/openapi.json`.

# Métrica

Dejemos que una herramienta como Prometeo raspe`http://127.0.0.1:9464/metrics`.

**_ NEW _**

**Tabla de contenido**

-   [Instalación](#installation)
-   [Fuente de la versión](#version-source)
-   [Ambientes](#environments)
-   [Construir](#build)
-   [Licencia](#license)

## Instalación

```console
pip install threagile-monitoring
```

## Fuente de la versión

-   El[escotilla-vcs](https://github.com/ofek/hatch-vcs)El complemento fuente de la versión determina la versión del proyecto usando etiquetas Git.

## Ambientes

-   Definido claramente de forma independiente[`hatch.toml`](https://hatch.pypa.io/latest/intro/#configuration)
-   El`test`la matriz utiliza el[contenedores-escotilla](https://github.com/ofek/hatch-containers)complemento para ejecutar cada entorno dentro de contenedores Docker; El uso se puede ver en el[prueba](.github/workflows/test.yml)flujo de trabajo de GitHub

## Construir

-   Todos los objetivos de construcción utilizan el[escotilla-vcs](https://github.com/ofek/hatch-vcs)construir complemento de gancho para enviar un`_version.py`archivo para que la versión pueda usarse en tiempo de ejecución
-   Las ruedas utilizan el[hatch-mypyc](https://github.com/ofek/hatch-mypyc)complemento de enlace de compilación para compilar primero todo el código[mipyc](https://github.com/mypyc/mypyc)
-   El[construir](.github/workflows/build.yml)El flujo de trabajo de GitHub muestra cómo:
    -   usar[cibuildwheel](https://github.com/pypa/cibuildwheel)distribuir ruedas binarias para cada plataforma
    -   utilizar el[aplicación](https://hatch.pypa.io/latest/plugins/builder/app/)construir objetivo para crear distribuciones independientes para cada plataforma

## Licencia

`threagile-monitoring`se distribuye bajo los términos del[CON](https://spdx.org/licenses/MIT.html)licencia.

    === END:  UPDATE THIS SECTION FOR message board ===

## Interfaz

1) Cree la aplicación SvelteKit:

    $ cd containers/app
    $ npx sv create frontend
    Choose "SvelteKit demo"
    Choose Yes, using Typescript syntax
    Choose prettier, eslint, vitest, tailwindcss
    Choose typography, forms, container-queries
    Choose pnpm

Próximos pasos:

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

## 100 - Introducción

Ver[README.md](./100/README.md)

## 200 - Requisitos

Ver[README.md](./200/README.md)

## 300 - Construyendo nuestra aplicación

Ver[README.md](./300/README.md)

## 400 - Conclusión

Ver[README.md](./400/README.md)
