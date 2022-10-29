---
layout: page
title: common/fdp (português (Brasil))
description: "Renderiza uma imagem de um gráfico de rede `force-directed` a partir de um arquivo `graphviz`."
content_hash: eca28a4f6002dea4af4b081d556e8ce1859055cf
related_topics:
  - title: English version
    url: /en/common/fdp.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># fdp

Renderiza uma imagem de um gráfico de rede `force-directed` a partir de um arquivo `graphviz`.
Layouts: `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage` & `patchwork`.
Mais informações: <https://graphviz.org/doc/info/command.html>.

- Renderiza uma imagem `png` com um nome de arquivo baseado no nome do arquivo de entrada e formato de saída (-O maiúsculo):

`fdp -T png -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/entrada.gv</span>

- Renderiza uma imagem `svg` com o nome do arquivo de saída especificado (-o minúsculo):

`fdp -T svg -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/imagem.svg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/entrada.gv</span>

- Renderiza a saída nos formatos:

`fdp -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ps|pdf|svg|fig|png|gif|jpg|json|dot</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/entrada.gv</span>

- Renderiza uma imagem `gif` usando stdin e stdout:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">digraph {isso -> aquilo} </span>`" | fdp -T gif > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/imagem.gif</span>

- Exibe ajuda:

`fdp -?`
