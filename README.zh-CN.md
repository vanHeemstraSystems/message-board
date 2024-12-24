留言板

# 留言板

|           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 持续集成/持续交付 | [![CI - Server](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_server.yml/badge.svg)](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_server.yml)[![CD - Frontend](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_frontend.yml/badge.svg)](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_frontend.yml)                                                                                                                                                                                         |
| 包裹        | [![PyPI - Version](https://img.shields.io/pypi/v/message-board.svg?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.org/project/message-board/)[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/message-board.svg?logo=python&label=Python&logoColor=gold)](https://pypi.org/project/message-board/)                                                                                                                                                                                                                                                                                 |
| 元         | [![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)[![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![types - Mypy](https://img.shields.io/badge/types-Mypy-blue.svg)](https://github.com/ambv/black)[![License - MIT](https://img.shields.io/badge/license-MIT-9400d3.svg)](https://spdx.org/licenses/)[![GitHub Sponsors](https://img.shields.io/github/sponsors/vanHeemstraSystems?logo=GitHub%20Sponsors&style=social)](https://github.com/sponsors/vanHeemstraSystems) |

* * *

> 留言板将显示提交的消息。

-   [文档](./DOCUMENTATION.md)
-   [词汇表](./GLOSSARY.md)
-   [图片](./IMAGES.md)
-   [参考](./REFERENCES.md)
-   [遥测](./TELEMETRY.md)

**执行摘要**

## GOES

我们建议使用[Cursor.io](https://www.cursor.com/)作为该项目的集成开发环境（IDE）。

## 服务器

在您自己的系统上启动并运行您的代码。

**笔记**: 确保您满足[要求](./200/README.md).

1.  **安装过程：**

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

    **笔记**：现代的方法是使用`pyproject.toml`安装依赖项，而不是\`\`\`requirements.txt。因此不应该有requirements.txt 文件。

    === 开始：更新留言板的这一部分 ===

    **使用 webpack 打包您的网站：**一旦你有了一个足够好的网站可供你使用，你就必须使用 webpack 打包应用程序。该包文件夹列于`.gitignore`以避免它被提交给 git。

    现在所有设置都应该准备就绪，因此您需要做的就是：
    1）`$ hatch shell`2)`(threagile-monitoring) $ cd src/threagile_monitoring`3)`(threagile-monitoring) $ npm install`4)`(threagile-monitoring) $ npm run build`

    这将创建`app.js`文件 - 包含所有组件 - 在`/src/threagile_monitoring/static/js/`.

    **使用webpack开发：**如果您仍在开发您的网站，**单独的终端会话**，按照上述安装过程后，执行以下操作：
    1）`$ hatch shell`2)`(threagile-monitoring) $ cd src/threagile_monitoring`3)`(threagile-monitoring) $ npm install`4)`(threagile-monitoring) $ npm run watch`

    这将 - 在单独的终端会话中（即`background`) - 不断地将您所做的更改加载到适当的文件中，同时您可以在初始终端会话中继续进行这些更改（即`foreground`）。因此，您不必在每次编辑后构建源代码，它会自动处理！

    要查看更改，只需保存并重新加载导航器（通常使用 F5）。

    确保在使用后端功能进行测试时运行您的网页，如下所示：
    1）`(threagile-monitoring) $ cd src/threagile_monitoring`2)`(threagile-monitoring) $ python app.py`

    **测试**

    以这种方式测试应用程序（前端）：

    1)`$ hatch shell`2)`(threagile-monitoring) $ cd src/threagile_monitoring`3)`(threagile-monitoring) $ npm install`4)`(threagile-monitoring) $ npm test`5)`(threagile-monitoring) $ npm test -- --coverage`

    **跑步：**

    如果不进行开发，请按以下方式运行应用程序（同时后端和前端）：

        $ hatch run python src/threagile_monitoring/app.py # starts the app 

2.  软件依赖性

3.  最新版本

4.  API参考

5.  构建和测试：

    要构建您的代码，请使用：

    ```bash
    $ cd threagile-monitoring
    $ hatch build
    ```

    要使用 AI 进行拉取请求审查，请使用：

    <https://app.coderabbit.ai/dashboard>（使用`phpstan.neon`)

    要运行该应用程序，请使用：

    Linux：

    ```bash
    $ export SECRET_KEY="secret"
    ```

    视窗：

    ```bash
    $ setx SECRET_KEY secret
    ```

    然后：

    ```bash
    $ cd threagile-monitoring
    # Without hatch: $ python src/threagile_monitoring/app.py
    $ hatch run python src/threagile_monitoring/app.py
    ```

    然后，导航至`http://127.0.0.1:5000/`在您的网络浏览器中。

    要运行测试，请使用：

    ```bash
    $ cd threagile-monitoring
    $ pip install pytest # optional
    $ pytest tests/
    ```

# 码头工人

**笔记**：为了有效利用资源，我们使用**柔和的**而不是**码头工人**!

将这些行添加到 ~/.zshrc 或 ~/.bashrc 中：

    alias docker=podman
    alias docker-compose='podman compose'

然后重新加载您的 shell 配置：

    $ source ~/.zshrc  # if using zsh
    # or
    $source ~/.bashrc # if using bash

通过 pip 安装 podman-compose：

    $ pip install podman-compose

验证安装：

    $ podman compose --version

# 检查是否存在任何 Podman 机器

    $ podman machine list

# 如果不存在机器，则创建一台

    $ podman machine init

# 启动 Podman 机器

    $ podman machine start

# 设置套接字路径

    $ export DOCKER_HOST=unix://$HOME/.local/share/containers/podman/machine/podman.sock

# 验证 Podman 是否正常工作

    $ podman ps

使用以下命令启动 Docker 容器：

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

这将启动三个容器：

-   留言板服务器-dev（端口 8080:5000）
-   留言板前端开发（端口 80:3000）
-   留言板数据库-dev（端口 5432:5432）
-   留言板-db-gui-dev（端口 5444:5444）

所有四个容器均成功运行。让我们验证每个服务：

1）前端（Vue.js）：

-   在浏览器中访问http&#x3A;//localhost:80

2）后端（Flask）：

-   在浏览器中访问http&#x3A;//localhost:8080/api/health
-   应返回健康检查响应

3）数据库（PostgreSQL）：

-   已经运行且健康（如状态所示）
-   可在本地主机上访问：5432

4）CloudBeaver（数据库图形用户界面）：

-   访问 http&#x3A;//localhost:8978
-   首次设置：
-   出现提示时创建管理员凭据
-   用户名：cbadmin
-   密码：S3cr3tPwd
-   点击“新连接”
-   选择“PostgreSQL”
-   输入连接详细信息：
-   主机：数据库
-   端口：5432
-   数据库：message_board_db
-   用户名：db-user-dev
-   密码：db-password-dev

DbVisualizer 应使用以下凭据连接到您的 PostgreSQL 数据库：

服务器：数据库
端口：5432
数据库：message_board_db
用户名：db-user-dev
密码：db-password-dev

如果 DbVisualizer 没有自动启动，您可以检查容器日志：

    $ docker logs message-board-db-gui-dev

# API文档

导航至`http://127.0.0.1:5000/docs`在您的网络浏览器中，或从以下位置下载 openapi.json`http://127.0.0.1:5000/openapi.json`.

# 指标

让像 Prometheus 这样的工具刮擦`http://127.0.0.1:9464/metrics`.

**_新的_**

**目录**

-   [安装](#installation)
-   [版本来源](#version-source)
-   [环境](#environments)
-   [建造](#build)
-   [执照](#license)

## 安装

```console
pip install threagile-monitoring
```

## 版本来源

-   这[孵化VCS](https://github.com/ofek/hatch-vcs)版本源插件使用 Git 标签确定项目版本

## 环境

-   整齐地定义在一个独立的[`hatch.toml`](https://hatch.pypa.io/latest/intro/#configuration)
-   这`test`矩阵使用[孵化集装箱](https://github.com/ofek/hatch-containers)用于运行 Docker 容器内每个环境的插件；用法可以在[测试](.github/workflows/test.yml)GitHub 工作流程

## 建造

-   所有构建目标都使用[孵化VCS](https://github.com/ofek/hatch-vcs)构建钩子插件来发送`_version.py`文件，以便可以在运行时使用该版本
-   轮子使用[孵化 mypyc](https://github.com/ofek/hatch-mypyc) build hook plugin to first compile all code with [Mypyc](https://github.com/mypyc/mypyc)
-   这[建造](.github/workflows/build.yml)GitHub 工作流程展示了如何：
    -   使用[cibuildwheel](https://github.com/pypa/cibuildwheel)为每个平台分发二进制轮子
    -   使用[应用程序](https://hatch.pypa.io/latest/plugins/builder/app/)构建目标为每个平台构建独立发行版

## 执照

`threagile-monitoring`是根据以下条款分发的[和](https://spdx.org/licenses/MIT.html)执照。

    === END:  UPDATE THIS SECTION FOR message board ===

## 前端

1）创建SvelteKit应用程序：

    $ cd containers/app
    $ npx sv create frontend
    Choose "SvelteKit demo"
    Choose Yes, using Typescript syntax
    Choose prettier, eslint, vitest, tailwindcss
    Choose typography, forms, container-queries
    Choose pnpm

后续步骤：

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

## 内存问题（在 Mac 上）：

您可以采取以下几个步骤来解决内存问题：

1.  **检查可用内存**:
    -   从 Apple 菜单中打开活动监视器。
    -   选择“内存”选项卡。
    -   查看“使用情况”列，了解当前使用了多少内存。

2.  **关闭不必要的应用程序**:
    -   确保您没有运行任何可能消耗内存的不必要的应用程序。

3.  **清除缓存**:
    -   有时，清除缓存可以帮助释放内存。

4.  **重新启动计算机**:
    -   有时，简单的重新启动就可以解决内存问题。

5.  **检查更新**:
    -   确保您的操作系统和应用程序是最新的。

6.  **检查内存泄漏**:
    -   使用 Valgrind 或 Instruments 等工具来检查应用程序中的内存泄漏。

7.  清除Docker资源：
    -   运行以下命令删除所有未使用的 Docker 资源：
        docker system prune -a

8.  Docker 桌面内存限制
    您可以限制 Docker Desktop 的资源使用：
    打开 Docker 桌面
    转到设置/首选项
    选择“资源”
    减少内存限制（例如，根据您的系统减少至 4-6GB）

9.  XQuartz 优化
    退出并重新启动 XQuartz
    考虑仅在需要时使用 XQuartz，而不是保持其运行

10. 系统级解决方案：
    清除系统缓存：

        sudo purge

    检查交换空间使用情况：

        sysctl vm.swapusage

11. 长期解决方案：

    -   升级您的硬件：

    -   考虑使用具有更多 RAM 的更强大的机器。

    -   优化您的应用程序：

    -   使用内存分析工具来识别和优化内存密集型操作。

    -   监控和管理资源：

    -   使用类似的工具`htop`或者`iostat`监控系统资源并有效管理它们。

    -   为 Docker 容器和映像设置自动清理脚本。

如果问题仍然存在，您可能需要：

    1. Monitor which application is consuming the most memory
    2. Consider alternatives to running all these applications simultaneously
    3. Use lightweight alternatives where possible (e.g., Podman instead of Docker Desktop)

## 100 - 简介

看[README.md](./100/README.md)

## 200 - 要求

看[README.md](./200/README.md)

## 300 - 构建我们的应用程序

看[README.md](./300/README.md)

## 400 - 结论

看[README.md](./400/README.md)
