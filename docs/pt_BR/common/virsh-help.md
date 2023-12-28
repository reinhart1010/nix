---
layout: page
title: common/virsh-help (português (Brasil))
description: "Exibir informações sobre comandos ou grupos de comandos do `virsh`."
content_hash: f310e04174a0dd12862d758b7daffc2d87f1f897
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/virsh-help.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/virsh-help.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh-help

Exibir informações sobre comandos ou grupos de comandos do `virsh`.
Veja também: `virsh`.
Mais informações: <https://manned.org/virsh>.

- Lista os comandos do `virsh` agrupados em categorias relacionadas:

`virsh help`

- Lista as categorias de comandos:

`virsh help | grep "palavra-chave"`

- Lista os comandos de uma categoria:

`virsh help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palavra-chave_da_categoria</span>

- Mostra ajuda para um comando:

`virsh help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>
