---
layout: page
title: common/virsh-pool-define-as (português (Brasil))
description: "Cria um arquivo de configuração em `/etc/libvirt/storage` para um pool de armazenamento persistente de máquina virtual a partir dos argumentos fornecidos."
content_hash: 9bafd90ff59f40c885165bdc7e3a25f3eb158fe3
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/virsh-pool-define-as.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/virsh-pool-define-as.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh pool-define-as

Cria um arquivo de configuração em `/etc/libvirt/storage` para um pool de armazenamento persistente de máquina virtual a partir dos argumentos fornecidos.
Veja também: `virsh`, `virsh-pool-build`, `virsh-pool-start`.
Mais informações: <https://manned.org/virsh>.

- Cria o arquivo de configuração para um pool de armazenamento chamado pool_name usando `/var/vms` como o sistema de armazenamento subjacente:

`virsh pool-define-as --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pool</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dir</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/vms</span>
