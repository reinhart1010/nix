---
layout: page
title: common/hostname (русский)
description: "Показ и изменение системного имени хоста."
content_hash: 6e6ea69d67c484bfde1dbb1c8b49daa9bc9da734
related_topics:
  - title: English version
    url: /en/common/hostname.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/hostname.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># hostname

Показ и изменение системного имени хоста.
Больше информации: <https://manned.org/hostname>.

- Показать имя хоста:

`hostname`

- Показать сетевой адрес, соответствующий имени хоста:

`hostname -i`

- Показать все сетевые адреса хоста:

`hostname -I`

- Показать полное доменное имя (FQDN, Fully Qualified Domain Name):

`hostname --fqdn`

- Задать имя хоста:

`hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">новое_имя</span>
