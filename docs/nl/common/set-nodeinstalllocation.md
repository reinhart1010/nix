---
layout: page
title: common/set-nodeinstalllocation (Nederlands)
description: "Stel de standaard Node.js installatie map in voor `ps-nvm`."
content_hash: 9d361b7e6e49070eaac091da9665c0dea96f33bf
last_modified_at: 2023-12-21
related_topics:
  - title: English version
    url: /en/common/set-nodeinstalllocation.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/set-nodeinstalllocation.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Set-NodeInstallLocation

Stel de standaard Node.js installatie map in voor `ps-nvm`.
Onderdeel van `ps-nvm` en kan alleen uitgevoerd worden in PowerShell.
Meer informatie: <https://github.com/aaronpowell/ps-nvm>.

- Verander de Node.js installatie locatie naar een gespecificeerde map (`ps-nvm` zal een nieuwe `.nvm` submap maken om deze te kunnen installeren):

`Set-NodeInstallLocation `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>
