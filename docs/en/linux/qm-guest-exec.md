---
layout: page
title: linux/qm-guest-exec (English)
description: "Execute a specific command via a guest agent."
content_hash: 848018a055bd4619e59869dfab3addfb6114afbc
last_modified_at: 2022-12-19
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># qm guest exec

Execute a specific command via a guest agent.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Execute a specific command via a guest agent:

`qm guest exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arg1 arg2 ...</span>

- Execute a specific command via a guest agent asynchronously:

`qm guest exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arg1 arg2 ...</span>` --synchronous 0`

- Execute a specific command via a guest agent with a specified timeout of 10 seconds:

`qm guest exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arg1 arg2 ...</span>` --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Execute a specific command via a guest agent and forward input from STDIN until EOF to the guest agent:

`qm guest exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arg1 arg2 ...</span>` --pass-stdin 1`
