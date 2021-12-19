---
layout: page
title: common/sum (English)
description: "Compute checksums and the number of blocks for a file."
content_hash: 6daf6295c5f77a0543c43884670138143436f4d2
related_topics:
  - title: தமிழ் version
    url: /ta/common/sum.html
    icon: bi bi-globe
---
# sum

Compute checksums and the number of blocks for a file.
A predecessor to the more modern `cksum`.
More information: <https://www.gnu.org/software/coreutils/sum>.

- Compute a checksum with BSD-compatible algorithm and 1024-byte blocks:

`sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Compute a checksum with System V-compatible algorithm and 512-byte blocks:

`sum --sysv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>
