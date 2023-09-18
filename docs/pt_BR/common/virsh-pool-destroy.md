---
layout: page
title: common/virsh-pool-destroy (português (Brasil))
description: "Interrompe um pool de armazenamento ativo de máquina virtual."
content_hash: 72ef7253455316d073170c2dffb7400f1276d314
last_modified_at: 2023-09-18
related_topics:
  - title: English version
    url: /en/common/virsh-pool-destroy.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># virsh pool-destroy

Interrompe um pool de armazenamento ativo de máquina virtual.
Veja também: `virsh`, `virsh-pool-delete`.
Mais informações: <https://manned.org/virsh>.

- Interrompe um pool de armazenamento especificado pelo nome ou UUID (determinado usando `virsh pool-list`):

`virsh pool-destroy --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome|uuid</span>
