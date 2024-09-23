---
layout: page
title: linux/bspc (português (Brasil))
description: "Configura e controla `bspwm`, gerenciando nós, áreas de trabalho, monitores, e outros."
content_hash: 24406c9aab0b4f7fb93712b9916a86530d3b9a0d
last_modified_at: 2024-09-23
related_topics:
  - title: English version
    url: /en/linux/bspc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/bspc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/bspc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bspc

Configura e controla `bspwm`, gerenciando nós, áreas de trabalho, monitores, e outros.
Veja também: `bspwm`.
Mais informações: <https://github.com/baskerville/bspwm>.

- Define duas áreas de trabalho virtuais:

`bspc monitor --reset-desktops `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_area_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_area_2</span>

- Foca em uma área de trabalho determinada:

`bspc desktop --focus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero</span>

- Fecha as janelas atreladas ao nó selecionado:

`bspc node --close`

- Envia o nó selecionado para uma área de trabalho determinada:

`bspc node --to-desktop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero</span>

- Alterna o nó selecionado para modo de tela cheia:

`bspc node --state ~fullscreen`

- Define o valor de uma configuração específica:

`bspc config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_configuracao</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>
