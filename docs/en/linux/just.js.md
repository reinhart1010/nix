---
layout: page
title: linux/just.js (English)
description: "A V8 JavaScript runtime for Linux."
content_hash: 31e2ffeb39f9430fb502c03199f87287a030bb21
last_modified_at: 2023-11-12
related_topics:
  - title: Nederlands version
    url: /nl/linux/just.js.html
    icon: bi bi-globe
tldri18n_status: 2
---
# just

A V8 JavaScript runtime for Linux.
More information: <https://github.com/just-js/just>.

- Start a REPL (interactive shell):

`just`

- Run a JavaScript file:

`just `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.js</span>

- Evaluate JavaScript code by passing it as an argument:

`just eval "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>`"`

- Initialize a new project in a directory of the same name:

`just init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Build a JavaScript application into an executable:

`just build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.js</span>` --static`
