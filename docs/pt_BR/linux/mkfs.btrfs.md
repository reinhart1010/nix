---
layout: page
title: linux/mkfs.btrfs (português (Brasil))
description: "Crie um sistema de arquivos btrfs."
content_hash: 72042a047dd4fcb9674ddc84731d34ecd7d32cf4
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/linux/mkfs.btrfs.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/mkfs.btrfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfs.btrfs

Crie um sistema de arquivos btrfs.
O padrão é `raid1`, que especifica 2 cópias de um determinado bloco de dados espalhados por 2 dispositivos diferentes.
Mais informações: <https://btrfs.readthedocs.io/en/latest/mkfs.btrfs.html>.

- Cria um sistema de arquivos btrfs em um único dispositivo:

`sudo mkfs.btrfs --metadata single --data single `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>

- Cria um sistema de arquivos btrfs em vários dispositivos com raid1:

`sudo mkfs.btrfs --metadata raid1 --data raid1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdN</span>

- Define um rótulo para o sistema de arquivos:

`sudo mkfs.btrfs --label "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rótulo</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdN</span>`]`
