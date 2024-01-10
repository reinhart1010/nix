---
layout: page
title: common/git-shortlog (español)
description: "Resume la salida de `git log`."
content_hash: 6bdb2ffbbfec38d883a607ad967b602f71a6bb21
last_modified_at: 2024-01-10
related_topics:
  - title: English version
    url: /en/common/git-shortlog.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-shortlog.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-shortlog.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-shortlog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git shortlog

Resume la salida de `git log`.
Más información: <https://git-scm.com/docs/git-shortlog>.

- Muestra un resumen de todas las confirmaciones realizadas, agrupadas alfabéticamente por autor:

`git shortlog`

- Muestra un resumen de todas las confirmaciones realizadas, agrupadas por el número de confirmaciones realizadas:

`git shortlog -n`

- Muestra un resumen de todas las confirmaciones realizadas, agrupadas por la identidad de quien realiza la confirmación (usuario y correo electrónico):

`git shortlog -c`

- Muestra un resumen de las últimas cinco confirmaciones (i. e., un rango de revisiones específico):

`git shortlog HEAD~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>`..HEAD`

- Muestra todos los usuarios, correos electrónicos y número de confirmaciones en la rama actual:

`git shortlog -sne`

- Muestra todos los usuarios, correos electrónicos y número de confirmaciones en todas las ramas:

`git shortlog -sne --all`
