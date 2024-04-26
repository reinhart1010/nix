---
layout: page
title: common/encfs (English)
description: "Mount or create encrypted virtual filesystems."
content_hash: 4b4ab27b2399a546a5e7d78c530ac3ad5db71ba6
last_modified_at: 2024-04-26
tldri18n_status: 2
---
# encfs

Mount or create encrypted virtual filesystems.
See also `fusermount`, which can unmount filesystems mounted by this command.
More information: <https://github.com/vgough/encfs>.

- Initialize or mount an encrypted filesystem:

`encfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/cipher_dir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/mount_point</span>

- Initialize an encrypted filesystem with standard settings:

`encfs --standard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/cipher_dir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/mount_point</span>

- Run encfs in the foreground instead of spawning a daemon:

`encfs -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/cipher_dir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/mount_point</span>

- Mount an encrypted snapshot of a plain directory:

`encfs --reverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/plain_dir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/cipher_dir</span>
