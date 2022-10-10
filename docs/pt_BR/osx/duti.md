---
layout: page
title: osx/duti (português (Brasil))
description: "Define os aplicativos padrão para tipos de documentos e esquemas de URL no macOS."
content_hash: b45776a0b681017af9a4c93b808026689eb04772
related_topics:
  - title: English version
    url: /en/osx/duti.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/duti.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># duti

Define os aplicativos padrão para tipos de documentos e esquemas de URL no macOS.
Mais informações: <https://github.com/moretension/duti>.

- Define o Safari como o manipulador padrão de documentos HTML:

`duti -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.apple.Safari</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public.html</span>` all`

- Define o VLC como visualizador padrão para arquivos com extensões `.m4v`:

`duti -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.videolan.vlc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">m4v</span>` viewer`

- Define o Finder como o manipulador padrão para esquema de URL ftp://:

`duti -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.apple.Finder</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftp</span>`"`

- Exibe informações sobre o aplicativo padrão para uma determinada extensão:

`duti -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ext</span>

- Exibe o manipulador padrão para um determinado UTI:

`duti -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uti</span>

- Exibe todos os manipuladores de um determinado UTI:

`duti -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uti</span>
