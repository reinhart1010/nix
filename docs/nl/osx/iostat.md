---
layout: page
title: osx/iostat (Nederlands)
description: "Geeft statistieken weer voor apparaten."
content_hash: 468bf0a5b6611c1ebc398da5a077e614ea2927d1
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/osx/iostat.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/iostat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iostat

Geeft statistieken weer voor apparaten.
Meer informatie: <https://ss64.com/mac/iostat.html>.

- Toon snapshot-apparaatstatistieken (KB/t, transfers per seconde, MB per seconde), CPU-statistieken (percentages van de tijd besteed in gebruikersmodus, systeemmodus en inactieve modus), en systeembelastinggemiddelden (voor de afgelopen 1, 5 en 15 minuten):

`iostat`

- Toon alleen apparaatstatistieken:

`iostat -d`

- Toon incrementele rapporten van CPU- en schijfstatistieken elke 2 seconden:

`iostat 2`

- Toon statistieken voor de eerste schijf elke seconde, oneindig:

`iostat -w 1 disk0`

- Toon statistieken voor de tweede schijf elke 3 seconden, 10 keer:

`iostat -w 3 -c 10 disk1`

- Toon met de oude `iostat` weergave. Laat sectoren per seconde zien, overdrachten per seconde, gemiddelde milliseconden per transactie, en CPU-statistieken + belastinggemiddelden uit de standaardweergave:

`iostat -o`

- Toon totale apparaatstatistieken (KB/t: kilobytes per overdracht zoals voorheen, xfrs: totaal aantal overdrachten, MB: totaal aantal overgedragen megabytes):

`iostat -I`
