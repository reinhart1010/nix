---
layout: page
title: windows/move-item (Nederlands)
description: "Verplaats of hernoem bestanden, mappen, registersleutels en andere PowerShell data items."
content_hash: 30311842eb8bdc73238e336c42089c6113c10c03
last_modified_at: 2023-11-07
related_topics:
  - title: English version
    url: /en/windows/move-item.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># Move-Item

Verplaats of hernoem bestanden, mappen, registersleutels en andere PowerShell data items.
Dit commando kan alleen worden uitgevoerd onder PowerShell.
Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/move-item>.

- Hernoem een bestand of map wanneer het doelwit geen bestaande map is:

`Move-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bron</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\doel</span>

- Verplaats een bestand of map naar een bestaande map:

`Move-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bron</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestaande_map</span>

- Hernoem of verplaats bestand(en) met een specifieke naam (behandel geen speciale karakters in strings):

`Move-Item -LiteralPath "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bron</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand_of_map</span>

- Verplaats meerdere bestanden naar een bestaande map, waardoor de bestandsnamen ongewijzigd blijven:

`Move-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bron1 , pad\naar\bron2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestaande_map</span>

- Verplaats of hernoem registersleutel(s):

`Move-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bron_sleutel1 , pad\naar\bron_sleutel2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\nieuwe_of_bestaande_sleutel</span>

- Vraag niet om bevestiging voordat bestaande bestanden of registersleutels worden overschreven:

`mv -Force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bron</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\doel</span>

- Vraag om bevestiging voordat bestaande bestanden worden overschreven, ongeacht bestandsrechten:

`mv -Confirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bron</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\doel</span>

- Verplaats bestanden in de dry-run-modus en toon bestanden en mappen die kunnen worden verplaatst zonder ze uit te voeren:

`mv -WhatIf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bron</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\doel</span>
