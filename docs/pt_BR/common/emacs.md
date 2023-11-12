---
layout: page
title: common/emacs (português (Brasil))
description: "O editor extensível, personalizável, autodocumentável, com exibição em tempo real."
content_hash: b0034812e41074ae74d9dd11c7ed28398bdcf0bf
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/emacs.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/emacs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/emacs.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># emacs

O editor extensível, personalizável, autodocumentável, com exibição em tempo real.
Veja também `emacsclient`.
Mais informações: <https://www.gnu.org/software/emacs>.

- Inicia o Emacs e abra um arquivo:

`emacs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Abre um arquivo em uma linha especificada:

`emacs +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_linha</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Inicia o Emacs em modo console (sem uma janela X):

`emacs --no-window-system`

- Inicia um servidor Emacs em segundo plano (acessível através do `emacsclient`):

`emacs --daemon`

- Para um servidor Emacs em funcionamento e todas as suas instâncias, pedindo confirmação em arquivos não salvos:

`emacsclient --eval '(save-buffers-kill-emacs)'`

- Salva um arquivo em Emacs:

`Ctrl + X, Ctrl + S`

- Deixa o Emacs:

`Ctrl + X, Ctrl + C`
