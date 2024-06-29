---
layout: page
title: linux/zramctl (português (Brasil))
description: "Configura e controla dispositivos zram."
content_hash: 6251e595a71bc0094474272ecf390356f9bf5d01
last_modified_at: 2024-06-29
related_topics:
  - title: English version
    url: /en/linux/zramctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/zramctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zramctl

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

`sudo zramctl`
