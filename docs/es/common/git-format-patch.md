---
layout: page
title: common/git-format-patch (español)
description: "Prepara archivos .patch. Es útil cuando se envían commits por correo electrónico."
content_hash: e5135ba0a4f7cb1f199fbfb107ceeb765a48a417
last_modified_at: 2023-07-03
related_topics:
  - title: English version
    url: /en/common/git-format-patch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-format-patch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-format-patch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-format-patch.html
    icon: bi bi-globe
---
# git format-patch

Prepara archivos .patch. Es útil cuando se envían commits por correo electrónico.
Véase también `git-am`, comando que puede aplicar los archivos .patch generados.
Más información: <https://git-scm.com/docs/git-format-patch>.

- Crea un archivo `.patch` con nombre automático para todos los cambios que no están en el push:

`git format-patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origen</span>

- Escribe un archivo `.patch` para todos los commits entre dos revisiones a `stdout`:

`git format-patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revisión_1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revisión_2</span>

- Escribe un archivo `.patch` para los 3 últimos commits:

`git format-patch -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>
