---
layout: page
title: windows/where-object (Nederlands)
description: "Selecteert objecten uit een verzameling op basis van hun eigenschapswaarden."
content_hash: 0975ec7f8268d766ace97934fb5a6a4ea17ecc8f
last_modified_at: 2023-11-24
related_topics:
  - title: English version
    url: /en/windows/where-object.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/where-object.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Where-Object

Selecteert objecten uit een verzameling op basis van hun eigenschapswaarden.
Dit commando kan alleen gebruikt worden via PowerShell.
Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/where-object>.

- Filter aliassen op naam:

`Get-Alias | Where-Object -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Property</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Name</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eq</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">naam</span>

- Toon een lijst van alle services die momenteel zijn gestopt. De `$_` automatische variable representeert ieder object dat word gestuurd naar de `Where-Object` cmdlet:

`Get-Service | Where-Object {$_.Status -eq "Stopped"}`

- Gebruik meerdere condities:

`Get-Module -ListAvailable | Where-Object { $_.Name -NotLike "Microsoft*" -And $_.Name -NotLike "PS*" }`
