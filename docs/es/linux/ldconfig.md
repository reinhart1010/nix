---
layout: page
title: linux/ldconfig (español)
description: "Configura enlaces simbólicos y caché para dependencias de biblioteca compartidas."
content_hash: 9d78628ec0bbda2ed880536bd78f6c325da306de
last_modified_at: 2024-12-21
related_topics:
  - title: Deutsch version
    url: /de/linux/ldconfig.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ldconfig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ldconfig

Configura enlaces simbólicos y caché para dependencias de biblioteca compartidas.
Más información: <https://manned.org/ldconfig>.

- Actualiza los enlaces simbólicos y reconstruye el caché (normalmente se ejecuta cuando se instala una nueva biblioteca):

`sudo ldconfig`

- Actualiza los enlaces simbólicos para un directorio dado:

`sudo ldconfig -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Imprime las bibliotecas en el caché y comprueba si una biblioteca dada está presente:

`ldconfig -p | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_biblioteca</span>
