---
layout: page
title: common/webpack (English)
description: "Bundle a web project's js files and other assets into a single output file."
content_hash: b786259688c72a923fd66bf8271f446258da6106
---
# webpack

Bundle a web project's js files and other assets into a single output file.
More information: <https://webpack.js.org>.

- Create a single output file from an entry point file:

`webpack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app.js</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bundle.js</span>

- Load CSS files too from the JavaScript file (this uses the CSS loader for `.css` files):

`webpack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app.js</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bundle.js</span>` --module-bind '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">css=css</span>`'`

- Pass a config file (with e.g. the entry script and the output filename) and show compilation progress:

`webpack --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">webpack.config.js</span>` --progress`

- Automatically recompile on changes to project files:

`webpack --watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app.js</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bundle.js</span>
