---
layout: page
title: common/asciidoctor (português (Brasil))
description: "Um processador que converte AsciiDoc em formatos publicáveis."
content_hash: c0a51e0ad1e0a810a2e5d3b9c73a1504cdf73200
related_topics:
  - title: English version
    url: /en/common/asciidoctor.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># asciidoctor

Um processador que converte AsciiDoc em formatos publicáveis.
Mais informações: <https://docs.asciidoctor.org>.

- Converte um arquivo `.adoc` em HTML (formato padrão de saída):

`asciidoctor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.adoc</span>

- Converte um arquivo `.adoc` em HTML e liga a uma folha de estilos CSS:

`asciidoctor -a stylesheet=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/estilos.css</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.adoc</span>

- Converte um arquivo `.adoc` em um HTML embutível, removendo tudo exceto o corpo:

`asciidoctor --embedded `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.adoc</span>

- Converte um arquivo `.adoc` em PDF usando a biblioteca `asciidoctor-pdf`:

`asciidoctor --backend=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` --require=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">asciidoctor-pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.adoc}`
