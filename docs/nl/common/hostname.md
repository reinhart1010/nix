---
layout: page
title: common/hostname (Nederlands)
description: "Toon of stel de hostnaam van het systeem in."
content_hash: abfc3e2785e6294a5e1d3ba73f3caeb5b869d76a
last_modified_at: 2024-06-18
related_topics:
  - title: English version
    url: /en/common/hostname.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/hostname.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/hostname.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hostname.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hostname

Toon of stel de hostnaam van het systeem in.
Meer informatie: <https://manned.org/hostname>.

- Toon de huidige hostnaam:

`hostname`

- Toon het netwerkadres van de hostnaam:

`hostname -i`

- Toon alle netwerkadressen van de host:

`hostname -I`

- Toon de FQDN (Fully Qualified Domain Name):

`hostname --fqdn`

- Stel een nieuwe hostnaam in:

`hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nieuwe_hostnaam</span>
