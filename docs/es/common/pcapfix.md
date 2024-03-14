---
layout: page
title: common/pcapfix (español)
description: "Repara archivos PCAP y PcapNG dañados o corruptos."
content_hash: 906682d9c8832d7f5e9570d170356725e60a3571
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/pcapfix.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pcapfix

Repara archivos PCAP y PcapNG dañados o corruptos.
Más información: <https://f00l.de/pcapfix/>.

- Repara un archivo PCAP/PcapNG (Nota: para los archivos PCAP, sólo se escanean los primeros 262144 bytes de cada paquete):

`pcapfix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pcapng</span>

- Repara un archivo PCAP completo:

`pcapfix --deep-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pcap</span>

- Repara un archivo PCAP/PcapNG y escribe el archivo reparado en la ubicación especificada:

`pcapfix --outfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_reparado.pcap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pcap</span>

- Repara un archivo PcapNG y lo trata como un archivo PcapNG, ignorando el reconocimiento automático:

`pcapfix --pcapng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pcapng</span>

- Repara un archivo y muestra el proceso en detalle:

`pcapfix --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pcap</span>
