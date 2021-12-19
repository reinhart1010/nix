---
layout: page
title: linux/modinfo (English)
description: "Extract information about a Linux kernel module."
content_hash: 9bff3e99ce8526a041ae8901f7f5ad14ab6e2af3
related_topics:
  - title: italiano version
    url: /it/linux/modinfo.html
    icon: bi bi-globe
---
# modinfo

Extract information about a Linux kernel module.
More information: <https://manned.org/modinfo>.

- List all attributes of a kernel module:

`modinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kernel_module</span>

- List the specified attribute only:

`modinfo -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">author|description|license|parm|filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kernel_module</span>
