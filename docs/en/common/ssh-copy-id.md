---
layout: page
title: common/ssh-copy-id (English)
description: "Install your public key in a remote machine's authorized_keys."
content_hash: 14b30d38ab4b5749ac063a233ffbf4ea3a3fc912
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ssh-copy-id.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh-copy-id.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ssh-copy-id.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh-copy-id

Install your public key in a remote machine's authorized_keys.
More information: <https://manned.org/ssh-copy-id>.

- Copy your keys to the remote machine:

`ssh-copy-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username@remote_host</span>

- Copy the given public key to the remote:

`ssh-copy-id -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/certificate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>

- Copy the given public key to the remote with specific port:

`ssh-copy-id -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/certificate</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>
