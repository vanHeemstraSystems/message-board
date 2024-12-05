संदेश-बोर्ड

# संदेश बोर्ड

> स्लगलाइन

-   [शब्दकोष](./GLOSSARY.md)
-   [संदर्भ](./REFERENCES.md)
-   [प्रलेखन](./DOCUMENTATION.md)
-   [टेलीमेटरी](./TELEMETRY.md)

**कार्यकारी सारांश**

1) SvelteKit एप्लिकेशन बनाएं:

    $ cd containers/app
    $ npx sv create frontend
    Choose "SvelteKit demo"
    Choose Yes, using Typescript syntax
    Choose prettier, eslint, vitest, tailwindcss
    Choose typography, forms, container-queries
    Choose pnpm

Next steps:

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

## 100 - परिचय

देखना[README.md](./100/README.md)

## 200 - आवश्यकताएँ

देखना[README.md](./200/README.md)

## 300 - Building Our Application

देखना[README.md](./300/README.md)

## 400 - निष्कर्ष

देखना[README.md](./400/README.md)
