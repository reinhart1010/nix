---
layout: page
title: windows/nvm (Nederlands)
description: "Installeer, deïnstalleer of wissel tussen verschillende Node.js-versies."
content_hash: eebe95aeeb7a4fa95a32b08c26102258fbaad25d
last_modified_at: 2024-08-20
related_topics:
  - title: English version
    url: /en/windows/nvm.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/nvm.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/nvm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/nvm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/nvm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nvm

Installeer, deïnstalleer of wissel tussen verschillende Node.js-versies.
Ondersteunt versienummers zoals "12.8" of "v16.13.1", en labels zoals "stable", "system", enz.
Meer informatie: <https://github.com/coreybutler/nvm-windows>.

- Installeer een specifieke versie van Node.js:

`nvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_versie</span>

- Stel de standaardversie van Node.js in (moet worden uitgevoerd als Administrator):

`nvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_versie</span>

- Toon alle beschikbare Node.js-versies en markeer de standaardversie:

`nvm list`

- Toon alle remote Node.js-versies:

`nvm ls-remote`

- Deïnstalleer een bepaalde versie van Node.js:

`nvm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_versie</span>
