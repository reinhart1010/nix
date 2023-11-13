---
layout: page
title: common/powershell (Nederlands)
description: "Command-line shell en scripting taal specifiek ontworpen voor systeemadministratie."
content_hash: 6cdb673d6a2036a8346844b385e6baf3d12c2590
last_modified_at: 2023-11-13
related_topics:
  - title: English version
    url: /en/common/powershell.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/powershell.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/powershell.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/powershell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/powershell.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/powershell.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># powershell

Command-line shell en scripting taal specifiek ontworpen voor systeemadministratie.
Zie ook: `pwsh`.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/powershell>.

- Start een interactieve shell sessie:

`powershell`

- Start een interactieve shell sessie zonder het laden van startup configuraties:

`powershell -NoProfile`

- Voer specifieke commando's uit:

`powershell -Command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'powershell is uitgevoerd'</span>`"`

- Voer een specifiek script uit:

`powershell -File `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/script.ps1</span>

- Start een sessie met een specifieke versie van PowerShell:

`powershell -Version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versie</span>

- Voorkom dat een shell uitgaat na het uitvoeren van startup commando's:

`powershell -NoExit`

- Beschrijf het formaat van gegevens die naar PowerShell zijn verzonden:

`powershell -InputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>

- Bepaal hoe een output van PowerShell wordt opgemaakt:

`powershell -OutputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>
