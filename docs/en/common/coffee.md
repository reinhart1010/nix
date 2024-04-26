---
layout: page
title: common/coffee (English)
description: "Execute CoffeeScript scripts or compiles them into JavaScript."
content_hash: e9ed6985461dc1ece6542c404585e1da77fa5f7e
last_modified_at: 2024-04-26
related_topics:
  - title: italiano version
    url: /it/common/coffee.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/coffee.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/coffee.html
    icon: bi bi-globe
tldri18n_status: 2
---
# coffee

Execute CoffeeScript scripts or compiles them into JavaScript.
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
