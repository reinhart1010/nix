---
layout: page
title: openbsd/pkg_add (polski)
description: "Instaluj/aktualizuj pakiety w OpenBSD."
content_hash: f35e2991bd4a4675fd5e6fbbd98d904716797dcb
last_modified_at: 2024-05-09
related_topics:
  - title: English version
    url: /en/openbsd/pkg_add.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/openbsd/pkg_add.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/openbsd/pkg_add.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkg_add

Instaluj/aktualizuj pakiety w OpenBSD.
Zobacz także: `pkg_info`, `pkg_delete`.
Więcej informacji: <https://man.openbsd.org/pkg_add>.

- Zaktualizuj wszystkie pakiety, w tym zależności:

`pkg_add -u`

- Zainstaluj nowy pakiet:

`pkg_add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Zainstaluj pakiety z surowego wyjścia `pkg_info`:

`pkg_add -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>
