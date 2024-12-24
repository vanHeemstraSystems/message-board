Message-Board

# Message Board

|       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CI/CD | [![CI - Server](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_server.yml/badge.svg)](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_server.yml)[![CD - Frontend](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_frontend.yml/badge.svg)](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_frontend.yml)                                                                                                                                                                                         |
| Paket | [![PyPI - Version](https://img.shields.io/pypi/v/message-board.svg?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.org/project/message-board/)[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/message-board.svg?logo=python&label=Python&logoColor=gold)](https://pypi.org/project/message-board/)                                                                                                                                                                                                                                                                                 |
| Meta  | [![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)[![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![types - Mypy](https://img.shields.io/badge/types-Mypy-blue.svg)](https://github.com/ambv/black)[![License - MIT](https://img.shields.io/badge/license-MIT-9400d3.svg)](https://spdx.org/licenses/)[![GitHub Sponsors](https://img.shields.io/github/sponsors/vanHeemstraSystems?logo=GitHub%20Sponsors&style=social)](https://github.com/sponsors/vanHeemstraSystems) |

* * *

> Ein Message Board, das eingereichte Nachrichten anzeigt.

-   [Dokumentation](./DOCUMENTATION.md)
-   [Glossar](./GLOSSARY.md)
-   [Bilder](./IMAGES.md)
-   [Referenzen](./REFERENCES.md)
-   [Telemetrie](./TELEMETRY.md)

**Zusammenfassung**

## GEHT

Wir empfehlen die Verwendung von[Cursor.io](https://www.cursor.com/)als integrierte Entwicklungsumgebung (IDE) für dieses Projekt.

## Server

Bringen Sie Ihren Code auf Ihrem eigenen System zum Laufen.

**Notiz**: Stellen Sie sicher, dass Sie die erfüllen[Anforderungen](./200/README.md).

1.  **Installationsprozess:**

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

    **NOTIZ**: Die moderne Art ist zu verwenden`pyproject.toml`um Abhängigkeiten zu installieren, nicht „requirements.txt“. Daher sollte es keine Datei „requirements.txt“ geben.

    === START: AKTUALISIEREN SIE DIESEN ABSCHNITT FÜR DAS Message Board ===

    **Verpacken Sie Ihre Website mit Webpack:**Sobald Sie eine Website haben, die für Sie gut genug ist, müssen Sie die Anwendung mit Webpack packen. Dieser Paketordner ist in aufgeführt`.gitignore`um zu vermeiden, dass man sich an Git bindet.

    Die gesamte Einrichtung sollte inzwischen fertig sein. Sie müssen also nur noch Folgendes tun:
    1)`$ hatch shell`2)`(threagile-monitoring) $ cd src/threagile_monitoring`3)`(threagile-monitoring) $ npm install`4)`(threagile-monitoring) $ npm run build`

    Dadurch wird das erstellt`app.js`Datei - die alle Komponenten enthält - in`/src/threagile_monitoring/static/js/`.

    **Entwicklung mit Webpack:**Wenn Sie Ihre Website noch entwickeln, in a**separate Terminalsitzung**, nachdem Sie den oben genannten Installationsprozess befolgt haben, gehen Sie wie folgt vor:
    1)`$ hatch shell`2)`(threagile-monitoring) $ cd src/threagile_monitoring`3)`(threagile-monitoring) $ npm install`4)`(threagile-monitoring) $ npm run watch`

    Dies wird - in der separaten Terminalsitzung (d. h.`background`) – lädt die von Ihnen vorgenommenen Änderungen ständig in die entsprechenden Dateien, während Sie diese Änderungen weiterhin vornehmen können – in der ersten Terminalsitzung (d. h.`foreground`). Sie müssen Ihre Quellen also nicht nach jeder Bearbeitung neu erstellen, dies geschieht automatisch!

    Um die Änderungen zu sehen, speichern Sie einfach Ihren Navigator und laden Sie ihn neu (normalerweise mit F5).

    Stellen Sie sicher, dass Sie Ihre Webseite beim Testen mit Backend-Funktionen wie folgt ausführen:
    1)`(threagile-monitoring) $ cd src/threagile_monitoring`2)`(threagile-monitoring) $ python app.py`

    **Prüfen**

    Testen Sie die Anwendung (Frontend) auf diese Weise:

    1)`$ hatch shell`2)`(threagile-monitoring) $ cd src/threagile_monitoring`3)`(threagile-monitoring) $ npm install`4)`(threagile-monitoring) $ npm test`5)`(threagile-monitoring) $ npm test -- --coverage`

    **Laufen:**

    Wenn Sie nicht entwickeln, führen Sie die Anwendung (Backend und Frontend gleichzeitig) auf diese Weise aus:

        $ hatch run python src/threagile_monitoring/app.py # starts the app 

2.  Softwareabhängigkeiten

3.  Neueste Veröffentlichungen

4.  API-Referenzen

