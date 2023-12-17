---
layout: page
title: common/lpq (português (Brasil))
description: "Mostra o estado da fila de impressão."
content_hash: fb5bdd6708241e6046b084a745f53665f6d5c91c
last_modified_at: 2023-12-17
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lpq.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lpq

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
