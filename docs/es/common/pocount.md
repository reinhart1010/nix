---
layout: page
title: common/pocount (español)
description: "Utilidad de Translate Toolkit para obtener el progreso de la traducción de un archivo, soporta varios formatos."
content_hash: 0727183999dece7ec0261d4a7e8ab344f99f017f
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/pocount.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pocount

Utilidad de Translate Toolkit para obtener el progreso de la traducción de un archivo, soporta varios formatos.
Más información: <https://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/pocount.html>.

- Imprime una tabla colorida con el progreso de la traducción de un archivo:

`pocount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.po</span>

- Imprime el progreso de las traducciones de varios archivos, una línea por archivo:

`pocount --short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">traducción_*.ts</span>

- Genera un archivo CSV con el progreso de la traducción de varios archivos:

`pocount --csv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">traducción_*.ts</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/progreso_de_traducción.csv</span>
