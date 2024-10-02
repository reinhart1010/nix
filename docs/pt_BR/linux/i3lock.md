---
layout: page
title: linux/i3lock (português (Brasil))
description: "Bloqueador de tela simples para o gerenciador de janelas i3."
content_hash: 66a0793e1f17604a4703bdacbfc9e49d92404cce
last_modified_at: 2024-10-02
related_topics:
  - title: English version
    url: /en/linux/i3lock.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># i3lock

Bloqueador de tela simples para o gerenciador de janelas i3.
Mais informações: <https://i3wm.org/i3lock>.

- Bloqueia a tela com uma tela branca:

`i3lock`

- Bloqueia a tela com uma cor de fundo (formato rrggbb):

`i3lock --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0000ff</span>

- Bloqueia a tela com uma imagem PNG:

`i3lock --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/imagem.png</span>

- Bloqueia a tela e disabilita o indicador de desbloqueio (remove as resposta do sistema ao pressionar alguma tecla):

`i3lock --no-unlock-indicator`

- Bloqueia a tela e não esconde o ponteiro do mouse:

`i3lock --pointer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default</span>

- Bloqueia a tela com uma imagem PNG sendo mostrada em todos os monitores:

`i3lock --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/imagem.png</span>` --tiling`

- Bloqueia a tela e mostra o número de tentativas de login que falharam:

`i3lock --show-failed-attempts`
