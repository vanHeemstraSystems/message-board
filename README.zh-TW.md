留言板

# 留言板

|           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 持續整合/持續交付 | [![CI - Server](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_server.yml/badge.svg)](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_server.yml)[![CD - Frontend](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_frontend.yml/badge.svg)](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_frontend.yml)                                                                                                                                                                                         |
| 包裹        | [![PyPI - Version](https://img.shields.io/pypi/v/message-board.svg?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.org/project/message-board/)[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/message-board.svg?logo=python&label=Python&logoColor=gold)](https://pypi.org/project/message-board/)                                                                                                                                                                                                                                                                                 |
| 元         | [![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)[![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![types - Mypy](https://img.shields.io/badge/types-Mypy-blue.svg)](https://github.com/ambv/black)[![License - MIT](https://img.shields.io/badge/license-MIT-9400d3.svg)](https://spdx.org/licenses/)[![GitHub Sponsors](https://img.shields.io/github/sponsors/vanHeemstraSystems?logo=GitHub%20Sponsors&style=social)](https://github.com/sponsors/vanHeemstraSystems) |

* * *

> 留言板將顯示提交的訊息。

-   [文件](./DOCUMENTATION.md)
-   [詞彙表](./GLOSSARY.md)
-   [圖片](./IMAGES.md)
-   [參考](./REFERENCES.md)
-   [遙測](./TELEMETRY.md)

**執行摘要**

## 伺服器

在您自己的系統上啟動並運行您的程式碼。

**筆記**: 確保您滿足[要求](./200/README.md).

1.  **安裝過程：**

    ```bash
    $ cd server
    $ hatch --version # optional, will print the version of our package to the terminal without modifying the source directory (e.g. `0.0.1`).
    # Without hatch: $ python src/message_board/app.py
    $ hatch env create # optional, if the default env already exists you will be told
    $ hatch shell # spawn a shell within an environment
    (server) $ pip show message-board-server # optional, shows the project details, here 'message-board-server', from `pyproject.toml`
    # Name: message-board-server
    # Version: 0.0.1 # it takes this from src/message_board/__about__.py
    # ...
    (server) $ python -c "import sys;print(sys.executable)" # optional, see where your environment's python is located
    (server) $ pip install --upgrade pip # optional, the `run` command allows you to execute commands in an environment as if you had already entered it.
    (server) $ pip install -r requirements.txt # pipx won't do this
    (server) $ python -m setuptools_scm # optional, display the version of our package and perform any side-effects like writing to a file. (here: `_version.py`)
    (server) $ exit # optional, type `exit` to leave the environment
    ```

    === 開始：更新留言板的這一部分 ===

    **使用 webpack 打包您的網站：**一旦你有了一個足夠好的網站可供你使用，你就必須使用 webpack 打包應用程式。該包資料夾列於`.gitignore`以避免它被提交給 git。

    現在所有設定都應該準備就緒，因此您需要做的就是：
    1）`$ hatch shell`2)`(threagile-monitoring) $ cd src/threagile_monitoring`3)`(threagile-monitoring) $ npm install`4)`(threagile-monitoring) $ npm run build`

    這將創建`app.js`文件 - 包含所有組件 - 在`/src/threagile_monitoring/static/js/`.

    **使用webpack開發：**如果您仍在開發您的網站，**單獨的終端會話**，按照上述安裝程序後，執行以下操作：
    1）`$ hatch shell`2)`(threagile-monitoring) $ cd src/threagile_monitoring`3)`(threagile-monitoring) $ npm install`4)`(threagile-monitoring) $ npm run watch`

    這將 - 在單獨的終端會話中（即`background`) - 不斷地將您所做的更改載入到適當的文件中，同時您可以在初始終端會話中繼續進行這些更改（即`foreground`）。因此，您不必在每次編輯後建立原始程式碼，它會自動處理！

    要查看更改，只需儲存並重新載入導航器（通常使用 F5）。

    確保在使用後端功能進行測試時運行您的網頁，如下所示：
    1）`(threagile-monitoring) $ cd src/threagile_monitoring`2)`(threagile-monitoring) $ python app.py`

    **測試**

    Test the application (frontend) this way:

    1)`$ hatch shell`2)`(threagile-monitoring) $ cd src/threagile_monitoring`
    3) `(threagile-monitoring) $ npm install`4)`(threagile-monitoring) $ npm test`5)`(threagile-monitoring) $ npm test -- --coverage`

    **跑步：**

    如果不進行開發，請按以下方式運行應用程式（同時後端和前端）：

        $ hatch run python src/threagile_monitoring/app.py # starts the app 

