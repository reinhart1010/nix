---
layout: page
title: common/lpq (português (Brasil))
description: "Mostra o estado da fila de impressão."
content_hash: c1d30a922f7ed9b077d3d2472472eb70fe7567b1
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/lpq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lpq

Mostra o estado da fila de impressão.
Mais informações: <https://www.cups.org/doc/man-lpq.html>.

- Mostra os trabalhos na fila do destino padrão:

`lpq`

- Mostra os trabalhos na fila de todas as impressoras usando criptografia:

`lpq -a -E`

- Mostra os trabalhos da fila em um formato longo:

`lpq -l`

- Mostra os trabalhos da fila de uma impressora ou classe específica:

`lpq -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino[/instância]</span>

- Mostra os trabalhos na fila a cada n segundos até que a fila esteja vazia:

`lpq +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">intervalo</span>
