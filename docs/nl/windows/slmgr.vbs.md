---
layout: page
title: windows/slmgr.vbs (Nederlands)
description: "Installeer, activeer en beheer Windows licenties."
content_hash: dfce3188ed10248e8217741d9ae57b480840c73a
last_modified_at: 2023-12-04
related_topics:
  - title: English version
    url: /en/windows/slmgr.vbs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# slmgr.vbs

Installeer, activeer en beheer Windows licenties.
Dit commando kan uw huidige Windows licentie overschrijven, deactiveren en/of verwijderen. Ga met voorzichtigheid verder.
Meer informatie: <https://learn.microsoft.com/windows-server/get-started/activation-slmgr-vbs-options>.

- Toon de huidige Windows [l]icentie [i]nformatie:

`slmgr.vbs /dli`

- Toon de installatie [i]D voor het huidige apparaat. Nuttig voor offline licentie activatie:

`slmgr.vbs /dti`

- Toon de verloopdatum en -tijd van de huidige licentie:

`slmgr.vbs /xpr`

- [i]nstalleer een nieuwe Windows licentie [p]roduct sleutel. Vereist beheerdersrechten en zal de bestaande licentie overschrijven:

`slmgr.vbs /ipk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">product_sleutel</span>

- [a]c[t]iveer de Windows product licentie [o]nline. Vereist beheerdersrechten:

`slmgr.vbs /ato`

- [a]c[t]iveer de Windows [p]roduct licentie offline. Vereist beheerdersrechten een bevestigings ID verstrekt door Microsoft Product Activation Center:

`slmgr.vbs /atp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bevestigings_id</span>

- Wis de huidige licentie [p]roduct sleutel van het Windows register. Dit zal de huidige licentie niet deactiveren of verwijderen, maar voorkomt dat de sleutel in de toekomst wordt gestolen door kwaadaardige programma's:

`slmgr.vbs /cpky`

- Deinstalleer de huidigie licentie (door zijn [p]roduct sleutel):

`slmgr.vbs /upk`
