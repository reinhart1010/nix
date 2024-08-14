---
layout: page
title: osx/bc (Nederlands)
description: "Een rekenmachinetaal met willekeurige precisie."
content_hash: 3a8251c00f24e638e6aaf67c217f60170851a68d
last_modified_at: 2024-08-14
related_topics:
  - title: English version
    url: /en/osx/bc.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/bc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/bc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bc

Een rekenmachinetaal met willekeurige precisie.
Zie ook: `dc`.
Meer informatie: <https://keith.github.io/xcode-man-pages/bc.1.html>.

- Start een interactieve sessie:

`bc`

- Start een interactieve sessie met de standaard wiskundige bibliotheek ingeschakeld:

`bc --mathlib`

- Bereken een uitdrukking:

`bc --expression='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`'`

- Voer een script uit:

`bc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/script.bc</span>

- Bereken een uitdrukking met de gespecificeerde schaal:

`bc --expression='scale = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`'`

- Bereken een sinus/cosinus/arctangens/natuurlijke logaritme/exponentiële functie met behulp van `mathlib`:

`bc --mathlib --expression='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|c|a|l|e</span>`(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`)'`
