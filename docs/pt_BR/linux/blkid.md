---
layout: page
title: linux/blkid (português (Brasil))
description: "Lista todas as partições reconhecidas e seu Identificador Único Universal (UUID)."
content_hash: 61c5af297d1465fb231fe19570ed98fd61f313ab
related_topics:
  - title: English version
    url: /en/linux/blkid.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/blkid.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># blkid

Lista todas as partições reconhecidas e seu Identificador Único Universal (UUID).
Mais informações: <https://manned.org/blkid>.

- Lista todas as partições:

`sudo blkid`

- Lista todas as partições em uma tabela, incluindo os pontos de montagem atuais:

`sudo blkid -o list`
