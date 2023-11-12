---
layout: page
title: linux/addpart (English)
description: "Tells the Linux kernel about the existence of the specified partition."
content_hash: d936bb30401926b740ee96781b9cd8bc2a63faca
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/addpart.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/addpart.html
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

Tells the Linux kernel about the existence of the specified partition.
The command is a simple wrapper around the `add partition` ioctl.
More information: <https://manned.org/addpart>.

- Tell the kernel about the existence of the specified partition:

`addpart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">partition</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">length</span>
