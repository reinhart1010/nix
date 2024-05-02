---
layout: page
title: common/git-switch (español)
description: "Alterna entre ramas Git. Requiere una versión 2.23+ de Git."
content_hash: 8f7b44aa27db8679f645645aa249c7212d07937d
last_modified_at: 2024-05-02
related_topics:
  - title: Deutsch version
    url: /de/common/git-switch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-switch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-switch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-switch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-switch.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-switch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git switch

Alterna entre ramas Git. Requiere una versión 2.23+ de Git.
Vea también `git checkout`.
Más información: <https://git-scm.com/docs/git-switch>.

- Cambia a una rama existente:

`git switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Crea una nueva rama y se cambia a esta:

`git switch --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Crea y cambia a una nueva rama basada en una confirmación específica:

`git switch --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmación</span>

- Cambia a la rama anterior:

`git switch -`

- Cambia a una rama y actualiza todos los submódulos para coincidir:

`git switch --recurse-submodules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Cambia a una rama y automáticamente fusiona la rama actual y cualquier cambio sin confirmación en ella:

`git switch --merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>
