---
layout: page
title: linux/run0 (español)
description: "Eleva privilegios interactivamente."
content_hash: 7f4b6768bced001a202318d37618a105b9b06bc0
last_modified_at: 2024-11-16
related_topics:
  - title: English version
    url: /en/linux/run0.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/run0.html
    icon: bi bi-globe
tldri18n_status: 2
---
# run0

Eleva privilegios interactivamente.
Similar a `sudo`, pero no es un binario SUID, la autenticación tiene lugar a través de polkit, y los comandos se invocan desde un servicio `systemd`.
Más información: <https://www.freedesktop.org/software/systemd/man/latest/run0.html>.

- Ejecuta un comando como root:

`run0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Ejecuta un comando como otro usuario y/o grupo:

`run0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-u|--user</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario|uid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--group</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_grupo|gid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>
