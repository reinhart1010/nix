---
layout: page
title: linux/dpkg (español)
description: "Administrador de paquetes de Debian."
content_hash: 1beb0209653d6437bb7b681b73d267ebb297a361
last_modified_at: 2024-12-27
related_topics:
  - title: Deutsch version
    url: /de/linux/dpkg.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dpkg.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/dpkg.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/dpkg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/dpkg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/dpkg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dpkg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dpkg

Administrador de paquetes de Debian.
Algunos subcomandos como `deb` tienen su propia documentación de uso.
Para comandos equivalentes en otros gestores de paquetes, vea <https://wiki.archlinux.org/title/Pacman/Rosetta>.
Más información: <https://manned.org/dpkg>.

- Instala un paquete:

`dpkg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.deb</span>

- Remueve un paquete:

`dpkg -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Lista los paquetes instalados:

`dpkg -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón</span>

- Lista los contenidos de un paquete:

`dpkg -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Lista los contenidos de un archivo de paquete local:

`dpkg -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.deb</span>

- Averigua qué paquete posee un archivo:

`dpkg -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Purga un paquete instalado o ya eliminado, incluyendo su configuración:

`dpkg -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>
