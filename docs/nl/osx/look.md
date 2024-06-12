---
layout: page
title: osx/look (Nederlands)
description: "Toon regels die beginnen met een prefix in een gesorteerd bestand."
content_hash: c8476a34515341dad1f6aa30ac3a672906b90c25
last_modified_at: 2024-06-12
related_topics:
  - title: English version
    url: /en/osx/look.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/look.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/look.html
    icon: bi bi-globe
tldri18n_status: 2
---
# look

Toon regels die beginnen met een prefix in een gesorteerd bestand.
Bekijk ook: `grep`, `sort`.
Meer informatie: <https://keith.github.io/xcode-man-pages/look.1.html>.

- Zoek naar regels die beginnen met een specifieke prefix in een specifiek bestand:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Zoek hoofdletterongevoelig alleen op alfanumerieke tekens:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--ignore-case</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--alphanum</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Specificeer een string-terminatiekarakter (standaard is spatie):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--terminate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>

- Zoek in `/usr/share/dict/words` (`--ignore-case` en `--alphanum` worden aangenomen):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>
