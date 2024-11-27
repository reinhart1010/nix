---
layout: page
title: common/airodump-ng (español)
description: "Captura paquetes y muestra información sobre redes inalámbricas."
content_hash: 98daf07d3243d4cb4a1e8b354eae25700ce02154
last_modified_at: 2024-11-27
related_topics:
  - title: Deutsch version
    url: /de/common/airodump-ng.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/airodump-ng.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/airodump-ng.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/airodump-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/airodump-ng.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/airodump-ng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airodump-ng

Captura paquetes y muestra información sobre redes inalámbricas.
Parte de `aircrack-ng`.
Más información: <https://www.aircrack-ng.org/doku.php?id=airodump-ng>.

- Captura paquetes y muestra información sobre red(es) inalámbricas en la banda de 2.4GHz:

`sudo airodump-ng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Captura paquetes y muestra información sobre red(es) inalámbrica(s) en la banda de 5GHz:

`sudo airodump-ng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` --band a`

- Captura paquetes y muestra información sobre rede(s) inalámbrica(s) en las bandas 2.4GHz y 5GHz:

`sudo airodump-ng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` --band abg`

- Captura paquetes y muestra información sobre una red inalámbrica dada la dirección MAC y canal, y guarda la salida en un archivo:

`sudo airodump-ng --channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">canal</span>` --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaz</span>
