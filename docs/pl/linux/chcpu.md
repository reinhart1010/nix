---
layout: page
title: linux/chcpu (polski)
description: "Włącza/wyłącza CPU w systemie."
content_hash: 352c495e02df03e76b3382a364a4f8b31e940d9f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/chcpu.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chcpu

Włącza/wyłącza CPU w systemie.
Więcej informacji: <https://manned.org/chcpu>.

- Wyłączenie CPU przez podanie listy numerów ID CPU:

`chcpu -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,3</span>

- Włączenie zbioru CPU przez podanie zakresu numerów ID CPU:

`chcpu -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-10</span>
