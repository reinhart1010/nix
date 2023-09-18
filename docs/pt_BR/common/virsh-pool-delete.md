---
layout: page
title: common/virsh-pool-delete (português (Brasil))
description: "Exclui o sistema de armazenamento subjacente de um pool de armazenamento de máquina virtual inativo."
content_hash: eb0dae74061eff4113863bc60327fce93c0214bf
last_modified_at: 2023-09-18
related_topics:
  - title: English version
    url: /en/common/virsh-pool-delete.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># virsh pool-delete

Exclui o sistema de armazenamento subjacente de um pool de armazenamento de máquina virtual inativo.
Veja também: `virsh`, `virsh-pool-destroy`, `virsh-pool-undefine`.
Mais informações: <https://manned.org/virsh>.

- Exclui o sistema de armazenamento subjacente para o pool de armazenamento especificado pelo nome ou UUID (determinado usando `virsh pool-list`):

`virsh pool-delete --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome|uuid</span>