5.  Build and Test:

    Um Ihren Code zu erstellen, verwenden Sie:

    ```bash
    $ cd threagile-monitoring
    $ hatch build
    ```

    Um KI für Pull-Request-Reviews zu verwenden, verwenden Sie:

    <https://app.coderabbit.ai/dashboard>(verwendet`phpstan.neon`)

    Um die Anwendung auszuführen, verwenden Sie:

    Linux:

    ```bash
    $ export SECRET_KEY="secret"
    ```

    Windows:

    ```bash
    $ setx SECRET_KEY secret
    ```

    Dann:

    ```bash
    $ cd threagile-monitoring
    # Without hatch: $ python src/threagile_monitoring/app.py
    $ hatch run python src/threagile_monitoring/app.py
    ```

    Navigieren Sie dann zu`http://127.0.0.1:5000/`in Ihrem Webbrowser.

    Um Tests auszuführen, verwenden Sie:

    ```bash
    $ cd threagile-monitoring
    $ pip install pytest # optional
    $ pytest tests/
    ```

# Docker

**NOTIZ**: Für eine effiziente Nutzung der Ressourcen nutzen wir**Gedämpft**anstatt**Docker**!

Fügen Sie diese Zeilen zu Ihrem ~/.zshrc oder ~/.bashrc hinzu:

    alias docker=podman
    alias docker-compose='podman compose'

Laden Sie dann Ihre Shell-Konfiguration neu:

    $ source ~/.zshrc  # if using zsh
    # or
    $source ~/.bashrc # if using bash

Podman-Compose über Pip installieren:

    $ pip install podman-compose

Überprüfen Sie die Installation:

    $ podman compose --version

# Überprüfen Sie, ob Podman-Maschinen vorhanden sind

    $ podman machine list

# Wenn keine Maschine vorhanden ist, erstellen Sie eine

    $ podman machine init

# Starten Sie die Podman-Maschine

    $ podman machine start

# Legen Sie den Socket-Pfad fest

    $ export DOCKER_HOST=unix://$HOME/.local/share/containers/podman/machine/podman.sock

# Überprüfen Sie, ob Podman funktioniert

    $ podman ps

Starten Sie Ihre Docker-Container mit:

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

Dadurch werden drei Container geöffnet:

-   message-board-server-dev (Port 8080:5000)
-   message-board-frontend-dev (Port 80:3000)
-   message-board-database-dev (Port 5432:5432)
-   message-board-db-gui-dev (Port 5444:5444)

Alle vier Container laufen erfolgreich. Lassen Sie uns jeden Dienst überprüfen:

1) Frontend (Vue.js):

-   Besuchen Sie http&#x3A;//localhost:80 in Ihrem Browser

2) Backend (Flask):

-   Besuchen Sie http&#x3A;//localhost:8080/api/health in Ihrem Browser
-   Sollte eine Antwort zur Gesundheitsprüfung zurückgeben

3) Database (PostgreSQL):

-   Läuft bereits und ist fehlerfrei (wie im Status angezeigt)
-   Zugänglich auf localhost:5432

4) CloudBeaver (DB-GUI):

-   Besuchen Sie http&#x3A;//localhost:8978
-   Erstmalige Einrichtung:
-   Erstellen Sie Administratoranmeldeinformationen, wenn Sie dazu aufgefordert werden
-   Benutzername: cbadmin
-   Passwort: S3cr3tPwd
-   Klicken Sie auf „Neue Verbindung“
-   Wählen Sie „PostgreSQL“
-   Verbindungsdetails eingeben:
-   Host: Datenbank
-   Port: 5432
-   Datenbank: message_board_db
-   Benutzername: db-user-dev
-   Passwort: db-password-dev

DbVisualizer sollte mit diesen Anmeldeinformationen eine Verbindung zu Ihrer PostgreSQL-Datenbank herstellen:

Server: Datenbank
Port: 5432
Datenbank: message_board_db
Benutzername: db-user-dev
Passwort: db-password-dev

Wenn DbVisualizer nicht automatisch startet, können Sie die Containerprotokolle überprüfen:

    $ docker logs message-board-db-gui-dev

# API-Dokumentation

Navigieren Sie zu`http://127.0.0.1:5000/docs`in Ihrem Webbrowser oder laden Sie openapi.json herunter von`http://127.0.0.1:5000/openapi.json`.

# Metriken

Lassen Sie ein Werkzeug wie Prometheus kratzen`http://127.0.0.1:9464/metrics`.

**_NEU_**

**Inhaltsverzeichnis**

