---
layout: page
title: common/virsh-undefine (português (Brasil))
description: "Excluir uma máquina virtual."
content_hash: 1a4b0ca3fb7c82ffb0ec7dd4f3009c0557581ef0
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/virsh-undefine.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/virsh-undefine.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh-undefine

Excluir uma máquina virtual.
Mais informações: <https://manned.org/virsh>.

- Exclui apenas o arquivo de configuração da máquina virtual:

`virsh undefine --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_vm</span>

- Exclui o arquivo de configuração e todos os volumes de armazenamento associados:

`virsh undefine --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_vm</span>` --remove-all-storage`

- Exclui o arquivo de configuração e os volumes de armazenamento especificados usando o nome de destino ou o nome de origem (obtido a partir do comando `virsh domblklist`):

`virsh undefine --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_vm</span>` --storage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sda,caminho/para/origem</span>
