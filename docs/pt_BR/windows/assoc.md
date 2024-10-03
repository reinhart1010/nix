---
layout: page
title: windows/assoc (português (Brasil))
description: "Exibir ou alterar associações entre extensões de arquivo e tipos de arquivos."
content_hash: bc7241435f71211ebcafa8ff488a49e08c7a6453
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/windows/assoc.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/assoc.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/assoc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/assoc.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># assoc

Exibir ou alterar associações entre extensões de arquivo e tipos de arquivos.
Mais informações: <https://learn.microsoft.com/windows-server/administration/windows-commands/assoc>.

- Lista todas as associações entre extensões de arquivo e tipos de arquivos:

`assoc`

- Exibe o tipo de arquivo associado para uma extensão específica:

`assoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.txt</span>

- Define o tipo de arquivo associado para uma extensão específica:

`assoc .`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txt</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivotxt</span>

- Exibe a saída de `assoc` uma tela por vez:

`assoc | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">more</span>
