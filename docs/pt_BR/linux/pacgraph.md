---
layout: page
title: linux/pacgraph (português (Brasil))
description: "Desenha um grafo de pacotes instalados para PNG/SVG/GUI/console."
content_hash: 234f14b9587f05d10f0235f3da511fc424a8b9a9
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/linux/pacgraph.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/pacgraph.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacgraph

Desenha um grafo de pacotes instalados para PNG/SVG/GUI/console.
Mais informações: <https://github.com/keenerd/pacgraph>.

- Produz um grafo em SVG e PNG:

`pacgraph`

- Produz um grafo SVG:

`pacgraph --svg`

- Imprime um resumo para o console:

`pacgraph --console`

- Substitui o nome de arquivo ou local padrão (Nota: não especifique a extensão do arquivo):

`pacgraph --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Altera a cor dos pacotes que não são dependências:

`pacgraph --top=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cor</span>

- Altera a cor das dependências de pacotes:

`pacgraph --dep=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cor</span>

- Altera a cor de fundo de um grafo:

`pacgraph --background=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cor</span>

- Altera a cor dos links entre pacotes:

`pacgraph --link=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cor</span>
