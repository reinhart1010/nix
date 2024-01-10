---
layout: page
title: linux/csplit (Nederlands)
description: "Splits een bestand in stukken."
content_hash: 8563997e1c02838f6c633fed928381fde7a265a7
last_modified_at: 2024-01-10
related_topics:
  - title: English version
    url: /en/linux/csplit.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/csplit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# csplit

Splits een bestand in stukken.
Dit genereert bestanden zoals "xx00", "xx01" etc.
Meer informatie: <https://www.gnu.org/software/coreutils/csplit>.

- Splits een bestand op regels 5 en 23:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` 5 23`

- Splits een bestand iedere 5 regels (dit zal falen als het totaal aantal regels niet deelbaar is door 5):

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` 5 {*}`

- Splits een bestand iedere 5 regels en negeer de exacte verdeeldheid error:

`csplit -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` 5 {*}`

- Splits een bestand op regel 5 en gebruik een aangepaste prefix voor de uitvoerbestanden:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` 5 -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>

- Splits een bestand op een regel die overeenkomt met de reguliere expressie:

`csplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reguliere_expressie</span>`/`
