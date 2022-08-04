---
layout: page
title: common/salt-key (English)
description: "Manages salt minion keys on the salt master."
content_hash: c874fc3f83bf39e5e47b04de120a130d3f0c6fbe
---
# salt-key

Manages salt minion keys on the salt master.
Needs to be run on the salt master, likely as root or with sudo.
More information: <https://docs.saltstack.com/ref/cli/salt-key.html>.

- List all accepted, unaccepted and rejected minion keys:

`salt-key -L`

- Accept a minion key by name:

`salt-key -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MINION_ID</span>

- Reject a minion key by name:

`salt-key -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MINION_ID</span>

- Print fingerprints of all public keys:

`salt-key -F`
