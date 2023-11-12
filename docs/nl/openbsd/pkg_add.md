---
layout: page
title: openbsd/pkg_add (Nederlands)
description: "Installeer/update pakketten in OpenBSD."
content_hash: 0303d7ccaa6c692d060526918d032718ecdda3a0
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/openbsd/pkg_add.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkg_add

Installeer/update pakketten in OpenBSD.
Bekijk ook: `pkg_info`, `pkg_delete`.
Meer informatie: <https://man.openbsd.org/pkg_add>.

- Werk alle pakketten bij, inclusief afhankelijkheden:

`pkg_add -u`

- Installeer een nieuw pakket:

`pkg_add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Installeer pakketten van de onbewerkte uitvoer van `pkg_info`:

`pkg_add -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
