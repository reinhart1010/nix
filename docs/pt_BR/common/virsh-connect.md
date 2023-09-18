---
layout: page
title: common/virsh-connect (português (Brasil))
description: "Conectar-se a um hipervisor de máquina virtual."
content_hash: b8c6370cd63359638ad1ba8938d2612d720fdf8d
last_modified_at: 2023-09-18
related_topics:
  - title: English version
    url: /en/common/virsh-connect.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># virsh-connect

Conectar-se a um hipervisor de máquina virtual.
Veja também: `virsh`.
Mais informações: <https://manned.org/virsh>.

- Conectar-se ao hipervisor padrão:

`virsh connect`

- Conectar-se como root ao hipervisor local QEMU/KVM:

`virsh connect qemu:///system`

- Iniciar uma nova instância do hipervisor e conectar-se a ela como usuário local:

`virsh connect qemu:///session`

- Conectar-se como root a um hipervisor remoto usando ssh:

`virsh connect qemu+ssh://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário@nome_do_host</span>`/system`
