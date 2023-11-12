---
layout: page
title: common/alex (português (Brasil))
description: "Uma ferramenta que captura escrita insensível e sem consideraçāo."
content_hash: f3d35122be1f29061b55ee57a26038c0c699aeeb
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/alex.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/alex.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/alex.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/alex.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/alex.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/alex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# alex

Uma ferramenta que captura escrita insensível e sem consideraçāo.
Ajuda a encontrar no texto, frases favorecedoras de gênero, polarizantes, relacionadas à raça, insensíveis à religiao e outras frases desiguais.
Mais informações: <https://github.com/get-alex/alex>.

- Analisa o texto do `stdin`:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A rede dele parece boa</span>` | alex --stdin`

- Analisa todos arquivos no diretório atual:

`alex`

- Analisa um arquivo específico:

`alex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_do_texto.md</span>

- Analisa todos arquivos em Markdown exceto `example.md`:

`alex *.md !`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.md</span>
