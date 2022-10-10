---
layout: page
title: osx/dmesg (português (Brasil))
description: "Exibe mensagens do kernel na saída padrão."
content_hash: 50262165a2a62f3e637cb14cee1a268c9c893d40
related_topics:
  - title: English version
    url: /en/osx/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/dmesg.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dmesg

Exibe mensagens do kernel na saída padrão.
Mais informações: <https://www.manpagez.com/man/8/dmesg/>.

- Exibe mensagens do kernel:

`dmesg`

- Exibe quanta memória física está disponível no sistema:

`dmesg | grep -i memory`

- Exibe mensagens do kernel, 1 página por vez:

`dmesg | less`
