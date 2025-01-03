---
layout: page
title: common/popd (Nederlands)
description: "Verwijder een map van de directory stack die is geplaatst met de ingebouwde pushd-opdracht van de shell."
content_hash: d9b6891a8265df4ffe3c8b3b272759bbf6579dd4
last_modified_at: 2025-01-03
related_topics:
  - title: dansk version
    url: /da/common/popd.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/popd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/popd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/popd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# popd

Verwijder een map van de directory stack die is geplaatst met de ingebouwde pushd-opdracht van de shell.
Bekijk ook `pushd` om een map op de stapel te plaatsen en `dirs` om de inhoud van de stapel weer te geven.
Meer informatie: <https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html>.

- Verwijder de bovenste map van de stapel en ga ernaartoe:

`popd`

- Verwijder de N-de map (beginnend vanaf nul van links, uit de lijst die met `dirs` wordt weergegeven):

`popd +N`

- Verwijder de N-de map (beginnend vanaf nul van rechts, uit de lijst die met `dirs` wordt weergegeven):

`popd -N`

- Verwijder de eerste map (beginnend vanaf nul van links, uit de lijst die met `dirs` wordt weergegeven):

`popd -n`
