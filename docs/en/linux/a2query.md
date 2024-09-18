---
layout: page
title: linux/a2query (English)
description: "Retrieve runtime configuration from Apache on Debian-based OSes."
content_hash: 1f432b3f47a1715c0ed90ffbcd98dcf8d7e8e232
last_modified_at: 2024-09-18
related_topics:
  - title: català version
    url: /ca/linux/a2query.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/a2query.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/a2query.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/a2query.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/a2query.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/a2query.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/a2query.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/a2query.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/a2query.html
    icon: bi bi-globe
tldri18n_status: 2
---
# a2query

Retrieve runtime configuration from Apache on Debian-based OSes.
More information: <https://manned.org/a2query>.

- List enabled Apache modules:

`sudo a2query -m`

- Check if a specific module is installed:

`sudo a2query -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- List enabled virtual hosts:

`sudo a2query -s`

- Display the currently enabled Multi Processing Module:

`sudo a2query -M`

- Display Apache version:

`sudo a2query -v`
