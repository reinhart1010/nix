---
layout: page
title: common/wdiff (español)
description: "Muestra las diferencias de palabras entre archivos de texto."
content_hash: 47fbc1c240f70b870756a2b5e8ca7e2c9ff2f280
last_modified_at: 2024-03-28
related_topics:
  - title: English version
    url: /en/common/wdiff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wdiff

Muestra las diferencias de palabras entre archivos de texto.
Más información: <https://www.gnu.org/software/wdiff/>.

- Compara dos archivos:

`wdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo2</span>

- Ignora mayúsculas y minúsculas al comparar:

`wdiff --ignore-case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo2</span>

- Muestra cuantas palabras se han eliminado, insertado o sustituido:

`wdiff --statistics `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo2</span>
