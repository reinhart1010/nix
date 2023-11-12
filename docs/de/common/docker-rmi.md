---
layout: page
title: common/docker-rmi (Deutsch)
description: "Lösche eines oder mehrere Docker Images."
content_hash: 10ce7f1f08f53380f21be377b96c37f757db8803
last_modified_at: 2023-11-12
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
Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/rmi/>.

- Zeige Hilfe:

`docker rmi`

- Lösche eines oder mehrere Docker Images anhand der angegebenen Namen:

`docker rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image1 image2 ...</span>

- Erzwinge das Löschen eines Images:

`docker rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>

- Lösche ein Image aber behalte Eltern-Images ohne Tag:

`docker rmi --no-prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>
