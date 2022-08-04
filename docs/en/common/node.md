---
layout: page
title: common/node (English)
description: "Server-side JavaScript platform (Node.js)."
content_hash: 4e9f57c8cc98aca71a5c23bde48f17d2fdcdb13f
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
  - title: português (Brasil) version
    url: /pt_BR/common/node.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/node.html
    icon: bi bi-globe
---
# node

Server-side JavaScript platform (Node.js).
More information: <https://nodejs.org>.

- Run a JavaScript file:

`node `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Start a REPL (interactive shell):

`node`

- Evaluate JavaScript code by passing it as an argument:

`node -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>`"`

- Evaluate and print result, useful to see node's dependencies versions:

`node -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process.versions</span>`"`

- Activate inspector, pausing execution until a debugger is connected once source code is fully parsed:

`node --no-lazy --inspect-brk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
