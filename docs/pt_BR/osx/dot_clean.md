---
layout: page
title: osx/dot_clean (português (Brasil))
description: "Mescla ._* arquivos com arquivos nativos correspondentes."
content_hash: 019c05f9525acc605cea7fb413bf0b749c4e14ea
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/dot_clean.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/dot_clean.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dot_clean

Mescla ._* arquivos com arquivos nativos correspondentes.
Mais informações: <https://keith.github.io/xcode-man-pages/dot_clean.1.html>.

- Mescla todos os `._*` arquivos recursivamente:

`dot_clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Não mescla recursivamente todos `._*` em um diretório (flat merge):

`dot_clean -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Mescla e exclui todos os arquivos `._*`:

`dot_clean -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Somente exclui arquivos `._*` se houver um arquivo nativo correspondente:

`dot_clean -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Segue os links simbólicos:

`dot_clean -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Imprime saída verbosa:

`dot_clean -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>
