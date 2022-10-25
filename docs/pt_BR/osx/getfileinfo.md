---
layout: page
title: osx/getfileinfo (português (Brasil))
description: "Obtém informações sobre um arquivo em um diretório HFS+."
content_hash: 014950b2a4e54f6d487ff7810d5947d483f85e4c
related_topics:
  - title: English version
    url: /en/osx/getfileinfo.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/getfileinfo.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># GetFileInfo

Obtém informações sobre um arquivo em um diretório HFS+.
Mais informações: <https://www.unix.com/man-page/osx/1/GetFileInfo/>.

- Exibe informações sobre um determinado arquivo:

`GetFileInfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/nome_do_arquivo</span>

- Exibe a data e hora em que um determinado arquivo foi criado:

`GetFileInfo -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/nome_do_arquivo</span>

- Exibe a data e hora em que um determinado arquivo foi modificado pela última vez:

`GetFileInfo -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/nome_do_arquivo</span>

- Exibe o criador de um determinado arquivo:

`GetFileInfo -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/nome_do_arquivo</span>
