---
layout: page
title: common/virsh-pool-list (português (Brasil))
description: "Lista informações sobre pools de armazenamento de máquinas virtuais."
content_hash: 1727c35e40ed4440b8887db0147283330afcc26d
last_modified_at: 2023-09-18
related_topics:
  - title: English version
    url: /en/common/virsh-pool-list.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># virsh pool-list

Lista informações sobre pools de armazenamento de máquinas virtuais.
Veja também: `virsh`, `virsh-pool-autostart`, `virsh-pool-define-as`.
Mais informações: <https://manned.org/virsh>.

- Lista o nome, estado e se a inicialização automática está habilitada ou desabilitada para pools de armazenamento ativos:

`virsh pool-list`

- Lista informações para pools de armazenamento ativos e inativos ou apenas inativos:

`virsh pool-list --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all|inactive</span>

- Lista informações estendidas sobre persistência, capacidade, alocação e espaço disponível para pools de armazenamento ativos:

`virsh pool-list --details`

- Lista informações para pools de armazenamento ativos com inicialização automática habilitada ou desabilitada:

`virsh pool-list --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">autostart|no-autostart</span>

- Lista informações para pools de armazenamento ativos que são persistentes ou transitórios:

`virsh pool-list --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">persistent|transient</span>

- Lista o nome e UUID dos pools de armazenamento ativos:

`virsh pool-list --name --uuid`
