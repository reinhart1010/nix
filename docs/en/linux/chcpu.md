---
layout: page
title: linux/chcpu (English)
description: "Enable/disable a system's CPUs."
content_hash: 89cab70595ad0fd1f29a10ed41708154580458d4
last_modified_at: 2024-02-09
related_topics:
  - title: polski version
    url: /pl/linux/chcpu.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chcpu

Enable/disable a system's CPUs.
More information: <https://manned.org/chcpu>.

- Disable one or more CPUs by their IDs:

`chcpu -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,3</span>

- Enable one or more ranges of CPUs by their IDs:

`chcpu -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-3,5-7</span>
