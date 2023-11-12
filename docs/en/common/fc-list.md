---
layout: page
title: common/fc-list (English)
description: "List available fonts installed on the system."
content_hash: 5d6b74cc87975fbbcd3c0d3dc4b2ceab67b9e561
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/fc-list.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/fc-list.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fc-list

List available fonts installed on the system.
More information: <https://manned.org/fc-list>.

- Return a list of installed fonts in your system:

`fc-list`

- Return a list of installed fonts with given name:

`fc-list | grep '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DejaVu Serif</span>`'`

- Return the number of installed fonts in your system:

`fc-list | wc -l`
