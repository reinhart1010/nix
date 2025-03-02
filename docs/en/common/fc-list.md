---
layout: page
title: common/fc-list (English)
description: "List available fonts installed on the system."
content_hash: 01926c407cf1f3ba5de455d215747a54b49fc879
last_modified_at: 2025-01-05
related_topics:
  - title: español version
    url: /es/common/fc-list.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/fc-list.html
    icon: bi bi-globe
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

- Return a list of installed fonts that support the language based on its locale code:

`fc-list :lang=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jp</span>

- Return a list of installed fonts that contain the glyph specified by its Unicode code-point:

`fc-list :charset=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f303</span>
