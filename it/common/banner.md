---
layout: page
title: common/banner (italiano)
description: "Stampa il testo fornito per argomento come un grande banner in ASCII art."
content_hash: 0450458616cbec2ab662d844d9b206a08e0fc0c3
related_topics:
  - title: English version
    url: /en/common/banner.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/banner.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/banner.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/banner.html
    icon: bi bi-globe
---
# banner

Stampa il testo fornito per argomento come un grande banner in ASCII art.
Maggiori informazioni: <https://man.archlinux.org/man/banner.1>.

- Stampa il testo come un grande banner (le virgolette sono opzionali):

`banner "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`"`

- Stampa il testo come un banner con una larghezza di 50 caratteri:

`banner -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`"`

- Leggi testo da stdin:

`banner`