2.  軟體依賴性

3.  最新版本

4.  API參考

5.  建置和測試：

    要建立您的程式碼，請使用：

    ```bash
    $ cd threagile-monitoring
    $ hatch build
    ```

    若要使用 AI 進行拉取請求審查，請使用：

    <https://app.coderabbit.ai/dashboard>（使用`phpstan.neon`)

    要運行該應用程序，請使用：

    Linux：

    ```bash
    $ export SECRET_KEY="secret"
    ```

    視窗：

    ```bash
    $ setx SECRET_KEY secret
    ```

    然後：

    ```bash
    $ cd threagile-monitoring
    # Without hatch: $ python src/threagile_monitoring/app.py
    $ hatch run python src/threagile_monitoring/app.py
    ```

    然後，導航至`http://127.0.0.1:5000/`在您的網頁瀏覽器中。

    若要執行測試，請使用：

    ```bash
    $ cd threagile-monitoring
    $ pip install pytest # optional
    $ pytest tests/
    ```

# API Documentation

導航至`http://127.0.0.1:5000/docs` in your web browser, or download the openapi.json from `http://127.0.0.1:5000/openapi.json`.

# 指標

讓 Prometheus 這樣的工具刮擦`http://127.0.0.1:9464/metrics`.

**_新的_**

**目錄**

-   [安裝](#installation)
-   [版本來源](#version-source)
-   [環境](#environments)
-   [建造](#build)
-   [執照](#license)

## 安裝

```console
pip install threagile-monitoring
```

## 版本來源

-   這[孵化VCS](https://github.com/ofek/hatch-vcs)版本來源外掛程式使用 Git 標籤來確定專案版本

## 環境

-   整齊地定義在一個獨立的[`hatch.toml`](https://hatch.pypa.io/latest/intro/#configuration)
-   這`test`矩陣使用[孵化貨櫃](https://github.com/ofek/hatch-containers)用於運行 Docker 容器內每個環境的插件；用法可以在[測試](.github/workflows/test.yml)GitHub 工作流程

## 建造

-   所有建置目標都使用[孵化VCS](https://github.com/ofek/hatch-vcs)建立鉤子插件來發送`_version.py`文件，以便可以在運行時使用該版本
-   輪子使用[孵化 mypyc](https://github.com/ofek/hatch-mypyc)建立鉤子插件以首先編譯所有程式碼[Mypyc](https://github.com/mypyc/mypyc)
-   這[建造](.github/workflows/build.yml)GitHub 工作流程展示如何：
    -   使用[cibuildwheel](https://github.com/pypa/cibuildwheel)為每個平台分發二進制輪子
    -   使用[應用程式](https://hatch.pypa.io/latest/plugins/builder/app/)建構目標為每個平台建立獨立發行版

## 執照

`threagile-monitoring`是根據以下條款分發的[和](https://spdx.org/licenses/MIT.html)執照。

    === END:  UPDATE THIS SECTION FOR message board ===

## 前端

1）創建SvelteKit應用程式：

    $ cd containers/app
    $ npx sv create frontend
    Choose "SvelteKit demo"
    Choose Yes, using Typescript syntax
    Choose prettier, eslint, vitest, tailwindcss
    Choose typography, forms, container-queries
    Choose pnpm

後續步驟：

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

## 100 - 簡介

看[README.md](./100/README.md)

## 200 - 要求

看[README.md](./200/README.md)

## 300 - 建立我們的應用程式

看[README.md](./300/README.md)

## 400 - 結論

看[README.md](./400/README.md)
