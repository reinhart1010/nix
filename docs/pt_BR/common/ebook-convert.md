---
layout: page
title: common/ebook-convert (português (Brasil))
description: "Pode ser usado para converter e-books entre os fomatos comuns, como PDF, EPUB e MOBI."
content_hash: 387636a429d5f0298c567c2fbc3d3f89872abad5
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ebook-convert.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ebook-convert.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ebook-convert.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ebook-convert

Pode ser usado para converter e-books entre os fomatos comuns, como PDF, EPUB e MOBI.
Faz parte da biblioteca de ferramentas Calibre e-book.
Mais informações: <https://manual.calibre-ebook.com/generated/en/ebook-convert.html>.

- Converte um e-book em outro formato:

`ebook-convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_entrada</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_saída</span>

- Converte Markdown ou HTML em um e-book com ToC, título e autor:

`ebook-convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_entrada</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_saída</span>` --level1-toc="//h:h1" --level2-toc="//h:h2" --level3-toc="//h:h3" --title=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">titulo</span>` --authors=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">autor</span>
