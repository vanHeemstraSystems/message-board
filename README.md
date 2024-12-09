message-board
# Message Board

| | |
| --- | --- |
| CI/CD | [![CI - Server](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_server.yml/badge.svg)](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_server.yml) [![CD - Frontend](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_frontend.yml/badge.svg)](https://github.com/vanHeemstraSystems/message-board/actions/workflows/ci_frontend.yml) |
| Package | [![PyPI - Version](https://img.shields.io/pypi/v/message-board.svg?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.org/project/message-board/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/message-board.svg?logo=python&label=Python&logoColor=gold)](https://pypi.org/project/message-board/) |
| Meta | [![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch) [![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![types - Mypy](https://img.shields.io/badge/types-Mypy-blue.svg)](https://github.com/ambv/black) [![License - MIT](https://img.shields.io/badge/license-MIT-9400d3.svg)](https://spdx.org/licenses/) [![GitHub Sponsors](https://img.shields.io/github/sponsors/vanHeemstraSystems?logo=GitHub%20Sponsors&style=social)](https://github.com/sponsors/vanHeemstraSystems) |

-----

> A Message Board that will display submitted messages.

- [Documentation](./DOCUMENTATION.md)
- [Glossary](./GLOSSARY.md)
- [Images](./IMAGES.md)
- [References](./REFERENCES.md)
- [Telemetry](./TELEMETRY.md)

**Executive Summary**

## Server



## Frontend

1) Create the SvelteKit application:

```
$ cd containers/app
$ npx sv create frontend
Choose "SvelteKit demo"
Choose Yes, using Typescript syntax
Choose prettier, eslint, vitest, tailwindcss
Choose typography, forms, container-queries
Choose pnpm
```

Next steps:

```
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
```

## 100 - Introduction

See [README.md](./100/README.md)

## 200 - Requirements

See [README.md](./200/README.md)

## 300 - Building Our Application

See [README.md](./300/README.md)

## 400 - Conclusion

See [README.md](./400/README.md)
