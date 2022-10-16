---
layout: page
title: linux/btrfs-filesystem (português (Brasil))
description: "Gerencia sistemas de arquivos btrfs."
content_hash: 838e9e382e3042e70dc5b9a5ac382ed7a743a31f
related_topics:
  - title: English version
    url: /en/linux/btrfs-filesystem.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs-filesystem.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># btrfs filesystem

Gerencia sistemas de arquivos btrfs.
Mais informações: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-filesystem>.

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
