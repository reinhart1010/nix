---
layout: page
title: linux/btrfs-balance (português (Brasil))
description: "Balanceia grupos de blocos em um sistema de arquivos btrfs."
content_hash: 948ac3f3bfcd74065dfdc5bac6cc4747ec13fbaa
related_topics:
  - title: English version
    url: /en/linux/btrfs-balance.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># btrfs balance

Balanceia grupos de blocos em um sistema de arquivos btrfs.
Mais informações: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-balance>.

- Mostra o status de uma operação balance em execução ou pausada:

`sudo btrfs balance status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/sistema_de_arquivos_btrfs</span>

- Balanceia todos os grupos de blocos (lento; reescreve todos os blocos no sistema de arquivos):

`sudo btrfs balance start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/sistema_de_arquivos_btrfs</span>

- Balanceia grupos de blocos de dados com menos de 15% de utilização, executando a operação em segundo plano:

`sudo btrfs balance start --bg -dusage=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/sistema_de_arquivos_btrfs</span>

- Balanceia um máximo de 10 partes de metadados com menos de 20% de utilização e pelo menos 1 parte em um determinado dispositivo `devid` (consulte `btrfs filesystem show`):

`sudo btrfs balance start -musage=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>`,limit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`,devid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">devid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/sistema_de_arquivos_btrfs</span>

- Converte blocos de dados para raid6 e metadados para raid1c3 (veja mkfs.btrfs(8) para perfis):

`sudo btrfs balance start -dconvert=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raid6</span>` -mconvert=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raid1c3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/sistema_de_arquivos_btrfs</span>

- Converte blocos de dados para raid1, pulando pedaços já convertidos (por exemplo, após uma operação de conversão cancelada anterior):

`sudo btrfs balance start -dconvert=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raid1</span>`,soft `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/sistema_de_arquivos_btrfs</span>

- Cancela, pausa ou retoma uma operação de balanceamento em execução ou pausada:

`sudo btrfs balance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cancel|pause|resume</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/sistema_de_arquivos_btrfs</span>
