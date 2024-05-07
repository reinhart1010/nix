---
layout: page
title: linux/prime-run (English)
description: "Run a program using an alternative Nvidia graphics card."
content_hash: 0a81081c28a95a0ad4cc9327d193a505bb2a6524
last_modified_at: 2024-05-07
tldri18n_status: 2
---
# prime-run

Run a program using an alternative Nvidia graphics card.
More information: <https://wiki.archlinux.org/title/PRIME#PRIME_render_offload>.

- Run a program using a dedicated Nvidia GPU:

`prime-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Validate whether the Nvidia card is being used:

`prime-run glxinfo | grep "OpenGL renderer"`
