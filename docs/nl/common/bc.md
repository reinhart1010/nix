---
layout: page
title: common/bc (Nederlands)
description: "Een rekenmachinetaal met willekeurige precisie."
content_hash: cd4a8397125c9b32afcf64bdc2cdff4ff49c1292
last_modified_at: 2025-01-03
related_topics:
  - title: English version
    url: /en/common/bc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bc.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bc.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/bc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bc

Een rekenmachinetaal met willekeurige precisie.
Bekijk ook: `dc`, `qalc`.
Meer informatie: <https://manned.org/bc>.

- Start een interactieve sessie:

`bc`

- Start een [i]nteractieve sessie met de standaard wiskundige [b]ibliotheek ingeschakeld:

`bc --interactive --mathlib`

- Bereken een uitdrukking:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`' | bc`

- Voer een script uit:

`bc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/script.bc</span>

- Bereken een uitdrukking met de gespecificeerde schaal:

`echo 'scale = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`' | bc`

- Bereken een sinus/cosinus/arctangens/natuurlijke logaritme/exponentiële functie met behulp van `mathlib`:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|c|a|l|e</span>`(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`)' | bc --mathlib`

- Voer een inline faculteitsscript uit:

`echo "define factorial(n) { if (n <= 1) return 1; return n*factorial(n-1); }; factorial(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`)" | bc`
