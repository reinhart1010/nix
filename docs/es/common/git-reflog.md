---
layout: page
title: common/git-reflog (español)
description: "Muestra un registro de cambios de las referencias (*reflog*) locales como HEAD, ramas o etiquetas."
content_hash: b99e6ed31315b375cbfbeec805e17c03feae3ca1
last_modified_at: 2024-09-27
related_topics:
  - title: English version
    url: /en/common/git-reflog.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-reflog.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-reflog.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-reflog.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-reflog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git reflog

Muestra un registro de cambios de las referencias (*reflog*) locales como HEAD, ramas o etiquetas.
Más información: <https://git-scm.com/docs/git-reflog>.

- Muestra un registro de referencias para HEAD:

`git reflog`

- Muestra el registro de referencias para una rama:

`git reflog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Muestra solo las últimas 5 entradas en el registro de referencias:

`git reflog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--max-count</span>` 5`
