---
layout: page
title: common/remove-nodeversion (Nederlands)
description: "Deïnstalleer Node.js runtime versies voor `ps-nvm`."
content_hash: 72127c30a7f425e9ca226141c9f0cda4fc924e45
last_modified_at: 2023-12-21
related_topics:
  - title: English version
    url: /en/common/remove-nodeversion.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/remove-nodeversion.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Remove-NodeVersion

Deïnstalleer Node.js runtime versies voor `ps-nvm`.
Onderdeel van `ps-nvm` en kan alleen uitgevoerd worden in PowerShell.
Meer informatie: <https://github.com/aaronpowell/ps-nvm>.

- Deïnstalleer een gegeven Node.js versie:

`Remove-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_versie</span>

- Deïnstalleer meerdere Node.js versies:

`Remove-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_versie1 , node_versie2 , ...</span>

- Deïnstalleer alle huidige geïnstalleerde versie van Node.js 20.x:

`Get-NodeVersions -Filter ">=20.0.0 <21.0.0" | Remove-NodeVersion`

- Deïnstalleer alle huidige geïnstalleerde versies van Node.js:

`Get-NodeVersions | Remove-NodeVersion`
