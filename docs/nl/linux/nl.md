---
layout: page
title: linux/nl (Nederlands)
description: "Voorzie regels van een nummer uit een bestand of van `stdin`."
content_hash: b8b319d54140db95f9f1ba67932b151e376124ba
last_modified_at: 2024-06-25
related_topics:
  - title: English version
    url: /en/linux/nl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/nl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nl

Voorzie regels van een nummer uit een bestand of van `stdin`.
Meer informatie: <https://manned.org/nl.1p>.

- Voorzie niet-lege regels in een bestand van een nummer:

`nl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Lees van `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | nl -`

- Nummer [a]lle [b]ody regels inclusief lege regels of [n]ummer geen [b]ody regels:

`nl --body-numbering `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a|n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Nummer alleen de [b]ody regels die overeenkomen met een basis reguliere expressie (BRE) [p]atroon:

`nl --body-numbering p'FooBar[0-9]' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Gebruik een specifieke [i]ncrement voor regelnummering:

`nl --line-increment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">increment</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Specificeer het nummeringsformaat voor regels: [r]echts of [l]inks uitgelijnd, met of zonder voorloopnullen ([z]eros):

`nl --number-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rz|ln|rn</span>

- Specificeer de breedte van de nummering (standaard is 6):

`nl --number-width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kolombreedte</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Gebruik een specifieke string om de regelnummers van de regels te scheiden (standaard is TAB):

`nl --number-separator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scheidingsteken</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
