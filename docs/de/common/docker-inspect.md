---
layout: page
title: common/docker-inspect (Deutsch)
description: "Erhalte tiefgehende Informationen zu Docker Objekten."
content_hash: 1c52ad0360789e4785f2f0f6a497ff550ef738cd
related_topics:
  - title: English version
    url: /en/common/docker-inspect.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-inspect.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-inspect.html
    icon: bi bi-globe
---
# docker inspect

Erhalte tiefgehende Informationen zu Docker Objekten.
Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/inspect/>.

- Zeige Hilfeseite:

`docker inspect`

- Zeige Informationen über einen Container, ein Image oder Volume anhand des Namens oder der ID:

`docker inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container|image|ID</span>

- Zeige die IP Adresse eines Containers an:

`docker inspect --format='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">range .NetworkSettings.Networks</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.IPAddress</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Zeige den Pfad zur Logdatei eines Containers:

`docker inspect --format='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.LogPath</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Zeige den Namen des Images eines Containers:

`docker inspect --format='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Config.Image</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Zeige die Konfiguration als JSON an:

`docker inspect --format='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json .Config</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Zeige alle Port Bindings:

`docker inspect --format='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">range $p, $conf := .NetworkSettings.Ports</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$p</span>` -> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(index $conf 0).HostPort</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>
