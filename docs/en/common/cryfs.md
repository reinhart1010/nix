---
layout: page
title: common/cryfs (English)
description: "A cryptographic filesystem for the cloud."
content_hash: 4551a8510b0dda2bcda2abd08810b77de9191261
last_modified_at: 2024-01-31
related_topics:
  - title: 한국어 version
    url: /ko/common/cryfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cryfs

A cryptographic filesystem for the cloud.
More information: <https://www.cryfs.org/>.

- Mount an encrypted filesystem. The initialization wizard will be started on the first execution:

`cryfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/cipher_dir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>

- Unmount an encrypted filesystem:

`cryfs-unmount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>

- Automatically unmount after ten minutes of inactivity:

`cryfs --unmount-idle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/cipher_dir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>

- List supported ciphers:

`cryfs --show-ciphers`
