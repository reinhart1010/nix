---
layout: page
title: linux/xrandr (português (Brasil))
description: "Define o tamanho, orientação e/ou espelhamento das saídas para uma tela."
content_hash: 358c8e4308817a9aa5899072aa984ed0b79a7392
last_modified_at: 2024-05-23
related_topics:
  - title: Deutsch version
    url: /de/linux/xrandr.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/xrandr.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/xrandr.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xrandr

Define o tamanho, orientação e/ou espelhamento das saídas para uma tela.
Mais informações: <https://www.x.org/releases/current/doc/man/man1/xrandr.1.xhtml>.

- Exibe o estado atual do sistema (telas conhecidas, resoluções, ...):

`xrandr --query`

- Desativa saídas desconectadas e ativa as conectadas com as configurações padrão:

`xrandr --auto`

- Altera a resolução e frequência de atualização da DisplayPort 1 para 1920x1080, 60Hz:

`xrandr --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DP1</span>` --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1920x1080</span>` --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>

- Define a resolução do HDMI2 para 1280x1024 e o coloca à direita de DP1:

`xrandr --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HDMI2</span>` --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1280x1024</span>` --right-of `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DP1</span>

- Desativa a saída VGA1:

`xrandr --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VGA1</span>` --off`

- Define o brilho de LVDS1 como 50%:

`xrandr --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LVDS1</span>` --brightness `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5</span>
