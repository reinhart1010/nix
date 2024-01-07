---
layout: page
title: common/adscript (español)
description: "Compilador de archivos Adscript."
content_hash: e9eb0b10be9a7ca4faf8641288c1292ebc1a2acf
last_modified_at: 2024-01-07
related_topics:
  - title: Deutsch version
    url: /de/common/adscript.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/adscript.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adscript.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adscript.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/adscript.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adscript.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adscript.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adscript

Compilador de archivos Adscript.
Más información: <https://github.com/Amplus2/Adscript>.

- Compila un archivo en un archivo objeto:

`adscript --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_entrada.adscript</span>

- Compila y vincula un archivo a un ejecutable independiente:

`adscript --executable --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo_entrada.adscript</span>

- Compila un archivo a LLVM IR en lugar de código de máquina nativo:

`adscript --llvm-ir --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo.ll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo_entrada.adscript</span>

- Crea un archivo con código objeto para otra arquitectura u otro sistema operativo:

`adscript --target-triple `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">i386-linux-elf</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo_entrada.adscript</span>
