---
layout: page
title: linux/lsblk (English)
description: "Lists information about devices."
content_hash: bbf437f4d5e5bfdcfa2ebb323cd5e961d17d66dd
last_modified_at: 2023-11-12
related_topics:
  - title: हिन्दी version
    url: /hi/linux/lsblk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/lsblk.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/linux/lsblk.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/lsblk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/lsblk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lsblk

Lists information about devices.
More information: <https://manned.org/lsblk>.

- List all storage devices in a tree-like format:

`lsblk`

- Also list empty devices:

`lsblk -a`

- Print the SIZE column in bytes rather than in a human-readable format:

`lsblk -b`

- Output info about filesystems:

`lsblk -f`

- Use ASCII characters for tree formatting:

`lsblk -i`

- Output info about block-device topology:

`lsblk -t`

- Exclude the devices specified by the comma-separated list of major device numbers:

`lsblk -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,7</span>

- Display a customized summary using a comma-separated list of columns:

`lsblk --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">NAME</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SERIAL</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MODEL</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TRAN</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TYPE</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIZE</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FSTYPE</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MOUNTPOINT</span>
