---
layout: page
title: windows/move-item (Nederlands)
description: "Verplaats of hernoem bestanden, mappen, registersleutels en andere PowerShell data items."
content_hash: 30311842eb8bdc73238e336c42089c6113c10c03
last_modified_at: 2023-11-25
related_topics:
  - title: English version
    url: /en/windows/move-item.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/move-item.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

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
