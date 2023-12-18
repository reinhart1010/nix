---
layout: page
title: common/lpq (português (Brasil))
description: "Mostra o estado da fila de impressão."
content_hash: fb5bdd6708241e6046b084a745f53665f6d5c91c
last_modified_at: 2023-12-18
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

- Mostrar os trabalhos na fila de todas as impressoras usando criptografia:

`lpq -a -E`

- Mostrar os trabalhos da fila em um formato longo:

`lpq -l`

- Mostra os trabalhos da fila de uma impressora ou classe específica:

`lpq -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino[/instância]</span>

- Mostra os trabalhos na fila a cada n segundos até que a fila esteja vazia:

`lpq +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">intervalo</span>
