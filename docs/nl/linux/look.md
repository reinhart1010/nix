---
layout: page
title: linux/look (Nederlands)
description: "Toon regels die beginnen met een prefix in een gesorteerd bestand."
content_hash: c5bd3309432a0a8b768d785293c39416fc0b0867
last_modified_at: 2024-06-12
related_topics:
  - title: English version
    url: /en/linux/look.html
    icon: bi bi-globe
tldri18n_status: 2
---
# look

Toon regels die beginnen met een prefix in een gesorteerd bestand.
Let op: de regels in het bestand moeten gesorteerd zijn.
Bekijk ook: `grep`, `sort`.
Meer informatie: <https://manned.org/look>.

- Zoek naar regels die beginnen met een specifieke prefix in een specifiek bestand:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Zoek hoofdletterongevoeling alleen op lege en alfanumerieke tekens:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--ignore-case</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--alphanum</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Specificeer een string-terminatiekarakter (standaard is spatie):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--terminate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>

- Zoek in `/usr/share/dict/words` (`--ignore-case` en `--alphanum` worden aangenomen):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>

- Zoek in `/usr/share/dict/web2` (`--ignore-case` en `--alphanum` worden aangenomen):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--alternative</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>
