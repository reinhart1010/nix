---
layout: page
title: linux/zramctl (español)
description: "Configura y controla dispositivos zram."
content_hash: e1a01ee4abde3639795d1dda0802bdc926e80685
last_modified_at: 2024-07-02
related_topics:
  - title: English version
    url: /en/linux/zramctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/zramctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/zramctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zramctl

Configura y controla dispositivos zram.
Usa `mkfs` o `mkswap` para formatear dispositivos zram a particiones.
Más información: <https://manned.org/zramctl>.

- Comprueba si zram está habilitado:

`lsmod | grep -i zram`

- Habilita zram con un número dinámico de dispositivos (usa `zramctl` para configurar más dispositivos):

`sudo modprobe zram`

- Habilita zram con exactamente 2 dispositivos:

`sudo modprobe zram num_devices=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- Encuentra e inicializa el siguiente dispositivo zram libre a una unidad virtual de 2 GB usando compresión LZ4:

`sudo zramctl --find --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2GB</span>` --algorithm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lz4</span>

- Lista los dispositivos actualmente inicializados:

`sudo zramctl`
