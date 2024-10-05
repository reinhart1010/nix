---
layout: page
title: linux/btrfs (português (Brasil))
description: "Um sistema de arquivos baseado no princípio copy-on-write (COW) para Linux."
content_hash: 91cfb3d2a367a8a705247a2dfafe57fe96dc6eeb
last_modified_at: 2024-10-05
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
Alguns subcomandos como `device` têm sua própria documentação de uso.
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
