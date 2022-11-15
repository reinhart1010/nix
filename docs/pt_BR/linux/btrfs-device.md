---
layout: page
title: linux/btrfs-device (português (Brasil))
description: "Gerencia dispositivos em um sistema de arquivos btrfs."
content_hash: 10bbfd7413432e0513476da0d2703099e04542e6
related_topics:
  - title: English version
    url: /en/linux/btrfs-device.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-device.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs-device.html
    icon: bi bi-globe
---
# btrfs device

Gerencia dispositivos em um sistema de arquivos btrfs.
Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs-device.html>.

- Adiciona um ou mais dispositivos a um sistema de arquivos btrfs:

`sudo btrfs device add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/bloco_do_dispositivo1</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/bloco_do_dispositivo2</span>`] `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/sistema_de_arquivos_btrfs</span>

- Remove um dispositivo de um sistema de arquivos btrfs:

`sudo btrfs device remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/dispositivo|id_do_dispositivo</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>`]`

- Exibe estatísticas de erro:

`sudo btrfs device stats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/sistema_de_arquivos_btrfs</span>

- Examina todos os discos e informa ao kernel todos os sistemas de arquivos btrfs detectados:

`sudo btrfs device scan --all-devices`

- Exibe estatísticas detalhadas de alocação por disco:

`sudo btrfs device usage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/sistema_de_arquivos_btrfs</span>
