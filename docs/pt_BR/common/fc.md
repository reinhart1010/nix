---
layout: page
title: common/fc (português (Brasil))
description: "Abre o último comando executado em um editor de texto."
content_hash: ff709eae512a1cd92a97d69db11a9847b8b2c503
last_modified_at: 2024-11-17
related_topics:
  - title: English version
    url: /en/common/fc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/fc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/fc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/fc.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># fc

Abre o último comando executado em um editor de texto.
Mais informações: <https://manned.org/fc>.

- Abre o último comando executado no editor de texto padrão do sistema:

`fc`

- Especifica o editor de texto que será utilizado ao executar o comando:

`fc -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'emacs'</span>

- Exibe um histórico dos últimos comandos executados:

`fc -l`

- Lista os comandos recentes em ordem reversa:

`fc -l -r`

- Edita e executa um comando do histórico:

`fc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número</span>

- Edita comandos em um dado intervalo e executa-os:

`fc '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">416</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">420</span>`'`

- Mosta ajuda:

`fc --help`
