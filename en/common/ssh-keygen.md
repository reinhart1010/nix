---
layout: page
title: common/ssh-keygen (English)
description: "Generate ssh keys used for authentication, password-less logins, and other things."
content_hash: 4c93eb4383429172eec2ebe4b73cd9e96702857c
related_topics:
  - title: Deutsch version
    url: /de/common/ssh-keygen.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh-keygen.html
    icon: bi bi-globe
---
# ssh-keygen

Generate ssh keys used for authentication, password-less logins, and other things.
More information: <https://man.openbsd.org/ssh-keygen>.

- Generate a key interactively:

`ssh-keygen`

- Specify file in which to save the key:

`ssh-keygen -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/filename</span>

- Generate an ed25519 key with 100 key derivation function rounds:

`ssh-keygen -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ed25519</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Generate an RSA 4096-bit key with email as a comment:

`ssh-keygen -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dsa|ecdsa|ed25519|rsa</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4096</span>` -C "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comment|email</span>`"`

- Remove the keys of a host from the known_hosts file (useful when a known host has a new key):

`ssh-keygen -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>

- Retrieve the fingerprint of a key in MD5 Hex:

`ssh-keygen -l -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">md5</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/filename</span>

- Change the password of a key:

`ssh-keygen -p -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/filename</span>

- Change the type of the key format (for example from OPENSSH format to PEM), the file will be rewritten in-place:

`ssh-keygen -p -N "" -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PEM</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/OpenSSH_private_key</span>
