---
layout: page
title: common/adscript (español)
description: "Compilador de archivos Adscript."
content_hash: 5fa947c8611a013396b6f941cc0e9ecdf764256b
last_modified_at: 2022-12-31
related_topics:
  - title: English version
    url: /en/common/adscript.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adscript.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adscript.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># adscript

Compilador de archivos Adscript.
Más información: <https://github.com/Amplus2/Adscript>.

- Compilar un archivo en un archivo objeto:

`adscript --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_entrada.adscript</span>

- Compilar y vincular un archivo a un ejecutable independiente:

`adscript --executable --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo_entrada.adscript</span>

- Compilar un archivo a LLVM IR en lugar de código de máquina nativo:

`adscript --llvm-ir --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo.ll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo_entrada.adscript</span>

- Compilación cruzada de un archivo a un archivo objeto para una arquitectura de CPU o un sistema operativo foráneo:

`adscript --target-triple `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">i386-linux-elf</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo_entrada.adscript</span>
