---
layout: page
title: common/ssh-keyscan (English)
description: "Get the public ssh keys of remote hosts."
content_hash: 9832f92cdbc9e351b68d39086d8cb4ef482f7892
related_topics:
  - title: Deutsch version
    url: /de/common/ssh-keyscan.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh-keyscan.html
    icon: bi bi-globe
---
# ssh-keyscan

Get the public ssh keys of remote hosts.
More information: <https://man.openbsd.org/ssh-keyscan>.

- Retrieve all public ssh keys of a remote host:

`ssh-keyscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Retrieve all public ssh keys of a remote host listening on a specific port:

`ssh-keyscan -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Retrieve certain types of public ssh keys of a remote host:

`ssh-keyscan -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsa,dsa,ecdsa,ed25519</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Manually update the ssh known_hosts file with the fingerprint of a given host:

`ssh-keyscan -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` >> ~/.ssh/known_hosts`
