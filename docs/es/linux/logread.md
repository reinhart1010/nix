---
layout: page
title: linux/logread (español)
description: "Lee el registro de la memoria cíclica `logd`."
content_hash: b7088235c1f3d99d70140fd2fc2031b07dbf9d7a
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/logread.html
    icon: bi bi-globe
tldri18n_status: 2
---
# logread

Lee el registro de la memoria cíclica `logd`.
Más información: <https://openwrt.org/docs/guide-user/base-system/log.essentials>.

- Imprime el registro:

`logread`

- Imprime un número determinado de mensajes:

`logread -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>

- Filtra los mensajes por (palabra clave/expresión regular):

`logread -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón</span>

- Imprime los mensajes de registro a medida que se producen:

`logread -f`
