---
layout: page
title: common/strings (Nederlands)
description: "Vind printbare strings in een object bestand of binary."
content_hash: 5de429156953259f0c73f068dc2ea1d8b9c42968
last_modified_at: 2023-12-19
related_topics:
  - title: English version
    url: /en/common/strings.html
    icon: bi bi-globe
tldri18n_status: 2
---
# strings

Vind printbare strings in een object bestand of binary.
Meer informatie: <https://manned.org/strings>.

- Print alle strings in een binary:

`strings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Limiteer resultaten van strings met minimaal n karakters lang:

`strings -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Prefix ieder resultaat met de offset in het bestand:

`strings -t d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Prefix ieder resultaat met de offset in het bestand als hexadecimaal:

`strings -t x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
