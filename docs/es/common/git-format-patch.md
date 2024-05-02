---
layout: page
title: common/git-format-patch (español)
description: "Prepara archivos .patch. Es útil cuando se envían commits por correo electrónico."
content_hash: 7ab5aac17cc8a77d0d7de420f1dd36d8be722ad8
last_modified_at: 2024-05-02
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
tldri18n_status: 2
---
# git format-patch

Prepara archivos .patch. Es útil cuando se envían commits por correo electrónico.
Vea también `git-am`, comando que puede aplicar los archivos .patch generados.
Más información: <https://git-scm.com/docs/git-format-patch>.

- Crea un archivo `.patch` con nombre automático para todos los cambios que no están en el push:

`git format-patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origen</span>

- Escribe un archivo `.patch` para todos los commits entre dos revisiones a `stdout`:

`git format-patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revisión_1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revisión_2</span>

- Escribe un archivo `.patch` para los 3 últimos commits:

`git format-patch -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>
