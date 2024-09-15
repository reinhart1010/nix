---
layout: page
title: common/docker-rmi (Deutsch)
description: "Lösche eines oder mehrere Docker Images."
content_hash: 1671a884e7d2d8c8e751d07fdb032dbb3a7d1478
last_modified_at: 2024-09-15
related_topics:
  - title: English version
    url: /en/common/docker-rmi.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-rmi.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-rmi.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-rmi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker rmi

Lösche eines oder mehrere Docker Images.
Weitere Informationen: <https://docs.docker.com/reference/cli/docker/image/rm/>.

- Zeige Hilfe:

`docker rmi`

- Lösche eines oder mehrere Docker Images anhand der angegebenen Namen:

`docker rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image1 image2 ...</span>

- Erzwinge das Löschen eines Images:

`docker rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Lösche ein Image aber behalte Eltern-Images ohne Tag:

`docker rmi --no-prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>
