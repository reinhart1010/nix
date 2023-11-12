---
layout: page
title: common/mv (português (Brasil))
description: "Movimentação de arquivos entre diretórios, ou renomeá-los."
content_hash: 40f6b9b54ba476f7ba0f76fb372d9d50036018ac
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/mv.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/mv.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/mv.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/mv.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/mv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/mv.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/mv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mv.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mv

Movimentação de arquivos entre diretórios, ou renomeá-los.
Mais informações: <https://www.gnu.org/software/coreutils/mv>.

- Move um arquivo para um diretório arbitrário:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/arquivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/destino</span>

- Move arquivos para outro diretório, mantendo os nomes dos arquivos:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/arquivo_1 percorso/del/arquivo_2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/destino</span>

- Não requisitar confirmação para sobrescrição de arquivos:

`mv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/arquivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/destino</span>

- Requisita confirmação para sobrescrição de arquivos, independentemente das permissões de arquivo:

`mv -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/arquivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/destino</span>

- Não sobrescrita arquivos existentes no diretório de destino:

`mv -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/arquivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/destino</span>

- Move os arquivos em modo Verbose, mostrando os arquivos após sua movimentação:

`mv -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/arquivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/destino</span>
