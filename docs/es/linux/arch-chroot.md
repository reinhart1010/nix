---
layout: page
title: linux/arch-chroot (español)
description: "Comando `chroot` mejorado para facilitar el proceso de instalación de Arch Linux."
content_hash: ca6d49dff1a130ca645673600931e78df5fa5f97
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/linux/arch-chroot.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/arch-chroot.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/arch-chroot.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/arch-chroot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arch-chroot

Comando `chroot` mejorado para facilitar el proceso de instalación de Arch Linux.
Más información: <https://manned.org/arch-chroot.8>.

- Inicia un intérprete de comandos interactivo (Bash por defecto) en un nuevo directorio raíz:

`arch-chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/nueva/raíz</span>

- Especifica el usuario (distinto del actual) para ejecutar el intérprete de comandos:

`arch-chroot -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/nueva/raíz</span>

- Ejecuta un comando personalizado (en lugar de Bash) en el nuevo directorio raíz:

`arch-chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/nueva/raíz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumentos_del_comando</span>

- Especifica un intérprete de comandos distinto de Bash (en este caso, el paquete `zsh` debe estar instalado en el sistema de destino):

`arch-chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/nueva/raíz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zsh</span>
