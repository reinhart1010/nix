---
layout: page
title: common/virsh-connect (português (Brasil))
description: "Conectar-se a um hipervisor de máquina virtual."
content_hash: ca127cfdbe756652461d35f4a12e393a3fc6ac45
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/virsh-connect.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/virsh-connect.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh-connect

Conectar-se a um hipervisor de máquina virtual.
Veja também: `virsh`.
Mais informações: <https://manned.org/virsh>.

- Conecta ao hipervisor padrão:

`virsh connect`

- Conecta como root ao hipervisor local QEMU/KVM:

`virsh connect qemu:///system`

- Inicia uma nova instância do hipervisor e conectar-se a ela como usuário local:

`virsh connect qemu:///session`

- Conecta como root a um hipervisor remoto usando SSH:

`virsh connect qemu+ssh://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário@nome_do_host</span>`/system`
