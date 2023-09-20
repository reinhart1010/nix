---
layout: page
title: common/virsh-help (português (Brasil))
description: "Exibir informações sobre comandos ou grupos de comandos do `virsh`."
content_hash: 1d865edf6138fb96e490b3cbc0b96b2377edccf4
last_modified_at: 2023-09-18
related_topics:
  - title: English version
    url: /en/common/virsh-help.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># virsh-help

Exibir informações sobre comandos ou grupos de comandos do `virsh`.
Veja também: `virsh`.
Mais informações: <https://manned.org/virsh>.

- Listar os comandos do `virsh` agrupados em categorias relacionadas:

`virsh help`

- Listar as categorias de comandos:

`virsh help | grep "palavra-chave"`

- Listar os comandos de uma categoria:

`virsh help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palavra-chave_da_categoria</span>

- Mostrar ajuda para um comando:

`virsh help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>