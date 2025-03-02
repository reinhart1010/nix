---
layout: page
title: common/pathchk (Nederlands)
description: "Controleer de geldigheid en draagbaarheid van padnamen."
content_hash: 82867ad337c6697e9f046e8d8d492499aeeb5651
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/pathchk.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pathchk.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/pathchk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pathchk

Controleer de geldigheid en draagbaarheid van padnamen.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/pathchk-invocation.html>.

- Controleer padnamen op geldigheid in het huidige systeem:

`pathchk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad1 pad2 …</span>

- Controleer padnamen op geldigheid in een breder scala van POSIX-conforme systemen:

`pathchk -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad1 pad2 …</span>

- Controleer padnamen op geldigheid in alle POSIX-conforme systemen:

`pathchk --portability `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad1 pad2 …</span>

- Controleer alleen op lege padnamen of leidende streepjes (-):

`pathchk -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad1 pad2 …</span>
