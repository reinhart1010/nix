---
layout: page
title: linux/just-js (English)
description: "A V8 JavaScript runtime for Linux."
content_hash: 31e2ffeb39f9430fb502c03199f87287a030bb21
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># just

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
