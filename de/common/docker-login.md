---
layout: page
title: common/docker-login (Deutsch)
description: "Bei einer Docker Registry einloggen."
content_hash: 88d8e8463791c73cabdd687ace6a74f3f418ba36
related_topics:
  - title: English version
    url: /en/common/docker-login.html
    icon: bi bi-globe
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

- Einloggen mit einem Passwort, welches von stdin gelesen wird:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">passwort</span>`" | docker login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>` --password-stdin`
