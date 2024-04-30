---
layout: page
title: common/par2 (español)
description: "Verificación y reparación de archivos utilizando archivos de paridad compatibles con PAR 2.0 (archivos .par2)."
content_hash: d4feda782163d1434a616faeb83c641c79dca728
last_modified_at: 2024-04-30
related_topics:
  - title: English version
    url: /en/common/par2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# par2

Verificación y reparación de archivos utilizando archivos de paridad compatibles con PAR 2.0 (archivos .par2).
Más información: <https://github.com/Parchive/par2cmdline/>.

- Crea un archivo de paridad con un nivel de porcentaje de redundancia establecido:

`par2 create -r`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1..100</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Crea un archivo de paridad con un número determinado de archivos de volumen (además del archivo de índice):

`par2 create -n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1..32768</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Verifica un fichero con un archivo de paridad:

`par2 verify -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.par2</span>

- Repara un fichero con un archivo de paridad:

`par2 repair -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.par2</span>
