---
layout: page
title: common/pcapfix (español)
description: "Repara archivos `pcap` y `pcapng` dañados o corruptos."
content_hash: c3867e8d34c4a8fffa8592fe19af684d1dc01044
last_modified_at: 2024-02-15
related_topics:
  - title: English version
    url: /en/common/pcapfix.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pcapfix

Repara archivos `pcap` y `pcapng` dañados o corruptos.
Más información: <https://f00l.de/pcapfix/>.

- Repara un archivo `pcap`/`pcapng` (Nota: para los archivos `pcap`, sólo se escanean los primeros 262144 bytes de cada paquete):

`pcapfix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pcapng</span>

- Repara un archivo `pcap` completo:

`pcapfix --deep-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pcap</span>

- Repara un archivo `pcap`/`pcapng` y escribe el archivo reparado en la ubicación especificada:

`pcapfix --outfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_reparado.pcap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pcap</span>

- Repara un archivo `pcapng` y lo trata como un archivo `pcapng`, ignorando el reconocimiento automático:

`pcapfix --pcapng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pcapng</span>

- Repara un archivo y muestra el proceso en detalle:

`pcapfix --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pcap</span>
