---
layout: page
title: linux/fatlabel (English)
description: "Sets or gets the label of a FAT32 partition."
content_hash: 857ca48f93848bf3ecec4e1e044e840dec39ba53
last_modified_at: 2023-11-12
related_topics:
  - title: polski version
    url: /pl/linux/fatlabel.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/fatlabel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fatlabel

Sets or gets the label of a FAT32 partition.
More information: <https://manned.org/fatlabel>.

- Get the label of a FAT32 partition:

`fatlabel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>

- Set the label of a FAT32 partition:

`fatlabel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdc3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_label</span>`"`
