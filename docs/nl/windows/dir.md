---
layout: page
title: windows/dir (Nederlands)
description: "Geeft de inhoud weer van een map."
content_hash: 7b4c8c2ec76d888d27bfc210ea598fadebf077ae
last_modified_at: 2023-10-17
related_topics:
  - title: català version
    url: /ca/windows/dir.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/windows/dir.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/dir.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/dir.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/dir.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/dir.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/dir.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/dir.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/dir.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/dir.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/dir.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dir

Geeft de inhoud weer van een map.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/dir>.

- Geef de inhoud weer van de huidige map:

`dir`

- Geef de inhoud weer van een gegeven map:

`dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\directory</span>

- Geef de inhoud weer van de huidige map, inclusief verborgen bestanden:

`dir /a`

- Geef de inhoud weer van een gegeven map, inclusief verborgen bestanden:

`dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\directory</span>` /A`

- Toon een lijst met mappen en bestanden, zonder extra informatie:

`dir /b`
