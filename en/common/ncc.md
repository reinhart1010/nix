---
layout: page
title: common/ncc (English)
description: "Compile a Node.js application into a single file."
content_hash: e427425d405753fa2e204dbc008e6ab81d4196e6
---
# ncc

Compile a Node.js application into a single file.
Supports TypeScript, binary addons and dynamic requires.
More information: <https://github.com/vercel/ncc>.

- Bundle a Node.js application:

`ncc build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.js</span>

- Bundle and minify a Node.js application:

`ncc build --minify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.js</span>

- Bundle and minify a Node.js application and generate source maps:

`ncc build --source-map `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.js</span>

- Automatically recompile on changes to source files:

`ncc build --watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.js</span>

- Bundle a Node.js application into a temporary directory and run it for testing:

`ncc run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.js</span>

- Clean the `ncc` cache:

`ncc clean cache`
