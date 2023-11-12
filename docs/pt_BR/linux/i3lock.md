---
layout: page
title: linux/i3lock (português (Brasil))
description: "Bloqueador de tela simples para o i3wm."
content_hash: 5ed56d15250f2bfd2bf7d3c072c0e18183533276
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/i3lock.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># i3lock

Bloqueador de tela simples para o i3wm.
Mais informações: <https://i3wm.org/i3lock>.

- Bloqueia a tela com uma cor de fundo (formato rrggbb):

`i3lock -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0000ff</span>

- Bloqueia a tela com uma imagem PNG:

`i3lock -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local/da/imagem.png</span>

- Desabilita o indicador de desbloqueio (remove a resposta ao apertar teclas):

`i3lock -u`

- Exibe o ponteiro do mouse ao invés de ocultá-lo ('default' para o ponteiro padrão, 'win' para um ponteiro MS Windows):

`i3lock -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default|win</span>

- Bloqueia a tela com uma imagem PNG exibida em múltiplos monitores, com o ponteiro do mouse habilitado:

`i3lock -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local/da/imagem.png</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default|win</span>` -t`
