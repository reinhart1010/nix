---
layout: page
title: common/passwd (français)
description: "Passwd est un outil de changement de mot de passe utilisateur."
content_hash: f3d3a0fd7c4d1dc7503f3edd098a262c1d4082c7
related_topics:
  - title: English version
    url: /en/common/passwd.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># passwd

Passwd est un outil de changement de mot de passe utilisateur.
Plus d'informations : <https://manned.org/passwd>.

- Change le mot de passe de l'utilisateur actuel :

`passwd`

- Change le mot de passe d'un utilisateur particulier :

`passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>

- Affiche l'état actuel du compte utilisateur :

`passwd -S`

- Supprime le mot de passe de l'utilisateur (supprime l'authentification par mot de passe pour l'utilisateur indiqué) :

`passwd -d`
