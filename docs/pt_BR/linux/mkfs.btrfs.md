---
layout: page
title: linux/mkfs.btrfs (português (Brasil))
description: "Crie um sistema de arquivos btrfs."
content_hash: 89634ec45b65f10dbc8ca466d2e939deb785e924
last_modified_at: 2023-07-16
related_topics:
  - title: English version
    url: /en/linux/mkfs.btrfs.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/mkfs.btrfs.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mkfs.btrfs

Crie um sistema de arquivos btrfs.
O padrão é `raid1`, que especifica 2 cópias de um determinado bloco de dados espalhados por 2 dispositivos diferentes.
Mais informações: <https://btrfs.readthedocs.io/en/latest/mkfs.btrfs.html>.

- Criar um sistema de arquivos btrfs em um único dispositivo:

`sudo mkfs.btrfs --metadata single --data single `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>

- Criar um sistema de arquivos btrfs em vários dispositivos com raid1:

`sudo mkfs.btrfs --metadata raid1 --data raid1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdN</span>

- Definir um rótulo para o sistema de arquivos:

`sudo mkfs.btrfs --label "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rótulo</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdN</span>`]`
