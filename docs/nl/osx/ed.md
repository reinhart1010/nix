---
layout: page
title: osx/ed (Nederlands)
description: "De originele Unix tekst editor."
content_hash: f27cdb70582ddc16d9c839ec914855d2ae425f57
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/osx/ed.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/ed.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/ed.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/osx/ed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ed

De originele Unix tekst editor.
Bekijk ook: `awk`, `sed`.
Meer informatie: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- Start een interactieve editor sessie met een leeg document:

`ed`

- Start een interactieve editor sessie met een leeg document en een specifieke [p]rompt:

`ed -p '> '`

- Start een interactieve editor sessie met een leeg document en zonder diagnostics, het aantal bytes en de '!' prompt:

`ed -s`

- Pas een specifiek bestand aan (dit toont het aantal bytes van het geladen bestand):

`ed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Vervang een string met een specifieke vervanging voor alle regels:

`,s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reguliere_expressie</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vervanging</span>`/g`
