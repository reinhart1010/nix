---
layout: page
title: linux/lsb_release (català)
description: "Proporciona informació específica de la distribució i LSB (Linux Standard Base)."
content_hash: 1d5728900e9b11096363275150449e7e591cf13e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/lsb_release.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/lsb_release.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/linux/lsb_release.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/lsb_release.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lsb_release

Proporciona informació específica de la distribució i LSB (Linux Standard Base).
Més informació: <https://manned.org/lsb_release>.

- Mostra tota la informació disponible:

`lsb_release -a`

- Mostra una descripció dels sistema operatiu (normalment el nom complet):

`lsb_release -d`

- Mostra només el nom del sistema operatiu (ID) sense el camp nom:

`lsb_release -i -s`

- Mostra el número de versió i el nom en clau de la distribució sense el camp nom:

`lsb_release -rcs`
