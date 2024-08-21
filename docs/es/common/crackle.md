---
layout: page
title: common/crackle (español)
description: "Crackea y descifra el cifrado Bluetooth Low Energy (BLE)."
content_hash: b6091718de9ffea485aa797172c24066901c6ad1
last_modified_at: 2024-08-21
related_topics:
  - title: English version
    url: /en/common/crackle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crackle

Crackea y descifra el cifrado Bluetooth Low Energy (BLE).
Más información: <https://github.com/mikeryan/crackle>.

- Comprueba si las comunicaciones BLE grabadas contienen los paquetes necesarios para recuperar claves temporales (TKs):

`crackle -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/entrada.pcap</span>

- Utiliza la fuerza bruta para recuperar la TK de los eventos de emparejamiento registrados y la utiliza para descifrar todas las comunicaciones posteriores:

`crackle -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/entrada.pcap</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/desencriptado.pcap</span>

- Utiliza la clave a largo plazo (LTK) especificada para descifrar la comunicación grabada:

`crackle -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/entrada.pcap</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/descifrar.pcap</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">81b06facd90fe7a6e9bbd9cee59736a7</span>
