---
layout: page
title: linux/growpart (English)
description: "Extend a partition in a disk or disk image to fill available space."
content_hash: 6091d4f6e2fc894b36ca9344cefc617aba0fe79d
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/growpart.html
    icon: bi bi-globe
tldri18n_status: 2
---
# growpart

Extend a partition in a disk or disk image to fill available space.
More information: <https://github.com/canonical/cloud-utils>.

- Extend partition `n` from `sdX` to fill empty space until end of disk or beginning of next partition:

`growpart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- Show what modifications would be made when growing partition `n` in a disk image:

`growpart --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/disk.img</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>
