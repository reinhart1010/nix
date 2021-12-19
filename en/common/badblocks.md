---
layout: page
title: common/badblocks (English)
description: "Search a device for bad blocks."
content_hash: 3295857d131f847e21b5eafb1612a035662c54c8
related_topics:
  - title: italiano version
    url: /it/common/badblocks.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/badblocks.html
    icon: bi bi-globe
---
# badblocks

Search a device for bad blocks.
Some usages of badblocks can cause destructive actions, such as erasing all data on a disk, including the partition table.
More information: <https://manned.org/badblocks>.

- Search a disk for bad blocks by using a non-destructive read-only test:

`sudo badblocks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Search an unmounted disk for bad blocks with a non-destructive read-write test:

`sudo badblocks -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Search an unmounted disk for bad blocks with a destructive write test:

`sudo badblocks -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Search an unmounted disk for bad blocks with a destructive write test and show verbose status:

`sudo badblocks -svw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Search an unmounted disk in destructive mode and output found blocks to a file:

`sudo badblocks -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Search an unmounted disk in destructive mode with improved speed using 4K block size and 64K block count:

`sudo badblocks -w -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4096</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">65536</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
