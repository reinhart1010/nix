---
layout: page
title: common/traefik (Deutsch)
description: "Ein HTTP-Reverse-Proxy und Load-Balancer."
content_hash: 3273a04ddfbfe7d48b18a0f1989ea263e8cb5399
last_modified_at: 2024-03-09
related_topics:
  - title: English version
    url: /en/common/traefik.html
    icon: bi bi-globe
tldri18n_status: 2
---
# traefik

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
