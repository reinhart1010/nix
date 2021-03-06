---
layout: page
title: common/ts-node (English)
description: "Run TypeScript code directly, without any compiling."
content_hash: 9af3546b489d57342bbec2068894f7fe223bd14d
---
# ts-node

Run TypeScript code directly, without any compiling.
More information: <https://typestrong.org/ts-node>.

- Execute a TypeScript file without compiling (`node` + `tsc`):

`ts-node `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ts</span>

- Execute a TypeScript file without loading `tsconfig.json`:

`ts-node --skip-project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ts</span>

- Evaluate TypeScript code passed as a literal on the command-line:

`ts-node --eval '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">console.log("Hello World")</span>`'`

- Execute a TypeScript file in script mode:

`ts-node --script-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ts</span>

- Transpile a TypeScript file to JavaScript without executing it:

`ts-node --transpile-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ts</span>

- Display TS-Node help:

`ts-node --help`
