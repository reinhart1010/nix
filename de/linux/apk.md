---
layout: page
title: linux/apk (Deutsch)
description: "Alpine Linux-Paketverwaltungstool."
content_hash: c1f0219bc84623d116d53989a16d99103a0b21a9
related_topics:
  - title: English version
    url: /en/linux/apk.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apk.html
    icon: bi bi-globe
---
# apk

Alpine Linux-Paketverwaltungstool.
Weitere Informationen: <https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management>.

- Aktualisiere die Indizes von allen externen Repositories:

`apk update`

- Installiere ein neues Paket:

`apk add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Entferne ein Paket:

`apk del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Repariere oder aktualisiere ein Paket, ohne die Hauptabhängigkeiten zu ändern:

`apk fix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Suche Pakete mit einem Schlüsselwort:

`apk search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">schlüsselwort</span>

- Erhalte Informationen über ein bestimmtes Paket:

`apk info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>
