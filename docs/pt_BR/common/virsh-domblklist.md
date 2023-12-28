---
layout: page
title: common/virsh-domblklist (português (Brasil))
description: "Listar informações sobre dispositivos de bloco associados a uma máquina virtual."
content_hash: a90baea2f34cb9c8236280042b1f5a9393aadeaa
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/virsh-domblklist.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/virsh-domblklist.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh-domblklist

Listar informações sobre dispositivos de bloco associados a uma máquina virtual.
Veja também: `virsh`.
Mais informações: <https://manned.org/virsh>.

- Lista o nome do destino e o caminho da origem dos dispositivos de bloco:

`virsh domblklist --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_vm</span>

- Lista o tipo de disco e o valor do dispositivo, bem como o nome do destino e o caminho da origem:

`virsh domblklist --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_vm</span>` --details`
