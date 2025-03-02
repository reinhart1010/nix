---
layout: page
title: common/llvm-mc (español)
description: "LLVM Machine Code Playground. Proporciona un conjunto de herramientas para trabajar con código de máquina LLVM."
content_hash: 4cb3e45b32259ed2d70de61514393c2c938f0045
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/llvm-mc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# llvm-mc

LLVM Machine Code Playground. Proporciona un conjunto de herramientas para trabajar con código de máquina LLVM.
Forma parte de LLVM.
Más información: <https://llvm.org/docs/CommandGuide/llvm-mc.html>.

- Ensambla un archivo de código ensamblador en un archivo con código de máquina:

`llvm-mc --filetype=obj -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/entrada.s</span>

- Desensambla un archivo con código de máquina en un archivo de código ensamblador:

`llvm-mc --disassemble -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.s</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/entrada.o</span>

- Compila el archivo de código de bits LLVM en código ensamblador:

`llvm-mc -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.s</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/entrada.bc</span>

- Ensambla el código ensamblador desde el flujo de entrada estándar y muestra la codificación en el flujo de salida estándar:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">addl %eax, %ebx</span>`" | llvm-mc -show-encoding -show-inst`

- Desensambla el código de máquina del flujo de entrada estándar para la tripleta especificada:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0xCD 0x21</span>`" | llvm-mc --disassemble -triple=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_objetivo</span>
