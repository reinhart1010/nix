---
layout: page
title: osx/bless (English)
description: "Set volume boot capability and startup disk options."
content_hash: 1780bd5ee431f18a6616a9b3e29fc8facef3fb23
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/bless.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/bless.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bless

Set volume boot capability and startup disk options.
More information: <https://keith.github.io/xcode-man-pages/bless.1.html>.

- Bless a volume with only Mac OS X or Darwin, and create the BootX and `boot.efi` files as needed:

`bless --folder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/Volumes/Mac OS X/System/Library/CoreServices</span>` --bootinfo --bootefi`

- Set a volume containing either Mac OS 9 and Mac OS X to be the active volume:

`bless --mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/Volumes/Mac OS</span>` --setBoot`

- Set the system to NetBoot and broadcast for an available server:

`bless --netboot --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bsdp://255.255.255.255</span>

- Gather information about the currently selected volume (as determined by the firmware), suitable for piping to a program capable of parsing Property Lists:

`bless --info --plist`
