---
layout: page
title: linux/btrfs-filesystem (português (Brasil))
description: "Gerencia sistemas de arquivos btrfs."
content_hash: 91656fc2230d949337d2bbba001830b7446027bd
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/btrfs-filesystem.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-filesystem.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs-filesystem.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs filesystem

Gerencia sistemas de arquivos btrfs.
Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs-filesystem.html>.

- Mostra uso do sistema de arquivos (opcionalmente execute como root para mostrar informações detalhadas):

`btrfs filesystem usage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/montagem_btrfs</span>

- Mostra uso por dispositivos individuais:

`sudo btrfs filesystem show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/montagem_btrfs</span>

- Desfragmenta um único arquivo em um sistema de arquivos btrfs (evite enquanto um agente de desduplicação estiver em execução):

`sudo btrfs filesystem defragment -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Desfragmenta um diretório recursivamente (não cruza os limites do subvolume):

`sudo btrfs filesystem defragment -v -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Força a sincronização de blocos de dados não gravados com o(s) disco(s):

`sudo btrfs filesystem sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/montagem_btrfs</span>

- Resume o uso do disco para os arquivos em um diretório recursivamente:

`sudo btrfs filesystem du --summarize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>
