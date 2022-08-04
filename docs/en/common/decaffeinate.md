---
layout: page
title: common/decaffeinate (English)
description: "Move your CoffeeScript source to modern JavaScript."
content_hash: aa79bae63d8207c4dd984c681b400be7d4d0cf65
related_topics:
  - title: italiano version
    url: /it/common/decaffeinate.html
    icon: bi bi-globe
---
# decaffeinate

Move your CoffeeScript source to modern JavaScript.
More information: <https://decaffeinate-project.org>.

- Convert a CoffeeScript file to JavaScript:

`decaffeinate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.coffee</span>

- Convert a CoffeeScript v2 file to JavaScript:

`decaffeinate --use-cs2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.coffee</span>

- Convert require and `module.exports` to import and export:

`decaffeinate --use-js-modules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.coffee</span>

- Convert a CoffeeScript, allowing named exports:

`decaffeinate --loose-js-modules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.coffee</span>
