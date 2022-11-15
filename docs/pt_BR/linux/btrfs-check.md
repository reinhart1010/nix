---
layout: page
title: linux/btrfs-check (português (Brasil))
description: "Verifica ou repara um sistema de arquivos btrfs."
content_hash: 2e8ea08987c22d2ca762dad77a885eea5092eb32
related_topics:
  - title: English version
    url: /en/linux/btrfs-check.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-check.html
    icon: bi bi-globe
---
# btrfs check

Verifica ou repara um sistema de arquivos btrfs.
Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs-check.html>.

- Verifica um sistema de arquivos btrfs:

`sudo btrfs check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/partição</span>

- Verifica e repara um sistema de arquivos btrfs (perigoso):

`sudo btrfs check --repair `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/partição</span>

- Mostra o andamento da verificação:

`sudo btrfs check --progress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/partição</span>

- Verifica a soma de verificação de cada bloco de dados (se o sistema de arquivos estiver bom):

`sudo btrfs check --check-data-csum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/partição</span>

- Usa o `n`-ésimo superbloco (`n` pode ser 0, 1 ou 2):

`sudo btrfs check --super `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/partição</span>

- Reconstrói a árvore de soma de verificação:

`sudo btrfs check --repair --init-csum-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/partição</span>

- Reconstrói a árvore de extensão:

`sudo btrfs check --repair --init-extent-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/partição</span>
