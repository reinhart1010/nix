---
layout: page
title: linux/e4defrag (English)
description: "Defragment an ext4 filesystem."
content_hash: ec87b9c88b99f0de63fa1d98417ff915e3d8db6e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# e4defrag

Defragment an ext4 filesystem.
More information: <https://manned.org/e4defrag>.

- Defragment the filesystem:

`e4defrag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- See how fragmented a filesystem is:

`e4defrag -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Print errors and the fragmentation count before and after each file:

`e4defrag -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
