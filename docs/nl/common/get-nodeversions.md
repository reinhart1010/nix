---
layout: page
title: common/get-nodeversions (Nederlands)
description: "Toon geïnstalleerde en beschikbare Node.js versies voor `ps-nvm`."
content_hash: d3c73d36d34d8fbac86dbec274a28a693a2ee196
last_modified_at: 2023-12-14
related_topics:
  - title: English version
    url: /en/common/get-nodeversions.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/get-nodeversions.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Get-NodeVersions

Toon geïnstalleerde en beschikbare Node.js versies voor `ps-nvm`.
Onderdeel van `ps-nvm` en kan alleen uitgevoerd worden in PowerShell.
Meer informatie: <https://github.com/aaronpowell/ps-nvm>.

- Toon alle geïnstalleerde Node.js versies:

`Get-NodeVersions`

- Toon alle beschikbare Node.js versies:

`Get-NodeVersions -Remote`

- Toon alle beschikbare Node.js 20.x versies:

`Get-NodeVersions -Remote -Filter ">=20.0.0 <21.0.0"`
