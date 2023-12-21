---
layout: page
title: common/set-nodeversion (Nederlands)
description: "Stel de standaard Node.js versie in voor `ps-nvm`."
content_hash: 5cd7cfb9203e0f9240af0c0b62e6e1b4ca5d2aab
last_modified_at: 2023-12-21
related_topics:
  - title: English version
    url: /en/common/set-nodeversion.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/set-nodeversion.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Set-NodeVersion

Stel de standaard Node.js versie in voor `ps-nvm`.
Onderdeel van `ps-nvm` en kan alleen uitgevoerd worden in PowerShell.
Meer informatie: <https://github.com/aaronpowell/ps-nvm>.

- Gebruik een specifieke versie van Node.js in de huidige PowerShell sessie:

`Set-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versie</span>

- Gebruik de laatst geïnstalleerde Node.js versie van 20.x:

`Set-NodeVersion ^20`

- Stel de standaard Node.js versie in voor de huidige gebruiker (geldt alleen voor toekomstige PowerShell sessies):

`Set-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versie</span>` -Persist User`

- Stel de standaard Node.js versie in voor alle gebruikers (dient uitgevoerd te worden als Administrator/root en geldt alleen voor toekomstige PowerShell sessies):

`Set-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versie</span>` -Persist Machine`
