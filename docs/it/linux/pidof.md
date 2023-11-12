---
layout: page
title: linux/pidof (italiano)
description: "Ottiene l'ID di un processo a partire dal suo nome."
content_hash: 31c52f2d76252aa188927c574a4138835bf29aba
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/pidof.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pidof

Ottiene l'ID di un processo a partire dal suo nome.
Maggiori informazioni: <https://manned.org/pidof>.

- Elenca gli ID di tutti i processi con un dato nome:

`pidof `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash</span>

- Elenca un solo ID di processo con il nome specificato:

`pidof -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash</span>

- Elenca gli ID dei processi con un dato includendo anche gli script:

`pidof -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.py</span>

- Uccide tutti i processi con un dato nome:

`kill $(pidof `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>`)`
