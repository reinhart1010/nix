---
layout: page
title: common/look (Nederlands)
description: "Toon regels die beginnen met een prefix in een gesorteerd bestand."
content_hash: b861ac03ada6af1ceeb3d1aa789faf46afcc63e2
last_modified_at: 2024-06-12
related_topics:
  - title: English version
    url: /en/common/look.html
    icon: bi bi-globe
tldri18n_status: 2
---
# look

Toon regels die beginnen met een prefix in een gesorteerd bestand.
Let op: de regels in het bestand moeten gesorteerd zijn.
Bekijk ook: `grep`, `sort`.
Meer informatie: <https://man.openbsd.org/look>.

- Zoek naar regels die beginnen met een specifieke prefix in een specifiek bestand:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Zoek hoofdletterongevoelig ([f]) alleen op alfanumerieke tekens ([d]):

`look -f -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Specificeer een string-[t]erminatiekarakter (standaard is spatie):

`look -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>

- Zoek in `/usr/share/dict/words` (`--ignore-case` en `--alphanum` worden aangenomen):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>
