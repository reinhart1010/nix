---
layout: page
title: common/ipscan (español)
description: "Un rápido escáner de red diseñado para ser simple de usar."
content_hash: 868fc150cba75a680a136bd7aca2602e256cf711
last_modified_at: 2024-09-02
related_topics:
  - title: English version
    url: /en/common/ipscan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ipscan

Un rápido escáner de red diseñado para ser simple de usar.
También conocido como Angry IP Scanner.
Más información: <https://angryip.org/>.

- Escanea una dirección IP específica:

`ipscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1</span>

- Escanea un rango de direcciones IP:

`ipscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>

- Escanea un rango de direcciones IP y guardar los resultados en un archivo:

`ipscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.txt</span>

- Escanea IPs con un conjunto específico de puertos:

`ipscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80,443,22</span>

- Escanea con un retardo entre peticiones para evitar la congestión de la red:

`ipscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200</span>

- Muestra ayuda:

`ipscan --help`
