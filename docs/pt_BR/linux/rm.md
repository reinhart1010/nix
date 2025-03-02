---
layout: page
title: linux/rm (português (Brasil))
description: "Remove arquivos ou diretórios."
content_hash: 0e643977c16cffe625f1b605aae7d283e7f866a3
last_modified_at: 2025-03-02
related_topics:
  - title: العربية version
    url: /ar/linux/rm.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/rm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/rm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/rm.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/rm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rm

Remove arquivos ou diretórios.
Veja também: `rmdir`.
Mais informações: <https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html>.

- Remove arquivos específicos:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1 caminho/para/arquivo2 ...</span>

- Remove arquivos específicos ignorando os inexistentes:

`rm --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1 caminho/para/arquivo2 ...</span>

- Remove arquivos específicos interativamente avisando antes de cada remoção:

`rm --interactive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1 caminho/para/arquivo2 ...</span>

- Remove arquivos específicos imprimindo informações sobre cada remoção:

`rm --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1 caminho/para/arquivo2 ...</span>

- Remove arquivos e diretórios específicos recursivamente:

`rm --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretório1 caminho/para/arquivo_ou_diretório2 ...</span>

- Remove diretórios vazios (este é considerado o método seguro):

`rm --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>
