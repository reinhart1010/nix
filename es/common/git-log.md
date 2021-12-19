---
layout: page
title: common/git-log (español)
description: "Muestra un historial de commits."
content_hash: c3e84b8a9020b578bb427aae60900e3c902e569b
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
  - title: 中文 version
    url: /zh/common/git-log.html
    icon: bi bi-globe
---
# git log

Muestra un historial de commits.
Más información: <https://git-scm.com/docs/git-log>.

- Muestra la secuencia de commits comenzando desde el actual, en orden cronológico inverso, del respositorio de Git en el directorio de trabajo actual:

`git log`

- Muestra el historial de un archivo o directorio específico, incluyendo las diferencias:

`git log -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio</span>

- Muestra un resumen de los archivos, o archivo, cambiados en cada commit:

`git log --stat`

- Muestra un gráfico de los commits en la rama actual, utilizando solo la primer línea del mensaje de cada uno:

`git log --oneline --graph`

- Muestra un gráfico de todos los commits, etiquetas y ramas en todo el repositorio:

`git log --oneline --decorate --all --graph`

- Muestra solo los commits cuyo mensaje incluye una cadena dada (no diferencia entre mayúsculas y minúsculas):

`git log -i --grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena_a_buscar</span>

- Muestra los últimos N commits de cierto autor:

`git log -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero</span>` --author=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">autor</span>

- Muestra los commits entre dos fechas (yyyy-mm-dd):

`git log --before="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2017-01-29</span>`" --after="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2017-01-17</span>`"`
