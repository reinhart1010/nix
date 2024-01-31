---
layout: page
title: osx/du (português (Brasil))
description: "Uso do Disco: estima e resume o uso do espaço de arquivos e diretórios."
content_hash: a7314976a035b8eb53039f66a6461bb3310e699a
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/du.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/du.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/du.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/du.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/osx/du.html
    icon: bi bi-globe
tldri18n_status: 2
---
# du

Uso do Disco: estima e resume o uso do espaço de arquivos e diretórios.
Mais informações: <https://keith.github.io/xcode-man-pages/du.1.html>.

- Lista os tamanhos de um diretório e quaisquer subdiretórios, na unidade fornecida (KiB/MiB/GiB):

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">k|m|g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Lista os tamanhos de um diretório e quaisquer subdiretórios, em formato legível (ou seja, selecionando automaticamente a unidade apropriada para cada tamanho):

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Exibe o tamanho de um único diretório, em unidades legíveis:

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Lista os tamanhos legíveis de um diretório e de todos os arquivos e diretórios dentro dele:

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Lista os tamanhos legíveis de um diretório e quaisquer subdiretórios, até N níveis de profundidade:

`du -h -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Lista o tamanho legível de todos os arquivos `.jpg` nos subdiretórios do diretório atual e exibe um total cumulativo no final:

`du -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/*.jpg</span>
