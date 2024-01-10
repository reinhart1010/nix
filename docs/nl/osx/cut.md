---
layout: page
title: osx/cut (Nederlands)
description: "Snij velden eruit vanuit `stdin` of bestanden."
content_hash: 2b7da89e74a934d21c1021f788be023118f22d84
last_modified_at: 2024-01-10
related_topics:
  - title: English version
    url: /en/osx/cut.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/cut.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/cut.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/osx/cut.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cut

Snij velden eruit vanuit `stdin` of bestanden.
Meer informatie: <https://manned.org/man/freebsd-13.0/cut.1>.

- Toon een specifiek karakter/veldbereik voor iedere regel:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | cut -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c|f</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|1,10|1-10|1-|-10</span>

- Toon een bereik voor iedere regel met een specifieke scheiding:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | cut -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>`" -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Toon een bereik van iedere regel voor een specifiek bestand:

`cut -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
