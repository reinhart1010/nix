---
layout: page
title: common/virsh-pool-autostart (português (Brasil))
description: "Habilita ou desabilita a inicialização automática para um pool de armazenamento de máquina virtual."
content_hash: 1fb1d623b0c0c7c9c90c07fc8c498ce1073a1f81
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/virsh-pool-autostart.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/virsh-pool-autostart.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh pool-autostart

Habilita ou desabilita a inicialização automática para um pool de armazenamento de máquina virtual.
Veja também: `virsh`.
Mais informações: <https://manned.org/virsh>.

- Habilita a inicialização automática para o pool de armazenamento especificado pelo nome ou UUID (determinado usando `virsh pool-list`):

`virsh pool-autostart --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome|uuid</span>

- Desabilita a inicialização automática para o pool de armazenamento especificado pelo nome ou UUID:

`virsh pool-autostart --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome|uuid</span>` --disable`
