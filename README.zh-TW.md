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

## GOES

我們建議使用[Cursor.io](https://www.cursor.com/)作為該專案的整合開發環境（IDE）。

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
    # Version: 0.1.0 # it takes this from src/message_board/__about__.py
    # ...
    (server) $ python -c "import sys;print(sys.executable)" # optional, see where your environment's python is located
    (server) $ pip install --upgrade pip # optional, the `run` command allows you to execute commands in an environment as if you had already entered it.
    (server) $ exit # optional, type `exit` to leave the environment
    ```

    **筆記**: 現代的方法是使用`pyproject.toml`安裝依賴項，而不是\`\`\`requirements.txt。因此不應該有requirements.txt 檔案。

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

    以這種方式測試應用程式（前端）：

    1)`$ hatch shell`2)`(threagile-monitoring) $ cd src/threagile_monitoring`3)`(threagile-monitoring) $ npm install`4)`(threagile-monitoring) $ npm test`5)`(threagile-monitoring) $ npm test -- --coverage`

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

# 碼頭工人

**筆記**：為了有效利用資源，我們使用**柔和的**而不是**碼頭工人**!

將這些行加入 ~/.zshrc 或 ~/.bashrc 中：

    alias docker=podman
    alias docker-compose='podman compose'

然後重新載入您的 shell 配置：

    source ~/.zshrc  # if using zsh
    # or
    source ~/.bashrc # if using bash

透過 pip 安裝 podman-compose：

    pip install podman-compose

驗證安裝：

    podman compose --version

設定 Podman 套接字環境變數：

    export DOCKER_HOST=unix:///run/podman/podman.sock

使用以下命令啟動 Docker 容器：

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

這將啟動三個容器：

-   留言板伺服器-dev（連接埠 8080:5000）
-   留言板前端開發（連接埠 80:3000）
-   留言板資料庫-dev（連接埠 5432:5432）
-   留言板-db-gui-dev（連接埠 5444:5444）

DbVisualizer 應使用下列憑證連接到您的 PostgreSQL 資料庫：

伺服器：資料庫
埠：5432
資料庫：message_board_db
使用者名稱：db-user-dev
密碼：db-password-dev

如果 DbVisualizer 沒有自動啟動，您可以檢查容器日誌：

    $ docker logs message-board-db-gui-dev

# API文件

導航至`http://127.0.0.1:5000/docs`在您的網頁瀏覽器中，或從下列位置下載 openapi.json`http://127.0.0.1:5000/openapi.json`.

# 指標

讓像 Prometheus 這樣的工具刮擦`http://127.0.0.1:9464/metrics`.

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

## 記憶體問題（在 Mac 上）：

您可以採取以下幾個步驟來解決記憶體問題：

1.  **檢查可用內存**:
    -   從 Apple 選單中開啟活動監視器。
    -   選擇“內存”標籤。
    -   查看「使用情況」列，以了解目前使用了多少記憶體。

2.  **關閉不必要的應用程式**:
    -   確保您沒有運行任何可能消耗記憶體的不必要的應用程式。

3.  **清除快取**:
    -   有時，清除快取可以幫助釋放記憶體。

4.  **重新啟動計算機**:
    -   有時，簡單的重新啟動就可以解決記憶體問題。

5.  **檢查更新**:
    -   確保您的作業系統和應用程式是最新的。

6.  **檢查內存洩漏**:
    -   使用 Valgrind 或 Instruments 等工具來檢查應用程式中的記憶體洩漏。

7.  清除Docker資源：
    -   執行以下命令刪除所有未使用的 Docker 資源：
        docker system prune -a

8.  Docker 桌面記憶體限制
    您可以限制 Docker Desktop 的資源使用：
    開啟 Docker 桌面
    轉到設定/首選項
    選擇“資源”
    減少記憶體限制（例如，根據您的系統減少至 4-6GB）

9.  XQuartz 優化
    退出並重新啟動 XQuartz
    考慮僅在需要時使用 XQuartz，而不是保持其運行

10. 系統級解決方案：
    清除系統快取：

        sudo purge

    檢查交換空間使用：

        sysctl vm.swapusage

11. 長期解決方案：

    -   升級您的硬體：

    -   考慮使用具有更多 RAM 的更強大的機器。

    -   優化您的應用程式：

    -   使用記憶體分析工具來識別和優化記憶體密集型操作。

    -   監控與管理資源：

    -   使用類似的工具`htop`或者`iostat`監控系統資源並有效管理它們。

    -   為 Docker 容器和映像設定自動清理腳本。

如果問題仍然存在，您可能需要：

    1. Monitor which application is consuming the most memory
    2. Consider alternatives to running all these applications simultaneously
    3. Use lightweight alternatives where possible (e.g., Podman instead of Docker Desktop)

## 100 - 簡介

看[README.md](./100/README.md)

## 200 - 要求

看[README.md](./200/README.md)

## 300 - 建立我們的應用程式

看[README.md](./300/README.md)

## 400 - 結論

看[README.md](./400/README.md)
