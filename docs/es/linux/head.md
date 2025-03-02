---
layout: page
title: linux/head (español)
description: "Muestra la primera parte de los archivos."
content_hash: 16fdcae3c9fd402ca70e9cdc1d8650de1f092162
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/head.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/head.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/head.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/head.html
    icon: bi bi-globe
tldri18n_status: 2
---
# head

Muestra la primera parte de los archivos.
Más información: <https://www.gnu.org/software/coreutils/manual/html_node/head-invocation.html>.

- Muestra las primeras líneas de un archivo:

`head --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cuenta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra los primeros bits de un archivo:

`head --bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cuenta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra todo el contenido de un archivo excepto las últimas líneas:

`head --lines -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cuenta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra todo el contenido de un archivo excepto los últimos bits:

`head --bytes -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cuenta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
