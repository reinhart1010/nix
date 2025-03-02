---
layout: page
title: common/filecheck (español)
description: "Verificador de archivos de coincidencia de patrones flexible."
content_hash: b4626255ea767ac2a93443b6d60ae73242c20d95
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/filecheck.html
    icon: bi bi-globe
tldri18n_status: 2
---
# FileCheck

Verificador de archivos de coincidencia de patrones flexible.
Se utiliza típicamente a partir de pruebas de regresión LLVM y forma parte de una prueba `lit`.
Más información: <https://llvm.org/docs/CommandGuide/FileCheck.html>.

- Compara el contenido de `archivo_entrada` con el archivo de patrones `archivo_comprobado`:

`FileCheck --input-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_entrada</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_comprobación</span>

- Busca coincidencias de `stdin` con el archivo de patrones `archivo_de_comprobación`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algún_texto</span>`" | FileCheck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_comprobación</span>

- Busca coincidencias con el `prefijo` de comprobación personalizado especificado (Nota: el prefijo predeterminado es `CHECK`):

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algún_texto</span>`" | FileCheck --check-prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefijo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_comprobado</span>

- Imprime las coincidencias de patrón de directivas:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">some_text</span>`" | FileCheck -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_comprobado</span>

- Introduce `llvm_code.ll` en llvm-as y, a continuación, envía la salida a FileCheck para que coincida:

`llvm-as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/código_llvm_.ll</span>` | FileCheck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_comprobado</span>
