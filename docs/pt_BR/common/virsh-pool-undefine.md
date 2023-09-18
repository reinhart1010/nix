---
layout: page
title: common/virsh-pool-undefine (português (Brasil))
description: "Exclui o arquivo de configuração em `/etc/libvirt/storage` para um pool de armazenamento de máquina virtual parado."
content_hash: 480b6e1ec86a16e7c5569f74212ac6b06cb372d9
last_modified_at: 2023-09-18
related_topics:
  - title: English version
    url: /en/common/virsh-pool-undefine.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># virsh pool-undefine

Exclui o arquivo de configuração em `/etc/libvirt/storage` para um pool de armazenamento de máquina virtual parado.
Veja também: `virsh`, `virsh-pool-destroy`.
Mais informações: <https://manned.org/virsh>.

- Excluir a configuração do pool de armazenamento pelo nome ou UUID especificado (determinado usando `virsh pool-list`):

`virsh pool-undefine --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome|uuid</span>
