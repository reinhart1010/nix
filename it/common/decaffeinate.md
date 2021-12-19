---
layout: page
title: common/decaffeinate (italiano)
description: "Converti script CoffeScript in JavaScript moderno."
content_hash: af9279098d942515235b6f142a8f6a75f7f269b5
related_topics:
  - title: English version
    url: /en/common/decaffeinate.html
    icon: bi bi-globe
---
# decaffeinate

Converti script CoffeScript in JavaScript moderno.
Maggiori informazioni: <https://decaffeinate-project.org>.

- Converti un file CoffeeScript in JavaScript:

`decaffeinate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file.coffee</span>

- Converti un file CoffeeScript v2 in JavaScript:

`decaffeinate --use-cs2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file.coffee</span>

- Converti `require` e `module.exports` in `import` ed `export`:

`decaffeinate --use-js-modules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file.coffee</span>

- Converti un file CoffeeScript, permettendo di esportare nomi:

`decaffeinate --loose-js-modules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file.coffee</span>
