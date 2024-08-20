---
layout: page
title: common/netstat (Nederlands)
description: "Toon netwerkgerelateerde informatie zoals open verbindingen, open socketpoorten, enz."
content_hash: 1c852e91dcd1d8704d15177795186fbc65c6b272
last_modified_at: 2024-08-20
related_topics:
  - title: English version
    url: /en/common/netstat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/netstat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/netstat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/netstat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># netstat

Toon netwerkgerelateerde informatie zoals open verbindingen, open socketpoorten, enz.
Meer informatie: <https://manned.org/netstat>.

- Lijst alle poorten:

`netstat --all`

- Lijst alle luisterende poorten:

`netstat --listening`

- Lijst luisterende TCP-poorten:

`netstat --tcp`

- Toon PID en programmanamen:

`netstat --program`

- Lijst informatie continu:

`netstat --continuous`

- Lijst routes en los IP-adressen niet op naar hostnamen:

`netstat --route --numeric`

- Lijst luisterende TCP- en UDP-poorten (+ gebruiker en proces als je root bent):

`netstat --listening --program --numeric --tcp --udp --extend`
