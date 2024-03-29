---
layout: page
title: common/virsh-pool-build (português (Brasil))
description: "Constrói o sistema de armazenamento subjacente para um pool de armazenamento de máquina virtual, conforme definido em seu arquivo de configuração em `/etc/libvirt/storage`."
content_hash: ea6c31a574afdeea2daeaca0d18727c0e43afac3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/virsh-pool-build.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/virsh-pool-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh pool-build

Constrói o sistema de armazenamento subjacente para um pool de armazenamento de máquina virtual, conforme definido em seu arquivo de configuração em `/etc/libvirt/storage`.
Veja também: `virsh`, `virsh-pool-define-as`, `virsh-pool-start`.
Mais informações: <https://manned.org/virsh>.

- Constrói o pool de armazenamento especificado pelo nome ou UUID (determinado usando `virsh pool-list`):

`virsh pool-build --pool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome|uuid</span>
