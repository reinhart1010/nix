---
layout: page
title: linux/btrfs-inspect-internal (português (Brasil))
description: "Consulta informações internas de um sistema de arquivos btrfs."
content_hash: 3f66da53da58158e0c5518527f6b96f35c93f823
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/btrfs-inspect-internal.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-inspect-internal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs inspect-internal

Consulta informações internas de um sistema de arquivos btrfs.
Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs-inspect-internal.html>.

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
