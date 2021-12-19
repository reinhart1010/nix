---
layout: page
title: linux/lsblk (português (Brasil))
description: "Lista informações sobre dispositivos."
content_hash: a4d0a8442aaefd2cdf07dab86424fab957d02fd0
related_topics:
  - title: English version
    url: /en/linux/lsblk.html
    icon: bi bi-globe
---
# lsblk

Lista informações sobre dispositivos.
Mais informações: <https://manned.org/lsblk>.

- Lista todos dispositivos de armazenamento no formato de árvore:

`lsblk`

- Também lista dispositivos vazios:

`lsblk -a`

- Mostrar a coluna de tamanhos em bytes, em vez de um formato legível por humanos:

`lsblk -b`

- Mostrar na saída padrão informações sobre os filesystems dos dispositivos:

`lsblk -f`

- Utiliza caracteres ASCII para o formato de árvore:

`lsblk -i`

- Mostrar na saída padrão informações sobre block-device topology:

`lsblk -t`

- Excluír da saída padrão os dispositivos específicados por seus repectivos números separados por vírgulas:

`lsblk -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,7</span>

- Mostrar um resumo de forma customizada passando as colunas separadas por vírgulas:

`lsblk --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">NAME</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SERIAL</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MODEL</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TRAN</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TYPE</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIZE</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FSTYPE</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MOUNTPOINT</span>
