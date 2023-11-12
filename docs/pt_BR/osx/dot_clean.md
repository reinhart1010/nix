---
layout: page
title: osx/dot_clean (português (Brasil))
description: "Mescla ._* arquivos com arquivos nativos correspondentes."
content_hash: 77bbe9e37d16c443c0e3b60f986f87d7dbfb6150
last_modified_at: 2023-11-12
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
Mais informações: <https://ss64.com/osx/dot_clean.html>.

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
