---
layout: page
title: linux/rm (português (Brasil))
description: "Remove arquivos ou diretórios."
content_hash: 616c4d67382af102e6e65a3dc4c2dbfdecf0ce0b
last_modified_at: 2023-10-15
related_topics:
  - title: English version
    url: /en/linux/rm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/rm.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rm

Remove arquivos ou diretórios.
Veja também: `rmdir`.
Mais informações: <https://www.gnu.org/software/coreutils/rm>.

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
