---
layout: page
title: osx/dmesg (português (Brasil))
description: "Exibe mensagens do kernel na saída padrão."
content_hash: cbda535bb6ce2d955de23b9f104ff80432ea3486
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/dmesg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dmesg

Exibe mensagens do kernel na saída padrão.
Mais informações: <https://keith.github.io/xcode-man-pages/dmesg.8.html>.

- Exibe mensagens do kernel:

`dmesg`

- Exibe quanta memória física está disponível no sistema:

`dmesg | grep -i memory`

- Exibe mensagens do kernel, 1 página por vez:

`dmesg | less`
