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

## VA

Recomendamos el uso de[Cursor.io](https://www.cursor.com/)como el Entorno de Desarrollo Integrado (IDE) para este proyecto.

## Servidor

Cómo poner en marcha su código en su propio sistema.

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

# Estibador

**NOTA**: Para un uso eficiente de los recursos, utilizamos**Suave**en lugar de**Estibador**!

Agregue estas líneas a su ~/.zshrc o ~/.bashrc:

    alias docker=podman
    alias docker-compose='podman compose'

Luego recarga la configuración de tu shell:

    $ source ~/.zshrc  # if using zsh
    # or
    $source ~/.bashrc # if using bash

Instale podman-compose mediante pip:

    $ pip install podman-compose

Verifique la instalación:

    $ podman compose --version

# Compruebe si existe alguna máquina Podman

    $ podman machine list

# Si no existe ninguna máquina, cree una.

    $ podman machine init

# Iniciar la máquina Podman

    $ podman machine start

# Establecer la ruta del socket

    $ export DOCKER_HOST=unix://$HOME/.local/share/containers/podman/machine/podman.sock

# Verifique que Podman esté funcionando

    $ podman ps

Inicie sus contenedores Docker con:

    $ cd containers/app

    # For Linux
    $ xhost +local:docker
    $ docker compose --file docker-compose.dev.yml --project-name message-board-dev up --build -d

    # For macOS with XQuartz
    # On macOS we need to start XQuartz first. Here's the complete sequence:
    # 1.Install XQuartz if you haven't already:
    $ brew install --cask xquartz
    # 2. Start XQuartz:
    $ open -a XQuartz
    # 3. You should see an "X" icon in your menu bar at the top of the screen. Click on it to open XQuartz preferences.
    # 4. In XQuartz preferences, go to the "Security" tab and make sure "Allow connections from network clients" is checked.
    # 5. Wait a few seconds for XQuartz to fully start up
    # 6. Set display to local fisrt:
    $ export DISPLAY=:0
    # 7. Get your IP address
    $ export IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
    # 8. Allow X11 forwarding from your IP
    $ xhost + $IP
    # 9. Install podman and podman compose
    $ pip install podman podman-compose
    # 10. Initialize and start a new Podman machine with the correct mount (our cloned GitHub repository 'message-board' should reside in the '/usr/local/opt/code' directory)
    $ podman machine init --now --volume /usr/local/opt/code:/home/user/code
    $ podman machine set --rootful
    $ podman machine start
    $ podman volume create cloudbeaver-config
    $ podman run --rm \
      -v cloudbeaver-config:/config \
      -v $(pwd)/initial-data.conf:/initial-data.conf:ro \
      alpine cp /initial-data.conf /config/
    # 11. Then in your terminal:
    # Remove the existing pod
    $ podman pod rm -f pod_message-board-dev
    # Remove any existing volumes
    $ podman volume rm -f message-board-dev_dbvis-config
    $ podman volume rm -f message-board-dev_message-board-data
    # Verify everything is clean
    $ podman pod ls
    $ podman ps -a
    $ podman volume ls
    # Then start fresh
    $ podman-compose --file docker-compose.dev.yml --project-name message-board-dev up -d --build
    # or alternatively (since we have a mapping in ~/.zshrc file to map docker to podman):
    $ docker compose --file docker-compose.dev.yml --project-name message-board-dev up -d --build
    # The key is that XQuartz must be running before you execute the xhost command.

    # For Windows with VcXsrv
    $ set DISPLAY=host.docker.internal:0
    $ docker compose --file docker-compose.dev.yml --project-name message-board-dev up --build -d

Esto hará girar tres contenedores:

-   tablero de mensajes-servidor-dev (puerto 8080:5000)
-   tablero de mensajes-frontend-dev (puerto 80:3000)
-   tablero de mensajes-base-de-datos-dev (puerto 5432:5432)
-   tablero de mensajes-db-gui-dev (puerto 5444:5444)

Los cuatro contenedores se están ejecutando correctamente. Verifiquemos cada servicio:

1) Interfaz (Vue.js):

-   Visita http&#x3A;//localhost:80 en tu navegador

2) Backend (Frasco):

-   Visite http&#x3A;//localhost:8080/api/health en su navegador
-   Debería devolver una respuesta de control de salud

3) Base de datos (PostgreSQL):

