---
layout: page
title: linux/pw-top (português (Brasil))
description: "Mostra os nós e estatísticas de dispositivos PipeWire em tempo real."
content_hash: ed4aaf07c295dd5974dc881df1af707451f51d21
last_modified_at: 2024-01-03
related_topics:
  - title: English version
    url: /en/linux/pw-top.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pw-top

Mostra os nós e estatísticas de dispositivos PipeWire em tempo real.
Veja também: `pipewire`, `pw-dump`, `pw-cli`, `pw-profiler`.
Mais informações: <https://docs.pipewire.org/page_man_pw-top_1.html>.

- Mostra uma visualização interativa de nós e dispositivos PipeWire:

`pw-top`

- Monitora uma instância remota:

`pw-top --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_remoto</span>

- Imprime as informações várias vezes em vez de executar em modo interativo:

`pw-top --batch-mode`

- Imprime informações um número específico de vezes:

`pw-top --batch-mode --iterations `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>
