---
layout: page
title: common/git-log (español)
description: "Muestra un historial de confirmaciones."
content_hash: 12fb3a5ab5f237cac120af274df8881584d1b51f
last_modified_at: 2024-10-13
related_topics:
  - title: Deutsch version
    url: /de/common/git-log.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-log.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-log.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-log.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-log.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-log.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-log.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-log.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git log

Muestra un historial de confirmaciones.
Más información: <https://git-scm.com/docs/git-log>.

- Muestra la secuencia de confirmaciones comenzando desde el actual, en orden cronológico inverso, del respositorio de Git en el directorio de trabajo actual:

`git log`

- Muestra el historial de un archivo o directorio específico, incluyendo las diferencias:

`git log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-p|-u|--patch</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio</span>

- Muestra un resumen de los archivos, o archivo, cambiados en cada confirmación:

`git log --stat`

- Muestra un gráfico de las confirmaciones en la rama actual, utilizando solo la primer línea del mensaje de cada uno:

`git log --oneline --graph`

- Muestra un gráfico de todos las confirmaciones, etiquetas y ramas en todo el repositorio:

`git log --oneline --decorate --all --graph`

- Muestra solo las confirmaciones cuyo mensaje incluye una cadena dada (no diferencia entre mayúsculas y minúsculas):

`git log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--regexp-ignore-case</span>` --grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena_a_buscar</span>

- Muestra las últimas N confirmaciones de determinado autor:

`git log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--max-count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número</span>` --author "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">autor</span>`"`

- Muestra las confirmaciones entre dos fechas (yyyy-mm-dd):

`git log --before "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2017-01-29</span>`" --after "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2017-01-17</span>`"`
