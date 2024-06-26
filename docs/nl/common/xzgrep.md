---
layout: page
title: common/xzgrep (Nederlands)
description: "Zoek bestanden die mogelijk worden gecomprimeerd met `xz`, `lzma`, `gzip`, `bzip2`, `lzop`, of `zstd` met behulp van reguliere expressies."
content_hash: 338c3b8c4938e98ab3c16e865463904a2edb4b88
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/common/xzgrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xzgrep

Zoek bestanden die mogelijk worden gecomprimeerd met `xz`, `lzma`, `gzip`, `bzip2`, `lzop`, of `zstd` met behulp van reguliere expressies.
Bekijk ook: `grep`.
Meer informatie: <https://manned.org/xzgrep>.

- Zoek naar een patroon in een bestand:

`xzgrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Zoek naar een exacte tekenreeks (schakelt reguliere expressies uit):

`xzgrep --fixed-strings "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exact_string</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Zoek naar een patroon in alle bestanden en geef de regelnummers weer van de overeenkomsten:

`xzgrep --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Gebruik uitgebreidere reguliere expressies (ondersteund `?`, `+`, `{}`, `()` en `|`), in case-ongevoelige modus:

`xzgrep --extended-regexp --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon 3 regels met context rond, voor of na elke overeenkomst:

`xzgrep --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">context|before-context|after-context</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon bestandsnaam en regelnummer voor elke overeenkomst met kleuren:

`xzgrep --with-filename --line-number --color=always "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Zoek naar regels die overeenkomen met een patroon en toon alleen de gematchte tekst:

`xzgrep --only-matching "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
