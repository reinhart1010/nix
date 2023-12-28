---
layout: page
title: linux/lsblk (português (Brasil))
description: "Lista informações sobre dispositivos."
content_hash: d2dff22a3392b94b5336c996d2760ac5b696fdd5
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/linux/lsblk.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/lsblk.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/linux/lsblk.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/lsblk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/lsblk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lsblk

Lista informações sobre dispositivos.
Mais informações: <https://manned.org/lsblk>.

- Lista todos dispositivos de armazenamento no formato de árvore:

`lsblk`

- Também lista dispositivos vazios:

`lsblk -a`

- Mostra a coluna de tamanhos em bytes, em vez de um formato legível por humanos:

`lsblk -b`

- Mostra na saída padrão informações sobre os filesystems dos dispositivos:

`lsblk -f`

- Utiliza caracteres ASCII para o formato de árvore:

`lsblk -i`

- Mostra na saída padrão informações sobre block-device topology:

`lsblk -t`

- Excluír da saída padrão os dispositivos específicados por seus repectivos números separados por vírgulas:

`lsblk -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,7</span>

- Mostra um resumo de forma customizada passando as colunas separadas por vírgulas:

`lsblk --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">NAME</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SERIAL</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MODEL</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TRAN</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TYPE</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIZE</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FSTYPE</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MOUNTPOINT</span>
