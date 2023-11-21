---
layout: page
title: windows/slmgr.vbs (Nederlands)
description: "Installeer, activeer en beheer Windows licenties."
content_hash: e6c6539c6ad3f10d39134312e0fa5d4bda7a6e65
last_modified_at: 2023-11-21
related_topics:
  - title: English version
    url: /en/windows/slmgr.vbs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/slmgr.vbs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># slmgr.vbs

Installeer, activeer en beheer Windows licenties.
Dit commando kan uw huidige Windows licentie overschrijven, deactiveren en/of verwijderen. Ga met voorzichtigheid verder.
Meer informatie: <https://learn.microsoft.com/windows-server/get-started/activation-slmgr-vbs-options>.

- Toon de huidige Windows [l]icentie [i]nformatie:

`slmgr /dli`

- Toon de installatie [i]D voor het huidige apparaat. Nuttig voor offline licentie activatie:

`slmgr /dti`

- Toon de verloopdatum en -tijd van de huidige licentie:

`slmgr /xpr`

- [i]nstalleer een nieuwe Windows licentie [p]roduct sleutel. Vereist beheerdersrechten en zal de bestaande licentie overschrijven:

`slmgr /ipk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">product_sleutel</span>

- [a]c[t]iveer de Windows product licentie [o]nline. Vereist beheerdersrechten:

`slmgr /ato`

- [a]c[t]iveer de Windows [p]roduct licentie offline. Vereist beheerdersrechten een bevestigings ID verstrekt door Microsoft Product Activation Center:

`slmgr /atp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bevestigings_id</span>

- Wis de huidige licentie [p]roduct sleutel van het Windows register. Dit zal de huidige licentie niet deactiveren of verwijderen, maar voorkomt dat de sleutel in de toekomst wordt gestolen door kwaadaardige programma's:

`slmgr /cpky`

- Deinstalleer de huidigie licentie (door zijn [p]roduct sleutel):

`slmgr /upk`
