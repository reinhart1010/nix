---
layout: page
title: windows/set-location (Nederlands)
description: "Geef de huidige werkmap weer of ga naar een andere map."
content_hash: c65effc6f40719d1841f2bf6f9f86f1b4432e5d0
last_modified_at: 2023-10-26
related_topics:
  - title: English version
    url: /en/windows/set-location.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># Set-Location

Geef de huidige werkmap weer of ga naar een andere map.
Deze opdracht kan alleen worden gebruikt via PowerShell.
Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-location>.

- Ga naar de opgegeven map:

`Set-Location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\map</span>

- Ga naar een map in een andere drive:

`Set-Location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\map</span>

- Ga en toon de locatie van de opgegeven map:

`Set-Location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\map</span>` -PassThru`

- Ga naar de bovenliggende map van de huidige map:

`Set-Location ..`

- Ga naar de thuismap van de huidige gebruiker:

`Set-Location ~`

- Ga terug/vooruit naar de eerder gekozen map:

`Set-Location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-|+</span>

- Ga naar de hoofdmap van de huidige drive:

`Set-Location \`
