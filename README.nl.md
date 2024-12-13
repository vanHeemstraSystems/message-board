berichtenbord

# Berichtenbord

|        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CI/CD  | [![CI - Server](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_server.yml/badge.svg)](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_server.yml)[![CD - Frontend](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_frontend.yml/badge.svg)](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_frontend.yml)                                                                                                                                                                                         |
| Pakket | [![PyPI - Version](https://img.shields.io/pypi/v/message-board.svg?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.org/project/message-board/)[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/message-board.svg?logo=python&label=Python&logoColor=gold)](https://pypi.org/project/message-board/)                                                                                                                                                                                                                                                                                 |
| Meta   | [![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)[![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![types - Mypy](https://img.shields.io/badge/types-Mypy-blue.svg)](https://github.com/ambv/black)[![License - MIT](https://img.shields.io/badge/license-MIT-9400d3.svg)](https://spdx.org/licenses/)[![GitHub Sponsors](https://img.shields.io/github/sponsors/vanHeemstraSystems?logo=GitHub%20Sponsors&style=social)](https://github.com/sponsors/vanHeemstraSystems) |

* * *

> Een prikbord waarop verzonden berichten worden weergegeven.

-   [Documentatie](./DOCUMENTATION.md)
-   [Glossarium](./GLOSSARY.md)
-   [Afbeeldingen](./IMAGES.md)
-   [Referenties](./REFERENCES.md)
-   [Telemetrie](./TELEMETRY.md)

**Samenvatting**

## Server

Uw code op uw eigen systeem operationeel krijgen.

**Opmerking**: Zorg ervoor dat u voldoet aan de[vereisten](./200/README.md).

1.  **Installatieproces:**

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

    **OPMERKING**: De moderne manier is om te gebruiken`pyproject.toml`om afhankelijkheden te installeren, niet \`\`\`requirements.txt. Daarom mag er geen require.txt-bestand zijn.

    === START: UPDATE DEZE SECTIE VOOR message board ===

    **Verpak uw site met webpack:**Zodra u een website heeft die goed genoeg is om te gebruiken, moet u de applicatie verpakken met webpack. Deze pakketmap wordt vermeld in`.gitignore`om te voorkomen dat het aan git wordt vastgelegd.

    Alle instellingen zouden nu klaar moeten zijn, dus alles wat je hoeft te doen:
    1)`$ hatch shell`2)`(threagile-monitoring) $ cd src/threagile_monitoring`3)`(threagile-monitoring) $ npm install`4)`(threagile-monitoring) $ npm run build`

    Hierdoor ontstaat de`app.js`bestand - dat alle componenten bevat - in`/src/threagile_monitoring/static/js/`.

    **Ontwikkeling met webpack:**Als u uw website nog aan het ontwikkelen bent, in a**afzonderlijke terminalsessie**, nadat u het bovenstaande installatieproces heeft gevolgd, doet u het volgende:
    1)`$ hatch shell`2)`(threagile-monitoring) $ cd src/threagile_monitoring`3)`(threagile-monitoring) $ npm install`4)`(threagile-monitoring) $ npm run watch`

    Dit zal - in de afzonderlijke terminalsessie (d.w.z.`background`) - laad voortdurend de wijzigingen die u aanbrengt in de juiste bestanden, terwijl u door kunt gaan met het aanbrengen van die wijzigingen - in de initiële terminalsessie (d.w.z.`foreground`). Je hoeft dus niet na elke bewerking je bronnen opnieuw op te bouwen, dit gebeurt automatisch!

    Om de wijzigingen te zien, hoeft u alleen maar uw navigator op te slaan en opnieuw te laden (meestal met F5).

    Zorg ervoor dat u uw webpagina als volgt uitvoert tijdens het testen met backend-functies:
    1)`(threagile-monitoring) $ cd src/threagile_monitoring`2)`(threagile-monitoring) $ python app.py`

    **Test**

    Test de applicatie (frontend) op deze manier:

    1)`$ hatch shell`2)`(threagile-monitoring) $ cd src/threagile_monitoring`3)`(threagile-monitoring) $ npm install`4)`(threagile-monitoring) $ npm test`5)`(threagile-monitoring) $ npm test -- --coverage`

    **Loop:**

    Als u niet aan het ontwikkelen bent, voert u de applicatie (backend en frontend tegelijkertijd) op deze manier uit:

        $ hatch run python src/threagile_monitoring/app.py # starts the app 

2.  Software-afhankelijkheden

3.  Nieuwste releases

4.  API-referenties

5.  Bouwen en testen:

    Om uw code samen te stellen, gebruikt u:

    ```bash
    $ cd threagile-monitoring
    $ hatch build
    ```

    Om AI te gebruiken voor beoordelingen van pull-aanvragen, gebruikt u:

    <https://app.coderabbit.ai/dashboard>(gebruikt`phpstan.neon`)

    Om de applicatie uit te voeren, gebruikt u:

    Linux:

    ```bash
    $ export SECRET_KEY="secret"
    ```

    Ramen:

    ```bash
    $ setx SECRET_KEY secret
    ```

    Dan:

    ```bash
    $ cd threagile-monitoring
    # Without hatch: $ python src/threagile_monitoring/app.py
    $ hatch run python src/threagile_monitoring/app.py
    ```

    Navigeer vervolgens naar`http://127.0.0.1:5000/`in uw webbrowser.

    Om tests uit te voeren, gebruikt u:

    ```bash
    $ cd threagile-monitoring
    $ pip install pytest # optional
    $ pytest tests/
    ```

# Dokwerker

Start uw Docker-containers met:

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
    # 6. Then in your terminal:
    $ xhost +localhost
    $ export DISPLAY=host.docker.internal:0
    $ docker compose --file docker-compose.dev.yml --project-name message-board-dev up --build -d
    # The key is that XQuartz must be running before you execute the xhost command.

    # For Windows with VcXsrv
    $ set DISPLAY=host.docker.internal:0
    $ docker compose --file docker-compose.dev.yml --project-name message-board-dev up --build -d

Hierdoor worden drie containers geactiveerd:

-   message-board-server-dev (poort 8080:5000)
-   message-board-frontend-dev (poort 80:3000)
-   message-board-database-dev (poort 5432:5432)
-   message-board-db-gui-dev (poort 5444:5444)

DbVisualizer zou verbinding moeten maken met uw PostgreSQL-database met behulp van deze inloggegevens:

Server: database
Haven: 5432
Database: message_board_db
Gebruikersnaam: db-user-dev
Wachtwoord: db-wachtwoord-dev

Als DbVisualizer niet automatisch start, kunt u de containerlogboeken controleren:

    $ docker logs message-board-db-gui-dev

# API-documentatie

Navigeer naar`http://127.0.0.1:5000/docs`in uw webbrowser, of download de openapi.json van`http://127.0.0.1:5000/openapi.json`.

# Statistieken

Laat een stuk gereedschap als Prometheus schrapen`http://127.0.0.1:9464/metrics`.

**_NIEUW_**

**Inhoudsopgave**

-   [Installatie](#installation)
-   [Versiebron](#version-source)
-   [Omgevingen](#environments)
-   [Bouwen](#build)
-   [Licentie](#license)

## Installatie

```console
pip install threagile-monitoring
```

## Versiebron

-   De[hatch-vcs](https://github.com/ofek/hatch-vcs)versie bronplug-in bepaalt de projectversie met behulp van Git-tags

## Omgevingen

-   Netjes gedefinieerd in een standalone[`hatch.toml`](https://hatch.pypa.io/latest/intro/#configuration)
-   De`test`matrix maakt gebruik van de[luikcontainers](https://github.com/ofek/hatch-containers)plug-in om elke omgeving binnen Docker-containers uit te voeren; gebruik is te zien in de[test](.github/workflows/test.yml)GitHub-workflow

## Bouwen

-   Alle bouwdoelen gebruiken de[hatch-vcs](https://github.com/ofek/hatch-vcs)bouw een hook-plug-in om een`_version.py` file so the version can be used at runtime
-   Wielen gebruiken de[hatch-mypyc](https://github.com/ofek/hatch-mypyc)bouw hook-plug-in om eerst alle code mee te compileren[Mijnpyc](https://github.com/mypyc/mypyc)
-   De[bouwen](.github/workflows/build.yml)De GitHub-workflow laat zien hoe u:
    -   gebruik[cibuildwiel](https://github.com/pypa/cibuildwheel)om binaire wielen voor elk platform te distribueren
    -   gebruik de[app](https://hatch.pypa.io/latest/plugins/builder/app/)build target om zelfstandige distributies voor elk platform te bouwen

## Licentie

`threagile-monitoring`wordt verspreid onder de voorwaarden van de[MET](https://spdx.org/licenses/MIT.html)licentie.

    === END:  UPDATE THIS SECTION FOR message board ===

## Frontend

1) Maak de SvelteKit-applicatie:

    $ cd containers/app
    $ npx sv create frontend
    Choose "SvelteKit demo"
    Choose Yes, using Typescript syntax
    Choose prettier, eslint, vitest, tailwindcss
    Choose typography, forms, container-queries
    Choose pnpm

Volgende stappen:

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

## Geheugenproblemen (op Mac):

Hier zijn verschillende stappen die u kunt nemen om het geheugenprobleem op te lossen:

1.  **Controleer beschikbaar geheugen**:
    -   Open de Activity Monitor vanuit het Apple-menu.
    -   Selecteer het tabblad "Geheugen".
    -   Kijk naar de kolom 'Gebruik' om te zien hoeveel geheugen momenteel wordt gebruikt.

2.  **Sluit onnodige applicaties**:
    -   Zorg ervoor dat u geen onnodige toepassingen uitvoert die mogelijk geheugen in beslag nemen.

3.  **Cache wissen**:
    -   Soms kan het wissen van de cache geheugen helpen vrijmaken.

4.  **Start uw computer opnieuw op**:
    -   Soms kan een eenvoudige herstart geheugenproblemen oplossen.

5.  **Controleer op updates**:
    -   Zorg ervoor dat uw besturingssysteem en applicaties up-to-date zijn.

6.  **Controleer op geheugenlekken**:
    -   Gebruik tools zoals Valgrind of Instruments om te controleren op geheugenlekken in uw applicatie.

7.  Wis Docker-bronnen:
    -   Voer de volgende opdracht uit om alle ongebruikte Docker-bronnen te verwijderen:
        docker system prune -a

8.  Docker Desktop-geheugenlimieten
    U kunt het bronnengebruik van Docker Desktop beperken:
    Open Docker-bureaublad
    Ga naar Instellingen/Voorkeuren
    Selecteer "Bronnen"
    Verlaag de geheugenlimiet (bijvoorbeeld naar 4-6 GB, afhankelijk van uw systeem)

9.  XQuartz-optimalisatie
    Sluit XQuartz af en start het opnieuw
    Overweeg om XQuartz alleen te gebruiken als dat nodig is, in plaats van het draaiende te houden

10. Oplossingen op systeemniveau:
    Systeemcache wissen:

        sudo purge

    Controleer het swapgebruik:

        sysctl vm.swapusage

11. Oplossingen voor de lange termijn:

    -   Upgrade uw hardware:

    -   Overweeg een krachtigere machine met meer RAM te gebruiken.

    -   Optimaliseer uw applicatie:

    -   Gebruik geheugenprofileringstools om geheugenintensieve bewerkingen te identificeren en te optimaliseren.

    -   Middelen bewaken en beheren:

    -   Gebruik hulpmiddelen zoals`htop`of`iostat`om systeembronnen te bewaken en deze effectief te beheren.

    -   Stel automatische opschoonscripts in voor Docker-containers en afbeeldingen.

Als het probleem zich blijft voordoen, kunt u het volgende doen:

    1. Monitor which application is consuming the most memory
    2. Consider alternatives to running all these applications simultaneously
    3. Use lightweight alternatives where possible (e.g., Podman instead of Docker Desktop)

## 100 - Inleiding

Zien[README.md](./100/README.md)

## 200 - Vereisten

Zien[README.md](./200/README.md)

## 300 - Onze applicatie bouwen

Zien[README.md](./300/README.md)

## 400 - Conclusie

Zien[README.md](./400/README.md)
