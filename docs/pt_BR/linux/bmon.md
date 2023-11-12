---
layout: page
title: linux/bmon (português (Brasil))
description: "Monitora a largura de banda e produz estatísticas relacionadas a rede."
content_hash: a02904590093c402b1c3563e326be7ab631d298a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/bmon.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/bmon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bmon

Monitora a largura de banda e produz estatísticas relacionadas a rede.
Mais informações: <https://github.com/tgraf/bmon>.

- Exibir uma lista com todas as interfaces de rede:

`bmon -a`

- Exibir as taxas de transferência de dados em bits por segundo:

`bmon -b`

- Definir quais interfaces serão visíveis:

`bmon -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface_1,interface_2,interface_3</span>

- Definir o intervalo (em segundos) que a taxa por contador será calculada:

`bmon -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.0</span>
