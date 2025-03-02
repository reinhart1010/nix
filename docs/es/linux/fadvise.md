---
layout: page
title: linux/fadvise (español)
description: "Controla el comportamiento de la caché de archivos de Linux."
content_hash: 587b6b35928900360deba8683d5bc6cf54c6f2dc
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/fadvise.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fadvise

Controla el comportamiento de la caché de archivos de Linux.
Más información: <https://manned.org/fadvise>.

- Precarga un archivo en la caché:

`fadvise `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--advice</span>` willneed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Sugiere eliminar un archivo de la caché:

`fadvise `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra la ayuda:

`fadvise --help`
