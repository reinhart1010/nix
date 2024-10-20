---
layout: page
title: common/tsc (English)
description: "TypeScript compiler."
content_hash: f0b786e12c5586fd4a3f3cc4a941f7ef03b9cc71
last_modified_at: 2024-10-20
tldri18n_status: 2
---
# tsc

TypeScript compiler.
More information: <https://www.typescriptlang.org/docs/handbook/compiler-options.html>.

- Compile a TypeScript file `foobar.ts` into a JavaScript file `foobar.js`:

`tsc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foobar.ts</span>

- Compile a TypeScript file into JavaScript using a specific target syntax (default is `ES3`):

`tsc --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ES5|ES2015|ES2016|ES2017|ES2018|ESNEXT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foobar.ts</span>

- Compile a TypeScript file into a JavaScript file with a custom name:

`tsc --outFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.js</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.ts</span>

- Compile all `.ts` files of a TypeScript project defined in a `tsconfig.json` file:

`tsc --build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tsconfig.json</span>

- Run the compiler using command-line options and arguments fetched from a text file:

`tsc @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">args.txt</span>

- Type-check multiple JavaScript files, and output only the errors:

`tsc --allowJs --checkJs --noEmit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">src/**/*.js</span>

- Run the compiler in watch mode, which automatically recompiles code when it changes:

`tsc --watch`
