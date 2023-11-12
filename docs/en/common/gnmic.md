---
layout: page
title: common/gnmic (English)
description: "A gNMI command-line client."
content_hash: 3570fd10a8d830567bfab3f571617fbb694447a2
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gnmic

A gNMI command-line client.
Manage gNMI network device configuration and view operational data.
More information: <https://gnmic.kmrd.dev>.

- Request device capabilities:

`gnmic --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:port</span>` capabilities`

- Provide a username and password to fetch device capabilities:

`gnmic --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:port</span>` --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` capabilities`

- Get a snapshot of the device state at a specific path:

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:port</span>` get --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>

- Update device state at a specific path:

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:port</span>` set --update-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>` --update-value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Subscribe to target state updates under the subtree at a specific path:

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:port</span>` subscribe --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>
