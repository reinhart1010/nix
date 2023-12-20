---
layout: page
title: linux/pw-link (português (Brasil))
description: "Gerenciar conexões entre portas no PipeWire."
content_hash: 4d6f63af2c01cd3075ef8eddd70985359a275c5b
last_modified_at: 2023-12-20
related_topics:
  - title: English version
    url: /en/linux/pw-link.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pw-link.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pw-link

Gerenciar conexões entre portas no PipeWire.
Mais informações: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

- Lista todos as saídas e entradas de áudio com seus IDs:

`pw-link --output --input --ids`

- Cria uma conexão entre uma porta de entrada e uma porta de saída:

`pw-link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_port_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_port_name</span>

- Desconecta duas portas:

`pw-link --disconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_port_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_port_name</span>

- Lista todas as conexões com seus IDs:

`pw-link --links --ids`

- Exibe ajuda:

`pw-link -h`
