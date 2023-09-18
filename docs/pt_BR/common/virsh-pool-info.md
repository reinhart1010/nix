---
layout: page
title: common/virsh-pool-info (português (Brasil))
description: "Lista informações sobre um pool de armazenamento de máquina virtual."
content_hash: 1642469fc90adc8e31c4ed68475525d991899d9e
last_modified_at: 2023-09-18
related_topics:
  - title: English version
    url: /en/common/virsh-pool-info.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># virsh pool-info

Lista informações sobre um pool de armazenamento de máquina virtual.
Veja também: `virsh`.
Mais informações: <https://manned.org/virsh>.

- Lista o nome, UUID, estado, tipo de persistência, status de inicialização automática, capacidade, espaço alocado e espaço disponível para o pool de armazenamento especificado pelo nome ou UUID (determinado usando `virsh pool-list`):

`virsh pool-info --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome|uuid</span>
