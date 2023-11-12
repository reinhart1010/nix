---
layout: page
title: common/virsh-pool-destroy (português (Brasil))
description: "Interrompe um pool de armazenamento ativo de máquina virtual."
content_hash: 72ef7253455316d073170c2dffb7400f1276d314
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/virsh-pool-destroy.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/virsh-pool-destroy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh pool-destroy

Interrompe um pool de armazenamento ativo de máquina virtual.
Veja também: `virsh`, `virsh-pool-delete`.
Mais informações: <https://manned.org/virsh>.

- Interrompe um pool de armazenamento especificado pelo nome ou UUID (determinado usando `virsh pool-list`):

`virsh pool-destroy --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome|uuid</span>