-   Ya funcionando y saludable (como se muestra en el estado)
-   Accesible en localhost: 5432

4) CloudBeaver (GUI de base de datos):

-   Visita http&#x3A;//localhost:8978
-   Configuración por primera vez:
-   Cree credenciales de administrador cuando se le solicite
-   Nombre de usuario: cbadmin
-   Contraseña: S3cr3tPwd
-   Haga clic en "Nueva conexión"
-   Elija "PostgreSQL"
-   Ingrese los detalles de la conexión:
-   Anfitrión: base de datos
-   Puerto: 5432
-   Base de datos: message_board_db
-   Nombre de usuario: db-user-dev
-   Contraseña: db-contraseña-dev

DbVisualizer debería conectarse a su base de datos PostgreSQL usando estas credenciales:

Servidor: base de datos
Puerto: 5432
Base de datos: message_board_db
Nombre de usuario: db-user-dev
Contraseña: db-contraseña-dev

Si DbVisualizer no se inicia automáticamente, puede consultar los registros del contenedor:

    $ docker logs message-board-db-gui-dev

# Documentación API

Navegar a`http://127.0.0.1:5000/docs`en su navegador web, o descargue openapi.json desde`http://127.0.0.1:5000/openapi.json`.

# Métrica

Dejemos que una herramienta como Prometeo raspe`http://127.0.0.1:9464/metrics`.

**_NUEVO_**

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

## Problemas de memoria (en Mac):

Aquí hay varios pasos que puede seguir para solucionar el problema de la memoria:

1.  **Verificar memoria disponible**:
    -   Abra el Monitor de actividad desde el menú Apple.
    -   Seleccione la pestaña "Memoria".
    -   Mire la columna "Uso" para ver cuánta memoria se está utilizando actualmente.

2.  **Cerrar aplicaciones innecesarias**:
    -   Asegúrese de no estar ejecutando ninguna aplicación innecesaria que pueda estar consumiendo memoria.

3.  **Borrar caché**:
    -   A veces, borrar el caché puede ayudar a liberar memoria.

4.  **Reinicie su computadora**:
    -   A veces, un simple reinicio puede resolver problemas de memoria.

5.  **Buscar actualizaciones**:
    -   Asegúrese de que su sistema operativo y sus aplicaciones estén actualizados.

6.  **Compruebe si hay pérdidas de memoria**:
    -   Utilice herramientas como Valgrind o Instruments para comprobar si hay pérdidas de memoria en su aplicación.

7.  Borrar recursos de Docker:
    -   Ejecute el siguiente comando para eliminar todos los recursos de Docker no utilizados:
        docker system prune -a

8.  Límites de memoria del escritorio Docker
    Puede limitar el uso de recursos de Docker Desktop:
    Abrir el escritorio Docker
    Ir a Configuración/Preferencias
    Seleccione "Recursos"
    Reduzca el límite de memoria (por ejemplo, a 4-6 GB dependiendo de su sistema)

9.  Optimización XQuartz
    Salga y reinicie XQuartz
    Considere usar XQuartz solo cuando sea necesario en lugar de mantenerlo funcionando

10. Soluciones a nivel de sistema:
    Borrar caché del sistema:

        sudo purge

    Verifique el uso del intercambio:

        sysctl vm.swapusage

11. Soluciones a largo plazo:

    -   Actualice su hardware:

    -   Considere utilizar una máquina más potente con más RAM.

    -   Optimice su aplicación:

    -   Utilice herramientas de creación de perfiles de memoria para identificar y optimizar operaciones que consumen mucha memoria.

    -   Monitorear y gestionar recursos:

    -   Utilice herramientas como`htop`o`iostat`para monitorear los recursos del sistema y administrarlos de manera efectiva.

    -   Configure scripts de limpieza automática para contenedores e imágenes de Docker.

Si el problema persiste, es posible que desees:

    1. Monitor which application is consuming the most memory
    2. Consider alternatives to running all these applications simultaneously
    3. Use lightweight alternatives where possible (e.g., Podman instead of Docker Desktop)

## 100 - Introducción

Ver[README.md](./100/README.md)

## 200 - Requisitos

Ver[README.md](./200/README.md)

## 300 - Construyendo nuestra aplicación

Ver[README.md](./300/README.md)

## 400 - Conclusión

Ver[README.md](./400/README.md)
