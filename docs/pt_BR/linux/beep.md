---
layout: page
title: linux/beep (português (Brasil))
description: "Utilitário que permite o computador emitir sons."
content_hash: 804cbf3a572fc753288f13d7a043a24eb49858f6
related_topics:
  - title: Deutsch version
    url: /de/linux/beep.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/beep.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/beep.html
    icon: bi bi-globe
---
# beep

Utilitário que permite o computador emitir sons.
Mais informações: <https://github.com/spkr-beep/beep>.

- Emitir um som:

`beep`

- Emitir um som repetidamente:

`beep -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repeticoes</span>

- Emitir um som em uma frequência (Hz) específica e com duração específica (milisegundos):

`beep -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">frequencia</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">duracao</span>

- Emitir cada frequência e duração como um som diferente:

`beep -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">frequencia</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">duracao</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">frequencia</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">duracao</span>

- Executar a escala de Dó maior:

`beep -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">262</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">294</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">330</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">349</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">392</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">440</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">494</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">523</span>
