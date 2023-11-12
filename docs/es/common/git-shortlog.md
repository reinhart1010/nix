---
layout: page
title: common/git-shortlog (español)
description: "Resume la salida de `git log`."
content_hash: 31ea74887f4b0e4c8a8c396bc9f83894e80f69bf
last_modified_at: 2023-11-12
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

- Muestra un resumen de todos los commits realizados, agrupados alfabéticamente por autor:

`git shortlog`

- Muestra un resumen de todos los commits realizados, agrupados por el número de commits realizados:

`git shortlog -n`

- Muestra un resumen de todos los commits realizados, agrupados por la identidad de quien realiza el commit (usuario y correo electrónico):

`git shortlog -c`

- Muestra un resumen de los últimos 5 commits (i. e., un rango de revisiones específico):

`git shortlog HEAD~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>`..HEAD`

- Muestra todos los usuarios, correos electrónicos y número de commits en la rama actual:

`git shortlog -sne`

- Muestra todos los usuarios, correos electrónicos y número de commits en todas las ramas:

`git shortlog -sne --all`
