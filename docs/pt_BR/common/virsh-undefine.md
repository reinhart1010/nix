---
layout: page
title: common/virsh-undefine (português (Brasil))
description: "Excluir uma máquina virtual."
content_hash: 484204cefdbadd528da8e66190063122df386c47
last_modified_at: 2023-09-18
related_topics:
  - title: English version
    url: /en/common/virsh-undefine.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># virsh-undefine

Excluir uma máquina virtual.
Mais informações: <https://manned.org/virsh>.

- Excluir apenas o arquivo de configuração da máquina virtual:

`virsh undefine --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_vm</span>

- Excluir o arquivo de configuração e todos os volumes de armazenamento associados:

`virsh undefine --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_vm</span>` --remove-all-storage`

- Excluir o arquivo de configuração e os volumes de armazenamento especificados usando o nome de destino ou o nome de origem (obtido a partir do comando `virsh domblklist`):

`virsh undefine --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_vm</span>` --storage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sda,caminho/para/origem</span>
