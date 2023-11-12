---
layout: page
title: common/docker-login (Deutsch)
description: "Bei einer Docker Registry einloggen."
content_hash: 564a2066634748eb4d29969c4c1559c8c8c99ced
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/docker-login.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-login.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-login.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker login

Bei einer Docker Registry einloggen.
Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/login/>.

- Interaktives Einloggen bei einer Registry:

`docker login`

- Einloggen mit einem angegebenen Benutzernamen (fragt nach dem Passwort):

`docker login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>

- Einloggen mit einem angegebenen Benutzernamen und Passwort:

`docker login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">passwort</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>

- Einloggen mit einem Passwort, welches von `stdin` gelesen wird:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">passwort</span>`" | docker login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>` --password-stdin`
