---
layout: page
title: common/asciidoctor (português (Brasil))
description: "Um processador que converte AsciiDoc em formatos publicáveis."
content_hash: 48f5995237f4b0e3da82876c950615a28d104314
last_modified_at: 2024-01-10
related_topics:
  - title: English version
    url: /en/common/asciidoctor.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/asciidoctor.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/asciidoctor.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/asciidoctor.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/asciidoctor.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asciidoctor

Um processador que converte AsciiDoc em formatos publicáveis.
Mais informações: <https://docs.asciidoctor.org>.

- Converte um arquivo `.adoc` em HTML (formato padrão de saída):

`asciidoctor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.adoc</span>

- Converte um arquivo `.adoc` em HTML e liga a uma folha de estilos CSS:

`asciidoctor -a stylesheet=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/estilos.css</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.adoc</span>

- Converte um arquivo `.adoc` em um HTML embutível, removendo tudo exceto o corpo:

`asciidoctor --embedded `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.adoc</span>

- Converte um arquivo `.adoc` em PDF usando a biblioteca `asciidoctor-pdf`:

`asciidoctor --backend=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` --require=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">asciidoctor-pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.adoc</span>
