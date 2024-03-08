---
layout: page
title: common/traefik (Deutsch)
description: "Ein HTTP-Reverse-Proxy und Load-Balancer."
content_hash: 3273a04ddfbfe7d48b18a0f1989ea263e8cb5399
last_modified_at: 2024-03-08
related_topics:
  - title: English version
    url: /en/common/traefik.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/traefik.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># traefik

Ein HTTP-Reverse-Proxy und Load-Balancer.
Weitere Informationen: <https://traefik.io>.

- Starte den Server mit der Standardkonfiguration:

`traefik`

- Starte den Server mit einer benutzerdefinierten Konfigurationsdatei:

`traefik --ConfigFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konfigurationsdatei.toml</span>

- Starte den Server mit aktiviertem Cluster-Modus:

`traefik --cluster`

- Starte den Server mit dem Web-UI:

`traefik --web`
