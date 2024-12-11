لوحة الرسائل

# لوحة الرسائل

|             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| سي آي/سي دي | [![CI - Server](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_server.yml/badge.svg)](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_server.yml)[![CD - Frontend](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_frontend.yml/badge.svg)](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_frontend.yml)                                                                                                                                                                                         |
| طَرد        | [![PyPI - Version](https://img.shields.io/pypi/v/message-board.svg?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.org/project/message-board/)[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/message-board.svg?logo=python&label=Python&logoColor=gold)](https://pypi.org/project/message-board/)                                                                                                                                                                                                                                                                                 |
| ميتا        | [![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)[![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![types - Mypy](https://img.shields.io/badge/types-Mypy-blue.svg)](https://github.com/ambv/black)[![License - MIT](https://img.shields.io/badge/license-MIT-9400d3.svg)](https://spdx.org/licenses/)[![GitHub Sponsors](https://img.shields.io/github/sponsors/vanHeemstraSystems?logo=GitHub%20Sponsors&style=social)](https://github.com/sponsors/vanHeemstraSystems) |

* * *

> لوحة الرسائل التي ستعرض الرسائل المقدمة.

-   [التوثيق](./DOCUMENTATION.md)
-   [مسرد](./GLOSSARY.md)
-   [الصور](./IMAGES.md)
-   [مراجع](./REFERENCES.md)
-   [القياس عن بعد](./TELEMETRY.md)

**ملخص تنفيذي**

## الخادم

الحصول على التعليمات البرمجية الخاصة بك وتشغيلها على النظام الخاص بك.

**ملحوظة**: تأكد من الوفاء[متطلبات](./200/README.md).

1.  **عملية التثبيت:**

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

    **ملحوظة**: الطريقة الحديثة هي الاستخدام`pyproject.toml`لتثبيت التبعيات، وليس \`\`\`requirements.txt. ومن ثم لا ينبغي أن يكون هناك ملف require.txt.

    === البدء: قم بتحديث هذا القسم للوحة الرسائل ===

    **حزم موقعك باستخدام حزمة الويب:**بمجرد أن يكون لديك موقع ويب جيد بما يكفي لاستخدامه، يجب عليك حزم التطبيق مع حزمة الويب. تم إدراج مجلد الحزمة هذا في`.gitignore`لتجنب ذلك يجب الالتزام بـ git.

    يجب أن تكون جميع الإعدادات جاهزة الآن، لذا كل ما عليك فعله:
    1)`$ hatch shell`2)`(threagile-monitoring) $ cd src/threagile_monitoring`3)`(threagile-monitoring) $ npm install`4)`(threagile-monitoring) $ npm run build`

    سيؤدي هذا إلى إنشاء`app.js`الملف - الذي يحتوي على جميع المكونات - في`/src/threagile_monitoring/static/js/`.

    **التطوير باستخدام حزمة الويب:**إذا كنت لا تزال تقوم بتطوير موقع الويب الخاص بك، في**جلسة طرفية منفصلة**، بعد اتباع عملية التثبيت المذكورة أعلاه، قم بما يلي:
    1)`$ hatch shell`2)`(threagile-monitoring) $ cd src/threagile_monitoring`3)`(threagile-monitoring) $ npm install`4)`(threagile-monitoring) $ npm run watch`

    سيؤدي هذا - في الجلسة الطرفية المنفصلة (أي`background`) - قم بتحميل التغييرات التي تجريها باستمرار على الملفات المناسبة، بينما يمكنك الاستمرار في إجراء هذه التغييرات - في الجلسة الطرفية الأولية (أي:`foreground`). لذلك لا يتوجب عليك بناء مصادرك بعد كل تعديل، بل يتم الاهتمام بها تلقائيًا!

    لرؤية التغييرات، ما عليك سوى حفظ متصفحك وإعادة تحميله (عادةً باستخدام F5).

    تأكد من تشغيل صفحة الويب الخاصة بك عند الاختبار باستخدام وظائف الواجهة الخلفية، كما يلي:
    1)`(threagile-monitoring) $ cd src/threagile_monitoring`2)`(threagile-monitoring) $ python app.py`

    **امتحان**

    اختبر التطبيق (الواجهة الأمامية) بهذه الطريقة:

    1)`$ hatch shell`2)`(threagile-monitoring) $ cd src/threagile_monitoring`3)`(threagile-monitoring) $ npm install`4)`(threagile-monitoring) $ npm test`5)`(threagile-monitoring) $ npm test -- --coverage`

    **يجري:**

    إذا لم يكن قيد التطوير، قم بتشغيل التطبيق (الواجهة الخلفية والواجهة الأمامية في وقت واحد) بهذه الطريقة:

        $ hatch run python src/threagile_monitoring/app.py # starts the app 

2.  تبعيات البرمجيات

3.  أحدث الإصدارات

4.  مراجع واجهة برمجة التطبيقات

5.  البناء والاختبار:

    لبناء الكود الخاص بك، استخدم:

    ```bash
    $ cd threagile-monitoring
    $ hatch build
    ```

    لاستخدام الذكاء الاصطناعي لمراجعات طلبات السحب، استخدم:

    <https://app.coderabbit.ai/dashboard>(الاستخدامات`phpstan.neon`)

    لتشغيل التطبيق استخدم:

    لينكس:

    ```bash
    $ export SECRET_KEY="secret"
    ```

    ويندوز:

    ```bash
    $ setx SECRET_KEY secret
    ```

    ثم:

    ```bash
    $ cd threagile-monitoring
    # Without hatch: $ python src/threagile_monitoring/app.py
    $ hatch run python src/threagile_monitoring/app.py
    ```

    ثم انتقل إلى`http://127.0.0.1:5000/`في متصفح الويب الخاص بك.

    لتشغيل الاختبارات استخدم:

    ```bash
    $ cd threagile-monitoring
    $ pip install pytest # optional
    $ pytest tests/
    ```

# عامل ميناء

ابدأ تشغيل حاويات Docker الخاصة بك باستخدام:

    $ cd containers/app
    $ docker compose --file docker-compose.dev.yml --project-name message-board-dev up --build -d

سيؤدي ذلك إلى تدوير ثلاث حاويات:

-   تطوير خادم لوحة الرسائل (المنفذ 8080:5000)
-   تطوير الواجهة الأمامية للوحة الرسائل (المنفذ 80:3000)
-   تطوير قاعدة بيانات لوحة الرسائل (المنفذ 5432:5432)

# وثائق واجهة برمجة التطبيقات

انتقل إلى`http://127.0.0.1:5000/docs`في متصفح الويب الخاص بك، أو قم بتنزيل openapi.json من`http://127.0.0.1:5000/openapi.json`.

# المقاييس

دع أداة مثل بروميثيوس تتخلص`http://127.0.0.1:9464/metrics`.

**_جديد_**

**جدول المحتويات**

-   [تثبيت](#installation)
-   [مصدر النسخة](#version-source)
-   [البيئات](#environments)
-   [يبني](#build)
-   [رخصة](#license)

## تثبيت

```console
pip install threagile-monitoring
```

## مصدر النسخة

-   ال[Hatch-vcs](https://github.com/ofek/hatch-vcs)يحدد البرنامج المساعد لمصدر الإصدار إصدار المشروع باستخدام علامات Git

## البيئات

-   تم تعريفها بدقة في قائمة بذاتها[`hatch.toml`](https://hatch.pypa.io/latest/intro/#configuration)
-   ال`test`تستخدم المصفوفة[حاويات الفتحة](https://github.com/ofek/hatch-containers)مكون إضافي لتشغيل كل بيئة داخل حاويات Docker؛ يمكن رؤية الاستخدام في[امتحان](.github/workflows/test.yml)سير عمل جيثب

## يبني

-   جميع أهداف البناء تستخدم[Hatch-vcs](https://github.com/ofek/hatch-vcs)بناء البرنامج المساعد هوك لشحن أ`_version.py`ملف بحيث يمكن استخدام الإصدار في وقت التشغيل
-   تستخدم العجلات[Hatch-mypyc](https://github.com/ofek/hatch-mypyc)أنشئ ملحقًا ربطًا لتجميع جميع التعليمات البرمجية أولاً[Mypyc](https://github.com/mypyc/mypyc)
-   ال[يبني](.github/workflows/build.yml)يوضح سير عمل GitHub كيفية:
    -   يستخدم[cibuildwheel](https://github.com/pypa/cibuildwheel)لتوزيع العجلات الثنائية لكل منصة
    -   استخدم[برنامج](https://hatch.pypa.io/latest/plugins/builder/app/)بناء الهدف لبناء توزيعات مستقلة لكل منصة

## رخصة

`threagile-monitoring`يتم توزيعها بموجب شروط[مع](https://spdx.org/licenses/MIT.html)رخصة.

    === END:  UPDATE THIS SECTION FOR message board ===

## الواجهة الأمامية

1) قم بإنشاء تطبيق SvelteKit:

    $ cd containers/app
    $ npx sv create frontend
    Choose "SvelteKit demo"
    Choose Yes, using Typescript syntax
    Choose prettier, eslint, vitest, tailwindcss
    Choose typography, forms, container-queries
    Choose pnpm

الخطوات التالية:

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

## 100- مقدمة

يرى[README.md](./100/README.md)

## 200 - المتطلبات

يرى[README.md](./200/README.md)

## 300 – بناء تطبيقنا

يرى[README.md](./300/README.md)

## 400 - الخاتمة

يرى[README.md](./400/README.md)
