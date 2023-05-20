---
layout: page
title: common/docker-start (Deutsch)
description: "Starte einen oder mehrere gestoppte Container."
content_hash: cd58431a1660663f89583d7311ebb98956ef9f88
last_modified_at: 2023-05-20
related_topics:
  - title: English version
    url: /en/common/docker-start.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-start.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-start.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-start.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-start.html
    icon: bi bi-globe
---
# docker start

Starte einen oder mehrere gestoppte Container.
Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/start/>.

- Zeige Hilfe:

`docker start`

- Starte einen Docker Container:

`docker start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Starte einen Container und verbinde dich mit der Standardausgabe sowie der Standardfehlerausgabe und leite Signale weiter:

`docker start --attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Starte einen oder mehrere durch Leerzeichen getrennte Container:

`docker start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container1 container2 ...</span>
