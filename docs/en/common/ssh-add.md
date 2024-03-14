---
layout: page
title: common/ssh-add (English)
description: "Manage loaded SSH keys in the `ssh-agent`."
content_hash: 41177bcba3b3b34ff70b9400f315371e3d03f843
last_modified_at: 2024-03-14
related_topics:
  - title: français version
    url: /fr/common/ssh-add.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ssh-add.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ssh-add.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh-add

Manage loaded SSH keys in the `ssh-agent`.
Ensure that `ssh-agent` is up and running for the keys to be loaded in it.
More information: <https://man.openbsd.org/ssh-add>.

- Add the default SSH keys in `~/.ssh` to the ssh-agent:

`ssh-add`

- Add a specific key to the ssh-agent:

`ssh-add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/private_key</span>

- List fingerprints of currently loaded keys:

`ssh-add -l`

- Delete a key from the ssh-agent:

`ssh-add -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/private_key</span>

- Delete all currently loaded keys from the ssh-agent:

`ssh-add -D`

- Add a key to the ssh-agent and the keychain:

`ssh-add -K `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/private_key</span>
