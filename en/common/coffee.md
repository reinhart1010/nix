---
layout: page
title: common/coffee (English)
description: "Executes CoffeeScript scripts or compiles them into JavaScript."
content_hash: 26c985922ea95f2dd9c54d2d3243dbb956b128a5
related_topics:
  - title: italiano version
    url: /it/common/coffee.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/coffee.html
    icon: bi bi-globe
---
# coffee

Executes CoffeeScript scripts or compiles them into JavaScript.
More information: <https://coffeescript.org#cli>.

- Run a script:

`coffee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.coffee</span>

- Compile to JavaScript and save to a file with the same name:

`coffee --compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.coffee</span>

- Compile to JavaScript and save to a given output file:

`coffee --compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.coffee</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.js</span>

- Start a REPL (interactive shell):

`coffee --interactive`

- Watch script for changes and re-run script:

`coffee --watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.coffee</span>
