message-board
# Message Board

> Slugline

- [Documentation](./DOCUMENTATION.md)
- [Glossary](./GLOSSARY.md)
- [Images](./IMAGES.md)
- [References](./REFERENCES.md)
- [Telemetry](./TELEMETRY.md)

**Executive Summary**

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
