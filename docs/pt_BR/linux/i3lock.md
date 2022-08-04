---
layout: page
title: linux/i3lock (português (Brasil))
description: "Bloqueador de tela simples para o i3wm."
content_hash: 5ed56d15250f2bfd2bf7d3c072c0e18183533276
related_topics:
  - title: English version
    url: /en/linux/i3lock.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/i3lock.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

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
