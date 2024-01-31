---
layout: page
title: osx/csrutil (English)
description: "Manage the System Integrity Protection configuration."
content_hash: 76d4dcadd9a1aaaf34cf90cda096c03cfd24db89
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/csrutil.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/csrutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# csrutil

Manage the System Integrity Protection configuration.
More information: <https://keith.github.io/xcode-man-pages/csrutil.8.html>.

- Display the System Integrity Protection status:

`csrutil status`

- Disable the System Integrity Protection:

`csrutil disable`

- Enable the System Integrity Protection:

`csrutil enable`

- Display the list of allowed NetBoot sources:

`csrutil netboot list`

- Add an IPv4 address to the list of allowed NetBoot sources:

`csrutil netboot add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>

- Reset the System Integrity Protection status and clear the NetBoot list:

`csrutil clear`
