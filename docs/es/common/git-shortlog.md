---
layout: page
title: common/git-shortlog (español)
description: "Resume la salida de `git log`."
content_hash: cc280489b184e8fff5693ea75c821739f0ad8dce
last_modified_at: 2024-10-13
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
  - title: 한국어 version
    url: /ko/common/git-shortlog.html
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

`git shortlog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--numbered</span>

- Muestra un resumen de todas las confirmaciones realizadas, agrupadas por la identidad de quien realiza la confirmación (usuario y correo electrónico):

`git shortlog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--committer</span>

- Muestra un resumen de las últimas cinco confirmaciones (i. e., un rango de revisiones específico):

`git shortlog HEAD~5..HEAD`

- Muestra todos los usuarios, correos electrónicos y número de confirmaciones en la rama actual:

`git shortlog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--summary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--numbered</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--email</span>

- Muestra todos los usuarios, correos electrónicos y número de confirmaciones en todas las ramas:

`git shortlog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--summary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--numbered</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--email</span>` --all`
