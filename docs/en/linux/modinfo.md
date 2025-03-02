---
layout: page
title: linux/modinfo (English)
description: "Extract information about a Linux kernel module."
content_hash: 7a31d861a613b9e7293e2d193adbca2ec83b0cbd
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/modinfo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/modinfo.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/modinfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# modinfo

Extract information about a Linux kernel module.
See also: `kmod`, for other module management commands.
More information: <https://manned.org/modinfo>.

- List all attributes of a kernel module:

`modinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kernel_module</span>

- List the specified attribute only:

`modinfo -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">author|description|license|parm|filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kernel_module</span>
