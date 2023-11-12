---
layout: page
title: linux/poweroff (português (Brasil))
description: "Desliga o sistema."
content_hash: 220a5d1ef7c129dcecf7d44c63dc9fb9bfaafbef
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/poweroff.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/poweroff.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/poweroff.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/poweroff.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/poweroff.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/poweroff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# poweroff

Desliga o sistema.
Mais informações: <https://www.man7.org/linux/man-pages/man8/poweroff.8.html>.

- Desliga o sistema:

`poweroff`

- Para o sistema (mesmo que `halt`):

`poweroff --halt`

- Reinicia o sistema (mesmo que `reboot`):

`poweroff --reboot`

- Desliga imediatamente sem contato com o gerenciador do sistema:

`poweroff --force --force`

- Grava a entrada de desligamento wtmp sem desligar o sistema:

`poweroff --wtmp-only`