-   [Installation](#installation)
-   [Versionsquelle](#version-source)
-   [Umgebungen](#environments)
-   [Bauen](#build)
-   [Lizenz](#license)

## Installation

```console
pip install threagile-monitoring
```

## Versionsquelle

-   Der[hatch-vcs](https://github.com/ofek/hatch-vcs)Das Versionsquellen-Plugin bestimmt die Projektversion mithilfe von Git-Tags

## Umgebungen

-   Ordentlich in einem Standalone definiert[`hatch.toml`](https://hatch.pypa.io/latest/intro/#configuration)
-   Der`test`Matrix verwendet die[Lukencontainer](https://github.com/ofek/hatch-containers)Plugin zum Ausführen jeder Umgebung in Docker-Containern; Die Verwendung ist in der zu sehen[prüfen](.github/workflows/test.yml)GitHub-Workflow

## Bauen

-   Alle Build-Ziele verwenden die[hatch-vcs](https://github.com/ofek/hatch-vcs)Erstellen Sie ein Hook-Plugin, um ein zu versenden`_version.py`Datei, damit die Version zur Laufzeit verwendet werden kann
-   Räder verwenden die[hatch-mypyc](https://github.com/ofek/hatch-mypyc)Build-Hook-Plugin, mit dem zunächst der gesamte Code kompiliert werden soll[Mypyc](https://github.com/mypyc/mypyc)
-   Der[bauen](.github/workflows/build.yml)Der GitHub-Workflow zeigt, wie Sie:
    -   verwenden[cibuildwheel](https://github.com/pypa/cibuildwheel)binäre Räder für jede Plattform zu verteilen
    -   Benutze die[App](https://hatch.pypa.io/latest/plugins/builder/app/)build target zum Erstellen eigenständiger Distributionen für jede Plattform

## Lizenz

`threagile-monitoring`wird gemäß den Bedingungen der verteilt[MIT](https://spdx.org/licenses/MIT.html)Lizenz.

    === END:  UPDATE THIS SECTION FOR message board ===

## Frontend

1) Erstellen Sie die SvelteKit-Anwendung:

    $ cd containers/app
    $ npx sv create frontend
    Choose "SvelteKit demo"
    Choose Yes, using Typescript syntax
    Choose prettier, eslint, vitest, tailwindcss
    Choose typography, forms, container-queries
    Choose pnpm

Nächste Schritte:

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

## Speicherprobleme (auf dem Mac):

Hier sind mehrere Schritte, die Sie unternehmen können, um das Speicherproblem zu beheben:

1.  **Überprüfen Sie den verfügbaren Speicher**:
    -   Öffnen Sie den Aktivitätsmonitor über das Apple-Menü.
    -   Wählen Sie die Registerkarte „Speicher“.
    -   Sehen Sie sich die Spalte „Nutzung“ an, um zu sehen, wie viel Speicher derzeit verwendet wird.

2.  **Schließen Sie nicht benötigte Anwendungen**:
    -   Stellen Sie sicher, dass Sie keine unnötigen Anwendungen ausführen, die möglicherweise Speicher verbrauchen.

3.  **Cache leeren**:
    -   Manchmal kann das Leeren des Caches helfen, Speicher freizugeben.

4.  **Starten Sie Ihren Computer neu**:
    -   Manchmal kann ein einfacher Neustart Speicherprobleme beheben.

5.  **Suchen Sie nach Updates**:
    -   Stellen Sie sicher, dass Ihr Betriebssystem und Ihre Anwendungen auf dem neuesten Stand sind.

6.  **Suchen Sie nach Speicherlecks**:
    -   Verwenden Sie Tools wie Valgrind oder Instruments, um in Ihrer Anwendung nach Speicherlecks zu suchen.

7.  Docker-Ressourcen löschen:
    -   Führen Sie den folgenden Befehl aus, um alle nicht verwendeten Docker-Ressourcen zu entfernen:
        docker system prune -a

8.  Docker-Desktop-Speichergrenzen
    Sie können die Ressourcennutzung von Docker Desktop begrenzen:
    Öffnen Sie Docker Desktop
    Gehen Sie zu Einstellungen/Präferenzen
    Wählen Sie „Ressourcen“
    Reduzieren Sie das Speicherlimit (z. B. auf 4–6 GB, abhängig von Ihrem System).

9.  XQuartz-Optimierung
    Beenden Sie XQuartz und starten Sie es neu
    Erwägen Sie, XQuartz nur bei Bedarf zu verwenden, anstatt es laufen zu lassen

10. Lösungen auf Systemebene:
    Systemcache leeren:

        sudo purge

    Swap-Nutzung prüfen:

        sysctl vm.swapusage

11. Langfristige Lösungen:

    -   Rüsten Sie Ihre Hardware auf:

    -   Erwägen Sie die Verwendung einer leistungsstärkeren Maschine mit mehr RAM.

    -   Optimieren Sie Ihre Bewerbung:

    -   Verwenden Sie Speicherprofilierungstools, um speicherintensive Vorgänge zu identifizieren und zu optimieren.

    -   Überwachen und verwalten Sie Ressourcen:

    -   Verwenden Sie Tools wie`htop`oder`iostat`um Systemressourcen zu überwachen und effektiv zu verwalten.

    -   Richten Sie automatische Bereinigungsskripts für Docker-Container und -Images ein.

Wenn das Problem weiterhin besteht, können Sie Folgendes tun:

    1. Monitor which application is consuming the most memory
    2. Consider alternatives to running all these applications simultaneously
    3. Use lightweight alternatives where possible (e.g., Podman instead of Docker Desktop)

## 100 - Einführung

Sehen[README.md](./100/README.md)

## 200 – Anforderungen

Sehen[README.md](./200/README.md)

## 300 – Erstellen unserer Anwendung

Sehen[README.md](./300/README.md)

## 400 – Fazit

Sehen[README.md](./400/README.md)
