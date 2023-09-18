---
layout: page
title: common/virsh-domblklist (português (Brasil))
description: "Listar informações sobre dispositivos de bloco associados a uma máquina virtual."
content_hash: 2873ab2650d62ca5c974c505d080bf1737a06732
last_modified_at: 2023-09-18
related_topics:
  - title: English version
    url: /en/common/virsh-domblklist.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># virsh-domblklist

Listar informações sobre dispositivos de bloco associados a uma máquina virtual.
Veja também: `virsh`.
Mais informações: <https://manned.org/virsh>.

- Listar o nome do destino e o caminho da origem dos dispositivos de bloco:

`virsh domblklist --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_vm</span>

- Listar o tipo de disco e o valor do dispositivo, bem como o nome do destino e o caminho da origem:

`virsh domblklist --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_vm</span>` --details`
