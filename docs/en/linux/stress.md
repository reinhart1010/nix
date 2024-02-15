---
layout: page
title: linux/stress (English)
description: "Stress test CPU, memory, and IO on a Linux system."
content_hash: d62b4da19b21da15483f350f20211eb83df85a7d
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# stress

Stress test CPU, memory, and IO on a Linux system.
More information: <https://manned.org/stress>.

- Spawn 4 workers to stress test CPU:

`stress -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Spawn 2 workers to stress test IO and timeout after 5 seconds:

`stress -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Spawn 2 workers to stress test memory (each worker allocates 256M bytes):

`stress -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --vm-bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">256M</span>

- Spawn 2 workers spinning on write()/unlink() (each worker writes 1G bytes):

`stress -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --hdd-bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1GB</span>
