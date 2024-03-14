---
layout: page
title: common/ssh-keyscan (English)
description: "Get the public SSH keys of remote hosts."
content_hash: e518278455dff2e8e048fb3a6fa1dcb71895422a
last_modified_at: 2024-03-14
related_topics:
  - title: Deutsch version
    url: /de/common/ssh-keyscan.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh-keyscan.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ssh-keyscan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh-keyscan

Get the public SSH keys of remote hosts.
More information: <https://man.openbsd.org/ssh-keyscan>.

- Retrieve all public SSH keys of a remote host:

`ssh-keyscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Retrieve all public SSH keys of a remote host listening on a specific port:

`ssh-keyscan -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Retrieve certain types of public SSH keys of a remote host:

`ssh-keyscan -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsa,dsa,ecdsa,ed25519</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Manually update the SSH known_hosts file with the fingerprint of a given host:

`ssh-keyscan -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` >> ~/.ssh/known_hosts`
