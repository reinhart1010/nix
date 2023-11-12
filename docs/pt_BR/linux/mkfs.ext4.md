---
layout: page
title: linux/mkfs.ext4 (português (Brasil))
description: "Cria um sistema de arquivos ext4 dentro de uma partição."
content_hash: 8dc004627a3e1c0e04b8766509c4180ba79ece8c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/mkfs.ext4.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/mkfs.ext4.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfs.ext4

Cria um sistema de arquivos ext4 dentro de uma partição.
Mais informações: <https://manned.org/mkfs.ext4>.

- Cria um sistema de arquivos ext4 dentro da partição 1 no dispositivo b (`sdb1`):

`sudo mkfs.ext4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Cria um sistema de arquivo ext4 com um rótulo de volume:

`sudo mkfs.ext4 -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rótulo_de_volume</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
