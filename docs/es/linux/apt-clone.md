---
layout: page
title: linux/apt-clone (español)
description: "Clona/hace copia de seguridad/restaura el estado de un paquete de un sistema basado en Debian."
content_hash: d7271558ea268dfa6fa4c7dd2b6aacb13c61001e
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/linux/apt-clone.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/apt-clone.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-clone

Clona/hace copia de seguridad/restaura el estado de un paquete de un sistema basado en Debian.
Más información: <https://github.com/mvo5/apt-clone>.

- Clona el estado del paquete del sistema actual en un directorio especificado:

`apt-clone clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Crea un archivo clon (`tar.gz`) con fines de copia de seguridad:

`apt-clone clone --destination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/backup.tar.gz</span>

- Restaura el estado del paquete desde un archivo clon:

`apt-clone restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/backup.tar.gz</span>

- Muestra información sobre un archivo clon (por ejemplo, la versión, la arquitectura):

`apt-clone info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/backup.tar.gz</span>

- Comprueba si el archivo clon se puede restaurar en el sistema actual:

`apt-clone restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/backup.tar.gz</span>` --destination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/restaurar</span>
