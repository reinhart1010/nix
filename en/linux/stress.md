---
layout: page
title: linux/stress (English)
description: "A tool to stress test CPU, memory, and IO on a Linux system."
content_hash: d35aa9fe3c28866aad97b849242a2506260008ee
---
# stress

A tool to stress test CPU, memory, and IO on a Linux system.

- Spawn 4 workers to stress test CPU:

`stress -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Spawn 2 workers to stress test IO and timeout after 5 seconds:

`stress -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Spawn 2 workers to stress test memory (each worker allocates 256M bytes):

`stress -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --vm-bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">256M</span>

- Spawn 2 workers spinning on write()/unlink() (each worker writes 1G bytes):

`stress -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --hdd-bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1GB</span>
