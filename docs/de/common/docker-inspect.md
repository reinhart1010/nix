---
layout: page
title: common/docker-inspect (Deutsch)
description: "Erhalte tiefgehende Informationen zu Docker Objekten."
content_hash: d7040545d2ba3a0981dccca5ab1df65a058fea2b
last_modified_at: 2024-09-24
related_topics:
  - title: English version
    url: /en/common/docker-inspect.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-inspect.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-inspect.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-inspect.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-inspect.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker inspect

Erhalte tiefgehende Informationen zu Docker Objekten.
Weitere Informationen: <https://docs.docker.com/reference/cli/docker/inspect/>.

- Zeige Hilfeseite:

`docker inspect`

- Zeige Informationen über einen Container, ein Image oder Volume anhand des Namens oder der ID:

`docker inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container|image|ID</span>

- Zeige die IP Adresse eines Containers an:

`docker inspect --format '\{\{range.NetworkSettings.Networks\}\}\{\{.IPAddress\}\}\{\{end\}\}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Zeige den Pfad zur Logdatei eines Containers:

`docker inspect --format='\{\{.LogPath\}\}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Zeige den Namen des Images eines Containers:

`docker inspect --format='\{\{.Config.Image\}\}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Zeige die Konfiguration als JSON an:

`docker inspect --format='\{\{json .Config\}\}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Zeige alle Port Bindings:

`docker inspect --format='\{\{range $p, $conf := .NetworkSettings.Ports\}\} \{\{$p\}\} -> \{\{(index $conf 0).HostPort\}\} \{\{end\}\}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>
