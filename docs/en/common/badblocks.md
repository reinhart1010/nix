---
layout: page
title: common/badblocks (English)
description: "Search a device for bad blocks."
content_hash: 88605b2f0f1d5655a7721ede35dfd89397cc6d99
last_modified_at: 2024-02-09
related_topics:
  - title: italiano version
    url: /it/common/badblocks.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/badblocks.html
    icon: bi bi-globe
tldri18n_status: 2
---
# badblocks

Search a device for bad blocks.
Some usages of badblocks can cause destructive actions, such as erasing all data on a disk, including the partition table.
More information: <https://manned.org/badblocks>.

- Search a disk for bad blocks by using a non-destructive read-only test:

`sudo badblocks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Search an unmounted disk for bad blocks with a [n]on-destructive read-write test:

`sudo badblocks -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Search an unmounted disk for bad blocks with a destructive [w]rite test:

`sudo badblocks -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Use the destructive [w]rite test and [s]how [v]erbose progress:

`sudo badblocks -svw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- In destructive mode, [o]utput found blocks to a file:

`sudo badblocks -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Use the destructive mode with improved speed using 4K [b]lock size and 64K block [c]ount:

`sudo badblocks -w -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4096</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">65536</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
