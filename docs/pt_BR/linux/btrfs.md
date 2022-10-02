---
layout: page
title: linux/btrfs (português (Brasil))
description: "Um sistema de arquivos baseado no princípio copy-on-write (COW) para Linux."
content_hash: c971610004316502ba9006522de84d39fa8ce654
related_topics:
  - title: English version
    url: /en/linux/btrfs.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># btrfs

Um sistema de arquivos baseado no princípio copy-on-write (COW) para Linux.
Alguns subcomandos como `btrfs device` têm sua própria documentação de uso.
Mais informações: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs>.

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
