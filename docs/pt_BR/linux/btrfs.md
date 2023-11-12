---
layout: page
title: linux/btrfs (português (Brasil))
description: "Um sistema de arquivos baseado no princípio copy-on-write (COW) para Linux."
content_hash: 2c3b4e77855354db289004172906a6d822774d21
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/btrfs.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/btrfs.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs

Um sistema de arquivos baseado no princípio copy-on-write (COW) para Linux.
Alguns subcomandos como `btrfs device` têm sua própria documentação de uso.
Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs.html>.

- Cria subvolume:

`sudo btrfs subvolume create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/subvolume</span>

- Lista subvolumes:

`sudo btrfs subvolume list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/ponto_de_montagem</span>

- Mostra informações de uso do espaço:

`sudo btrfs filesystem df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/ponto_de_montagem</span>

- Ativa a cota:

`sudo btrfs quota enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/subvolume</span>

- Mostra a cota:

`sudo btrfs qgroup show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/subvolume</span>
