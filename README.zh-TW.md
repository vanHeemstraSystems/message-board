留言板

# Message Board

> 斯拉格萊恩

-   [詞彙表](./GLOSSARY.md)
-   [參考](./REFERENCES.md)
-   [文件](./DOCUMENTATION.md)
-   [遙測](./TELEMETRY.md)

**執行摘要**

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
    │  4: git init && git add -A && git commit -m "Initial commit" (optional)  │
    │  5: pnpm dev --open                                                      │
    │                                                                          │
    │  To close the dev server, hit Ctrl-C                                     │
    │                                                                          │
    │  Stuck? Visit us at https://svelte.dev/chat                              |
    |                                                                          |
    |  6: pnpm run build # creates a new build folder with production version  |
    |  7: pnpm run preview # creates a preview of the production version       |

## 100 - 簡介

看[README.md](./100/README.md)

## 200 - 要求

看[README.md](./200/README.md)

## 300 - 建立我們的應用程式

看[README.md](./300/README.md)

## 400 - 結論

看[README.md](./400/README.md)
