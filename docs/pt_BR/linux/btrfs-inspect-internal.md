---
layout: page
title: linux/btrfs-inspect-internal (português (Brasil))
description: "Consulta informações internas de um sistema de arquivos btrfs."
content_hash: d12888a2394d87f30f665ea68bd8f68dec8815c1
related_topics:
  - title: English version
    url: /en/linux/btrfs-inspect-internal.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># btrfs inspect-internal

Consulta informações internas de um sistema de arquivos btrfs.
Mais informações: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-inspect-internal>.

- Imprime informações de superblocos:

`sudo btrfs inspect-internal dump-super `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/partição</span>

- Imprime as informações do superbloco e de todas as suas cópias:

`sudo btrfs inspect-internal dump-super --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/partição</span>

- Imprime informações de metadados do sistema de arquivos:

`sudo btrfs inspect-internal dump-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/partição</span>

- Imprime lista de arquivos no `n`-ésimo inode:

`sudo btrfs inspect-internal inode-resolve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/montagem_btrfs</span>

- Imprime a lista de arquivos em um determinado endereço lógico:

`sudo btrfs inspect-internal logical-resolve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endereço_lógico</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/montagem_btrfs</span>

- Imprime as estatísticas das árvores raiz, extensão, csum e fs:

`sudo btrfs inspect-internal tree-stats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/partição</span>
