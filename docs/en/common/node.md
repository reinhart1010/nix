---
layout: page
title: common/node (English)
description: "Server-side JavaScript platform (Node.js)."
content_hash: fc60706b3dde876ea3073212cd140d3e8a693614
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/node.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/node.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/node.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/node.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/node.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/node.html
    icon: bi bi-globe
tldri18n_status: 2
---
# node

Server-side JavaScript platform (Node.js).
More information: <https://nodejs.org>.

- Run a JavaScript file:

`node `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Start a REPL (interactive shell):

`node`

- Execute the specified file restarting the process when an imported file is changed (requires Node.js version 18.11+):

`node --watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Evaluate JavaScript code by passing it as an argument:

`node -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>`"`

- Evaluate and print the result, useful to print node's dependencies versions:

`node -p "process.versions"`

- Activate inspector, pausing execution until a debugger is connected once source code is fully parsed:

`node --no-lazy --inspect-brk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
