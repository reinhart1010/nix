---
layout: page
title: linux/zramctl (português (Brasil))
description: "Configura e controla dispositivos zram."
content_hash: 8c07a44e94c62a6ab517730b57178edef668fa2d
related_topics:
  - title: English version
    url: /en/linux/zramctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/zramctl.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># zramctl

Configura e controla dispositivos zram.
Use `mkfs` ou `mkswap` para formatar dispositivos zram para partições.
Mais informações: <https://manned.org/zramctl>.

- Verifica se o zram está habilitado:

`lsmod | grep -i zram`

- Habilita o zram com um número dinâmico de dispositivos (use `zramctl` para configurar ainda mais os dispositivos):

`sudo modprobe zram`

- Habilita o zram com exatamente 2 dispositivos:

`sudo modprobe zram num_devices=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- Encontra e inicializa o próximo dispositivo zram gratuito em uma unidade virtual de 2 GB usando a compressão LZ4:

`sudo zramctl --find --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2GB</span>` --algorithm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lz4</span>

- Lista dispositivos atualmente inicializados:

`zramctl`