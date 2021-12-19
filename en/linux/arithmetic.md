---
layout: page
title: linux/arithmetic (English)
description: "Quiz on simple arithmetic problems."
content_hash: dfb45c79c16ae15cad998d97590811eb8a1aa5ca
related_topics:
  - title: Deutsch version
    url: /de/linux/arithmetic.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/arithmetic.html
    icon: bi bi-globe
---
# arithmetic

Quiz on simple arithmetic problems.
More information: <https://manpages.debian.org/bsdgames/arithmetic.6.en.html>.

- Start an arithmetic quiz:

`arithmetic`

- Specify one or more arithmetic [o]peration symbols to get problems on them:

`arithmetic -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+|-|x|/</span>

- Specify a range. Addition and multiplication problems would feature numbers between 0 and range, inclusive. Subtraction and division problems would have required result and number to be operated on, between 0 and range:

`arithmetic -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>
