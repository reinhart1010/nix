---
layout: page
title: linux/btrfs-subvolume (português (Brasil))
description: "Gerencia subvolumes e snapshots btrfs."
content_hash: 2904192d80b7859e75965af5d571b4396e06534b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/btrfs-subvolume.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-subvolume.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs-subvolume.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs subvolume

Gerencia subvolumes e snapshots btrfs.
Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs-subvolume.html>.

- Cria um novo subvolume vazio:

`sudo btrfs subvolume create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/novo_subvolume</span>

- Lista todos os subvolumes e snapshots no sistema de arquivos especificado:

`sudo btrfs subvolume list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/sistema_de_arquivos_btrfs</span>

- Exclui um subvolume:

`sudo btrfs subvolume delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/subvolume</span>

- Cria um snapshot somente leitura de um subvolume existente:

`sudo btrfs subvolume snapshot -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/subvolume_de_origem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>

- Cria um snapshot de leitura/gravação de um subvolume existente:

`sudo btrfs subvolume snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/subvolume_de_origem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/destino</span>

- Mostra informações detalhadas sobre um subvolume:

`sudo btrfs subvolume show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/subvolume</span>
