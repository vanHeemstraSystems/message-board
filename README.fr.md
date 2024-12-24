babillard électronique

# Tableau de messages

|          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CI/CD    | [![CI - Server](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_server.yml/badge.svg)](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_server.yml)[![CD - Frontend](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_frontend.yml/badge.svg)](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_frontend.yml)                                                                                                                                                                                         |
| Emballer | [![PyPI - Version](https://img.shields.io/pypi/v/message-board.svg?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.org/project/message-board/)[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/message-board.svg?logo=python&label=Python&logoColor=gold)](https://pypi.org/project/message-board/)                                                                                                                                                                                                                                                                                 |
| Méta     | [![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)[![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![types - Mypy](https://img.shields.io/badge/types-Mypy-blue.svg)](https://github.com/ambv/black)[![License - MIT](https://img.shields.io/badge/license-MIT-9400d3.svg)](https://spdx.org/licenses/)[![GitHub Sponsors](https://img.shields.io/github/sponsors/vanHeemstraSystems?logo=GitHub%20Sponsors&style=social)](https://github.com/sponsors/vanHeemstraSystems) |

* * *

> Un forum de messages qui affichera les messages soumis.

-   [Documentation](./DOCUMENTATION.md)
-   [Glossaire](./GLOSSARY.md)
-   [Images](./IMAGES.md)
-   [Références](./REFERENCES.md)
-   [Télémétrie](./TELEMETRY.md)

**Résumé exécutif**

## VA

Nous recommandons l'utilisation de[Cursor.io](https://www.cursor.com/)comme environnement de développement intégré (IDE) pour ce projet.

## Serveur

Faire en sorte que votre code soit opérationnel sur votre propre système.

**Note**: Assurez-vous de remplir les[exigences](./200/README.md).

1.  **Processus d'installation :**

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

    **NOTE**: La manière moderne consiste à utiliser`pyproject.toml`pour installer les dépendances, pas \`\`\`requirements.txt. Par conséquent, il ne devrait pas y avoir de fichier exigences.txt.

    === DÉBUT : METTRE À JOUR CETTE SECTION POUR le forum ===

    **Packagez votre site avec webpack :**Une fois que vous disposez d’un site Web suffisamment performant pour que vous puissiez l’utiliser, vous devez empaqueter l’application avec webpack. Ce dossier de package est répertorié dans`.gitignore`pour éviter qu'il soit engagé dans git.

    Toute la configuration devrait être prête maintenant, il vous suffit donc de :
    1)`$ hatch shell`2)`(threagile-monitoring) $ cd src/threagile_monitoring`3)`(threagile-monitoring) $ npm install`4)`(threagile-monitoring) $ npm run build`

    Cela créera le`app.js`fichier - qui contient tous les composants - dans`/src/threagile_monitoring/static/js/`.

    **Développement avec webpack :**Si vous développez encore votre site Web, dans un**session terminale séparée**, après avoir suivi le processus d'installation ci-dessus, faites ceci :
    1)`$ hatch shell`2)`(threagile-monitoring) $ cd src/threagile_monitoring`3)`(threagile-monitoring) $ npm install`4)`(threagile-monitoring) $ npm run watch`

    Cela sera - dans la session de terminal séparée (c'est-à-dire`background`) - chargez constamment les modifications que vous apportez dans les fichiers appropriés, tandis que vous pouvez continuer à apporter ces modifications - lors de la session initiale du terminal (c'est-à-dire`foreground`). Vous n’avez donc pas besoin de construire vos sources après chaque édition, cela est pris en charge automatiquement !

    Pour voir les modifications, enregistrez et rechargez simplement votre navigateur (généralement avec F5).

    Assurez-vous d'exécuter votre page Web lors des tests avec les fonctions backend, comme suit :
    1)`(threagile-monitoring) $ cd src/threagile_monitoring`2)`(threagile-monitoring) $ python app.py`

    **Test**

    Testez l'application (frontend) de cette façon :

    1)`$ hatch shell`2)`(threagile-monitoring) $ cd src/threagile_monitoring`3)`(threagile-monitoring) $ npm install`4)`(threagile-monitoring) $ npm test`5)`(threagile-monitoring) $ npm test -- --coverage`

    **Courir:**

    Si vous ne développez pas, exécutez l'application (backend et frontend simultanément) de cette façon :

        $ hatch run python src/threagile_monitoring/app.py # starts the app 

2.  Dépendances logicielles

3.  Dernières versions

4.  Références API

5.  Construire et tester :

    Pour construire votre code, utilisez :

    ```bash
    $ cd threagile-monitoring
    $ hatch build
    ```

    Pour utiliser l'IA pour les révisions de demandes d'extraction, utilisez :

    <https://app.coderabbit.ai/dashboard>(utilise`phpstan.neon`)

    Pour exécuter l'application, utilisez :

    Linux :

    ```bash
    $ export SECRET_KEY="secret"
    ```

    Fenêtres :

    ```bash
    $ setx SECRET_KEY secret
    ```

    Alors:

    ```bash
    $ cd threagile-monitoring
    # Without hatch: $ python src/threagile_monitoring/app.py
    $ hatch run python src/threagile_monitoring/app.py
    ```

    Ensuite, accédez à`http://127.0.0.1:5000/`dans votre navigateur Internet.

    Pour exécuter des tests, utilisez :

    ```bash
    $ cd threagile-monitoring
    $ pip install pytest # optional
    $ pytest tests/
    ```

# Docker

**NOTE**: Pour une utilisation efficace des ressources, nous utilisons**Tamisé**au lieu de**Docker**!

Ajoutez ces lignes à votre ~/.zshrc ou ~/.bashrc :

    alias docker=podman
    alias docker-compose='podman compose'

Rechargez ensuite votre configuration shell :

    $ source ~/.zshrc  # if using zsh
    # or
    $source ~/.bashrc # if using bash

Install podman-compose via pip:

    $ pip install podman-compose

Vérifiez l'installation :

    $ podman compose --version

# Vérifiez s'il existe des machines Podman

    $ podman machine list

# Si aucune machine n'existe, créez-en une

    $ podman machine init

# Démarrez la machine Podman

    $ podman machine start

# Définir le chemin du socket

    $ export DOCKER_HOST=unix://$HOME/.local/share/containers/podman/machine/podman.sock

# Vérifiez que Podman fonctionne

    $ podman ps

Démarrez vos conteneurs Docker avec :

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

This will spin up three containers:

-   message-board-server-dev (port 8080:5000)
-   message-board-frontend-dev (port 80:3000)
-   message-board-database-dev (port 5432:5432)
-   message-board-db-gui-dev (port 5444:5444)

Les quatre conteneurs fonctionnent correctement. Vérifions chaque service :

1) Frontend (Vue.js):

-   Visitez http&#x3A;//localhost:80 dans votre navigateur

2) Backend (flacon) :

-   Visitez http&#x3A;//localhost:8080/api/health dans votre navigateur
-   Devrait renvoyer une réponse de vérification de l'état

3) Base de données (PostgreSQL) :

-   Déjà en cours d'exécution et en bonne santé (comme indiqué dans l'état)
-   Accessible sur localhost:5432

4) CloudBeaver (interface graphique de base de données) :

-   Visitez http&#x3A;//localhost:8978
-   Première configuration :
-   Créez des informations d'identification d'administrateur lorsque vous y êtes invité
-   Nom d'utilisateur : cbadmin
-   Mot de passe : S3cr3tPwd
-   Cliquez sur "Nouvelle connexion"
-   Choisissez "PostgreSQL"
-   Saisissez les détails de la connexion :
-   Hôte : base de données
-   Port : 5432
-   Base de données : message_board_db
-   Nom d'utilisateur : db-user-dev
-   Mot de passe : db-password-dev

DbVisualizer doit se connecter à votre base de données PostgreSQL à l'aide de ces informations d'identification :

Serveur : base de données
Port : 5432
Base de données : message_board_db
Nom d'utilisateur : db-user-dev
Mot de passe : db-password-dev

Si DbVisualizer ne se lance pas automatiquement, vous pouvez vérifier les journaux du conteneur :

    $ docker logs message-board-db-gui-dev

# Documentation API

Accédez à`http://127.0.0.1:5000/docs`dans votre navigateur Web, ou téléchargez le fichier openapi.json depuis`http://127.0.0.1:5000/openapi.json`.

# Métrique

Laissez un outil comme Prometheus gratter`http://127.0.0.1:9464/metrics`.

**_NOUVEAU_**

**Table des matières**

-   [Installation](#installation)
-   [Source de la version](#version-source)
-   [Environnements](#environments)
-   [Construire](#build)
-   [Licence](#license)

## Installation

```console
pip install threagile-monitoring
```

## Source de la version

-   Le[trappe-vcs](https://github.com/ofek/hatch-vcs)Le plugin source de version détermine la version du projet à l'aide des balises Git

## Environnements

-   Bien défini dans un environnement autonome[`hatch.toml`](https://hatch.pypa.io/latest/intro/#configuration)
-   Le`test`la matrice utilise le[conteneurs à écoutille](https://github.com/ofek/hatch-containers)plugin pour exécuter chaque environnement dans les conteneurs Docker ; l'utilisation peut être vue dans le[test](.github/workflows/test.yml)Flux de travail GitHub

## Construire

-   Toutes les cibles de build utilisent le[trappe-vcs](https://github.com/ofek/hatch-vcs)construire un plugin hook pour expédier un`_version.py`fichier afin que la version puisse être utilisée au moment de l'exécution
-   Les roues utilisent le[trappe-mypyc](https://github.com/ofek/hatch-mypyc)construire un plugin hook pour compiler d'abord tout le code avec[Monpyc](https://github.com/mypyc/mypyc)
-   Le[construire](.github/workflows/build.yml)Le workflow GitHub montre comment :
    -   utiliser[roue cibuild](https://github.com/pypa/cibuildwheel)distribuer des roues binaires pour chaque plateforme
    -   utiliser le[application](https://hatch.pypa.io/latest/plugins/builder/app/)construire une cible pour créer des distributions autonomes pour chaque plate-forme

## Licence

`threagile-monitoring`est distribué selon les termes du[AVEC](https://spdx.org/licenses/MIT.html)licence.

    === END:  UPDATE THIS SECTION FOR message board ===

## L'extrémité avant

1) Créez l'application SvelteKit :

    $ cd containers/app
    $ npx sv create frontend
    Choose "SvelteKit demo"
    Choose Yes, using Typescript syntax
    Choose prettier, eslint, vitest, tailwindcss
    Choose typography, forms, container-queries
    Choose pnpm

Prochaines étapes :

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

## Problèmes de mémoire (sur Mac) :

Voici plusieurs étapes que vous pouvez suivre pour résoudre le problème de mémoire :

1.  **Vérifier la mémoire disponible**:
    -   Ouvrez le moniteur d'activité à partir du menu Pomme.
    -   Sélectionnez l'onglet "Mémoire".
    -   Regardez la colonne « Utilisation » pour voir la quantité de mémoire actuellement utilisée.

2.  **Fermez les applications inutiles**:
    -   Assurez-vous que vous n’exécutez aucune application inutile susceptible de consommer de la mémoire.

3.  **Vider le cache**:
    -   Parfois, vider le cache peut aider à libérer de la mémoire.

4.  **Redémarrez votre ordinateur**:
    -   Parfois, un simple redémarrage peut résoudre les problèmes de mémoire.

5.  **Vérifier les mises à jour**:
    -   Assurez-vous que votre système d'exploitation et vos applications sont à jour.

6.  **Rechercher des fuites de mémoire**:
    -   Utilisez des outils comme Valgrind ou Instruments pour vérifier les fuites de mémoire dans votre application.

7.  Effacer les ressources Docker :
    -   Exécutez la commande suivante pour supprimer toutes les ressources Docker inutilisées :
        docker system prune -a

8.  Limites de mémoire du bureau Docker
    Vous pouvez limiter l'utilisation des ressources de Docker Desktop :
    Ouvrir le bureau Docker
    Allez dans Paramètres/Préférences
    Sélectionnez "Ressources"
    Réduisez la limite de mémoire (par exemple, à 4-6 Go selon votre système)

9.  Optimisation XQuartz
    Quittez et redémarrez XQuartz
    Envisagez d'utiliser XQuartz uniquement en cas de besoin plutôt que de le laisser fonctionner

10. Solutions au niveau du système :
    Effacer le cache système :

        sudo purge

    Vérifiez l'utilisation du swap :

        sysctl vm.swapusage

11. Solutions à long terme :

    -   Mettez à niveau votre matériel :

    -   Pensez à utiliser une machine plus puissante avec plus de RAM.

    -   Optimisez votre candidature :

    -   Utilisez des outils de profilage de mémoire pour identifier et optimiser les opérations gourmandes en mémoire.

    -   Surveiller et gérer les ressources :

    -   Utilisez des outils comme`htop`ou`iostat`pour surveiller les ressources du système et les gérer efficacement.

    -   Configurez des scripts de nettoyage automatique pour les conteneurs et les images Docker.

Si le problème persiste, vous souhaiterez peut-être :

    1. Monitor which application is consuming the most memory
    2. Consider alternatives to running all these applications simultaneously
    3. Use lightweight alternatives where possible (e.g., Podman instead of Docker Desktop)

## 100 - Introduction

Voir[README.md](./100/README.md)

## 200 - Exigences

Voir[README.md](./200/README.md)

## 300 - Créer notre application

Voir[README.md](./300/README.md)

## 400 - Conclusion

Voir[README.md](./400/README.md)
