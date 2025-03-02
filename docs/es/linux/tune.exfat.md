---
layout: page
title: linux/tune.exfat (español)
description: "Ajusta los parámetros del sistema de archivos en un sistema de archivos exFAT."
content_hash: 3a068c1dc73c659f309e534950800319b428e161
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/tune.exfat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tune.exfat

Ajusta los parámetros del sistema de archivos en un sistema de archivos exFAT.
Más información: <https://manned.org/tune.exfat>.

- Imprime la etiqueta de volumen de un sistema de archivos:

`tune.exfat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--print-label</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- Establece la etiqueta de volumen de un sistema de archivos:

`tune.exfat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-L|--set-label</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nueva_etiqueta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- Imprime el GUID del volumen de un sistema de archivos:

`tune.exfat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-u|--print-guid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- Establece el GUID de volumen de un sistema de archivos:

`tune.exfat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-U|--set-guid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuevo_guid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- Imprime el número de serie del volumen de un sistema de archivos:

`tune.exfat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--print-serial</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- Establece el volumen de serie de un sistema de archivos:

`tune.exfat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-I|--set-serial</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuevo_serial</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>
