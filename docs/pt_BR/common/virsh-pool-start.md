---
layout: page
title: common/virsh-pool-start (português (Brasil))
description: "Inicia um pool de armazenamento de máquina virtual previamente configurado, mas inativo."
content_hash: 3c1788aa950dda9ecd96fab33e1ce1fcd3a72cf6
last_modified_at: 2023-09-18
related_topics:
  - title: English version
    url: /en/common/virsh-pool-start.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># virsh pool-start

Inicia um pool de armazenamento de máquina virtual previamente configurado, mas inativo.
Veja também: `virsh`, `virsh-pool-define-as`, `virsh-pool-destroy`.
Mais informações: <https://manned.org/virsh>.

- Inicia o pool de armazenamento especificado pelo nome ou UUID (determinado usando `virsh pool-list`) e cria o sistema de armazenamento subjacente se ele não existir:

`virsh pool-start --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome|uuid</span>` --build`
