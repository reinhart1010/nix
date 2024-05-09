---
layout: page
title: openbsd/pkg_delete (polski)
description: "Usuwaj pakiety w OpenBSD."
content_hash: 3b347301f4df8364b2e0ac2bd412574e8367f903
last_modified_at: 2024-05-09
related_topics:
  - title: English version
    url: /en/openbsd/pkg_delete.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/openbsd/pkg_delete.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/openbsd/pkg_delete.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkg_delete

Usuwaj pakiety w OpenBSD.
Zobacz także: `pkg_add`, `pkg_info`.
Więcej informacji: <https://man.openbsd.org/pkg_delete>.

- Usuń pakiet:

`pkg_delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Usuń pakiet wraz z jego nieużywanymi zależnościami:

`pkg_delete -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Usuń pakiet "na sucho":

`pkg_delete -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>
