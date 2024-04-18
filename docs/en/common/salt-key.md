---
layout: page
title: common/salt-key (English)
description: "Manage salt minion keys on the salt master."
content_hash: e3d494e5500d317df3c40ffb36677cab4020bd8a
last_modified_at: 2024-04-18
tldri18n_status: 2
---
# salt-key

Manage salt minion keys on the salt master.
Needs to be run on the salt master, likely as root or with sudo.
More information: <https://docs.saltproject.io/en/latest/ref/cli/salt-key.html>.

- List all accepted, unaccepted and rejected minion keys:

`salt-key -L`

- Accept a minion key by name:

`salt-key -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MINION_ID</span>

- Reject a minion key by name:

`salt-key -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MINION_ID</span>

- Print fingerprints of all public keys:

`salt-key -F`
