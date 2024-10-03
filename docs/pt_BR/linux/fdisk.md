---
layout: page
title: linux/fdisk (português (Brasil))
description: "Gerencia de tabelas de partições e partições em um disco rígido."
content_hash: e48a3aefec27dcfd60ae733567c49922b6b04db1
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/linux/fdisk.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/fdisk.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/fdisk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fdisk

Gerencia de tabelas de partições e partições em um disco rígido.
Veja também: `partprobe`.
Mais informações: <https://manned.org/fdisk>.

- Lista partições:

`sudo fdisk -l`

- Inicia o manipulador de partições:

`sudo fdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Uma vez particionando um disco, cria uma partição:

`n`

- Uma vez particionando um disco, seleciona uma partição para excluir:

`d`

- Uma vez particionando um disco, mostra uma tabela de partições:

`p`

- Uma vez particionando um disco, grava em disco as mudanças feitas:

`w`

- Uma vez particionando um disco, descarta as mudanças feitas:

`q`

- Uma vez particionando um disco, abre o menu de ajuda:

`m`
