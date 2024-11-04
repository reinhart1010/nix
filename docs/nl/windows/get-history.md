---
layout: page
title: windows/get-history (Nederlands)
description: "Toon de PowerShell commando-geschiedenis."
content_hash: 5e768bcee79de6db31f77adafff7d6593bce7693
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/windows/get-history.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/get-history.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/get-history.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Get-History

Toon de PowerShell commando-geschiedenis.
Let op: dit commando kan alleen gebruikt worden via PowerShell.
Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/get-history>.

- Toon de commando-geschiedenis met ID:

`Get-History`

- Haal het PowerShell geschiedenis-item op via een ID:

`Get-History -Id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Toon de laatste N commando's:

`Get-History -Count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>
