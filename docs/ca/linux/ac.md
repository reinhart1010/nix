---
layout: page
title: linux/ac (català)
description: "Imprimeix estadístiques sonre el temps de connexió dels usuaris."
content_hash: a6d27bfa892f36a0b0ec18baef891a6dad20d19f
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/ac.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ac.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/ac.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ac.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/ac.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/ac.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/linux/ac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/ac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ac

Imprimeix estadístiques sonre el temps de connexió dels usuaris.
Més informació: <https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- Imprimeix el temps de connexió del usuari actual en hores:

`ac`

- Imprimeix el temps total de connexió de tots els usuaris en hores:

`ac --individual-totals`

- Imprimeix el temps total de connexió d'un usuari concret en hores:

`ac --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_usuari</span>

- Imprimeix el temps de connexió d'un usuari concret en hores per dia (amb total):

`ac --daily-totals --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_usuari</span>

- Mostra també detalls adicionals:

`ac --compatibility`
