---
layout: page
title: common/gocryptfs (English)
description: "Encrypted overlay filesystem written in Go."
content_hash: 5114dfc0103832467b7433bf742b944d220beef2
related_topics:
  - title: italiano version
    url: /it/common/gocryptfs.html
    icon: bi bi-globe
---
# gocryptfs

Encrypted overlay filesystem written in Go.
More information: <https://github.com/rfjakob/gocryptfs>.

- Initialize an encrypted filesystem:

`gocryptfs -init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/cipher_dir</span>

- Mount an encrypted filesystem:

`gocryptfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/cipher_dir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>

- Mount with the explicit master key instead of password:

`gocryptfs --masterkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/cipher_dir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>

- Change the password:

`gocryptfs --passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/cipher_dir</span>

- Make an encrypted snapshot of a plain directory:

`gocryptfs --reverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/plain_dir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/cipher_dir</span>
