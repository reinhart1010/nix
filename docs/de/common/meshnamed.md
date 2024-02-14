---
layout: page
title: common/meshnamed (Deutsch)
description: "Verteiltes Namensystem für IPv6 Mesh-Netzwerke."
content_hash: f37d6ba0d4a6f936886e5ae05b1c2ea796f6c258
last_modified_at: 2024-02-14
related_topics:
  - title: English version
    url: /en/common/meshnamed.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/meshnamed.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># meshnamed

Verteiltes Namensystem für IPv6 Mesh-Netzwerke.
Weitere Informationen: <https://github.com/zhoreeq/meshname/>.

- Starte einen lokalen meshname DNS-Server:

`meshnamed`

- Wandle eine IPv6-Adresse in einen meshname um:

`meshnamed -getname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200:6fc8:9220:f400:5cc2:305a:4ac6:967e</span>

- Wandle einen meshname in eine IPv6-Adresse um:

`meshnamed -getip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aiag7sesed2aaxgcgbnevruwpy</span>
