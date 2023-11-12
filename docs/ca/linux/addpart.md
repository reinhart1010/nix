---
layout: page
title: linux/addpart (català)
description: "Comunica al linux kernel l'existència de la partició especificada."
content_hash: 552e5544b19737c54a9726195685fa4f72d34c69
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/addpart.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/addpart.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/addpart.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/addpart.html
    icon: bi bi-globe
tldri18n_status: 2
---
# addpart

Comunica al linux kernel l'existència de la partició especificada.
El commandament és un simple embolcall de `add partition` ioctl.
Més informació: <https://manned.org/addpart>.

- Comunica al kernel l'existència de la partició especificada:

`addpart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dispositiu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">partició</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inici</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">llargada</span>
