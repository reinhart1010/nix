---
layout: page
title: openbsd/pkg_info (polski)
description: "Wyświetl informację o pakietach w OpenBSD."
content_hash: 10b73800f8053135e8edf2cc9f6886f5ba82871c
last_modified_at: 2024-05-09
related_topics:
  - title: English version
    url: /en/openbsd/pkg_info.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/openbsd/pkg_info.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/openbsd/pkg_info.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkg_info

Wyświetl informację o pakietach w OpenBSD.
Zobacz także: `pkg_add`, `pkg_delete`.
Więcej informacji: <https://man.openbsd.org/pkg_info>.

- Wyszukaj pakiet, używając jego nazwy:

`pkg_info -Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Wyświetl listę zainstalowanych pakietów do użycia z `pkg_add -l`:

`pkg_info -mz`
