---
layout: page
title: linux/alien (español)
description: "Convierte diferentes paquetes de instalación a otros formatos."
content_hash: ca70bbbbea49799d5be7d98b93a4012369d39975
last_modified_at: 2025-03-02
related_topics:
  - title: বাংলা version
    url: /bn/linux/alien.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/alien.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/alien.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/alien.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/alien.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/alien.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/alien.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/alien.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/alien.html
    icon: bi bi-globe
tldri18n_status: 2
---
# alien

Convierte diferentes paquetes de instalación a otros formatos.
Vea también: `debtap`, para la conversión de `.deb` en Arch Linux.
Más información: <https://manned.org/alien>.

- Convierte un archivo de instalación específico al formato Debian (extensión `.deb`):

`sudo alien --to-deb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Convierte un archivo de instalación específico al formato Red Hat (extensión `.rpm`):

`sudo alien --to-rpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Convierte un archivo de instalación específico al formato de instalación de Slackware (extensión `.tgz`):

`sudo alien --to-tgz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Convierte un archivo de instalación específico al formato Debian y lo instala en el sistema:

`sudo alien --to-deb --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
