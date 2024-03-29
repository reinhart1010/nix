---
layout: page
title: common/webpack (English)
description: "Bundle a web project's js files and other assets into a single output file."
content_hash: 59e16ac4e96ee3175c5697f99bec780b293df9c4
last_modified_at: 2024-03-14
related_topics:
  - title: 한국어 version
    url: /ko/common/webpack.html
    icon: bi bi-globe
tldri18n_status: 2
---
# webpack

Bundle a web project's js files and other assets into a single output file.
More information: <https://webpack.js.org>.

- Create a single output file from an entry point file:

`webpack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app.js</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bundle.js</span>

- Load CSS files too from the JavaScript file (this uses the CSS loader for CSS files):

`webpack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app.js</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bundle.js</span>` --module-bind '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">css=css</span>`'`

- Pass a configuration file (with e.g. the entry script and the output filename) and show compilation progress:

`webpack --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">webpack.config.js</span>` --progress`

- Automatically recompile on changes to project files:

`webpack --watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app.js</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bundle.js</span>
