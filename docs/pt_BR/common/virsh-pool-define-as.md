---
layout: page
title: common/virsh-pool-define-as (português (Brasil))
description: "Cria um arquivo de configuração em `/etc/libvirt/storage` para um pool de armazenamento persistente de máquina virtual a partir dos argumentos fornecidos."
content_hash: 7942b3f8b21c8ade63f3a895bd113d8713b38d66
last_modified_at: 2023-09-18
related_topics:
  - title: English version
    url: /en/common/virsh-pool-define-as.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># virsh pool-define-as

Cria um arquivo de configuração em `/etc/libvirt/storage` para um pool de armazenamento persistente de máquina virtual a partir dos argumentos fornecidos.
Veja também: `virsh`, `virsh-pool-build`, `virsh-pool-start`.
Mais informações: <https://manned.org/virsh>.

- Criar o arquivo de configuração para um pool de armazenamento chamado pool_name usando `/var/vms` como o sistema de armazenamento subjacente:

`virsh pool-define-as --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pool</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dir</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/vms</span>
